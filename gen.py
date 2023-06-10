import docker
import time
import socket
import pickle

def get_container_stats():
    client = docker.from_env()
    containers = client.containers.list()
    stats_list = []

    for container in containers:
        stats = container.stats(stream=False)
        storage_usage_gb = stats['memory_stats']['usage'] / (1024**3)  # Convert bytes to GB using memory usage
        container_stats = (
            container.id,
            container.name,
            stats['cpu_stats']['cpu_usage']['total_usage'] / stats['cpu_stats']['system_cpu_usage'] * 100,
            stats['memory_stats']['usage'] / stats['memory_stats']['limit'] * 100,
            storage_usage_gb
        )
        stats_list.append(container_stats)

    return stats_list

def send_system_snapshot():
    # Get the system snapshot
    system_snapshot = get_container_stats()

    # Create a socket and connect to the receiver
    host = 'localhost'
    port = 4747
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    try:
        # Continuously send the system snapshot
        while True:
            # Serialize the system snapshot using pickle
            serialized_data = pickle.dumps(system_snapshot)

            # Send the serialized data
            sock.sendall(serialized_data)
            
            print(system_snapshot)
            # Wait for a specified time interval before sending the next snapshot
            time.sleep(1)
            
    finally:
        # Close the socket connection in the finally block to ensure it's closed even if an exception occurs
        sock.close()

# Example usage
if __name__ == '__main__':
    print_interval = 0.2  # Print interval in seconds
    while True:
        send_system_snapshot()        
        time.sleep(print_interval)
