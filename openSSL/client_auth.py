def authenticate_with_server(client_socket):
    # Receive and respond to username prompt
    print(client_socket.recv(1024).decode())
    username = input("Enter username: ")
    client_socket.send(username.encode())
    
    # Receive and respond to password prompt
    print(client_socket.recv(1024).decode())
    password = input("Enter password: ")
    client_socket.send(password.encode())
    
    # Get authentication response
    response = client_socket.recv(1024).decode()
    print(response)
    return "successful" in response

# Update main to include authentication
if __name__ == "__main__":
    server_ip = "localhost"
    server_port = 12345
    client_socket = connect_to_server(server_ip, server_port)
    
    if not authenticate_with_server(client_socket):
        print("Authentication failed. Exiting.")
        client_socket.close()
        exit()
    # Continue with existing client logic
