import ssl
import socket
import threading

# start server with ssl
def start_server(port):
    # create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # wrap the socket with ssl
    server_socket = ssl.wrap_socket(server_socket, server_side=True, certfile='server.crt', keyfile='server.key', ssl_version=ssl.PROTOCOL_TLS)

    #bind the server to the port
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"servr listening seculerly on port {port}")

    while True:
        # accept client connection
        conn, addr = server_socket.accept()
        print(f"secure connection establish with {addr}")

        # handle each client in a separate thread
        thread = threading.Thread(target=handle_client_connection, args=(conn,))
        thread.start()

    if __name__ == "__main__":
        start_server(PORT)