import ssl
import socket

# Function to connect securely to the server
def connect_to_server(server_ip, server_port):
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Wrap the socket with SSL
    client_socket = ssl.wrap_socket(
        client_socket,
        ssl_version=ssl.PROTOCOL_TLS  # Use TLS for secure communication
    )
    
    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print("Secure connection established with the server")
    return client_socket

client_socket = connect_to_server(server_ip, server_port)
