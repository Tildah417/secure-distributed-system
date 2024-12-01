# Predefined credentials (in a real system, store securely)
credentials = {"user1": "password123", "user2": "securepass"}

def authenticate_client(conn):
    try:
        # Request username
        conn.send(b"Username: ")
        username = conn.recv(1024).decode()
        
        # Request password
        conn.send(b"Password: ")
        password = conn.recv(1024).decode()
        
        # Check credentials
        if username in credentials and credentials[username] == password:
            conn.send(b"Authentication successful")
            return True
        else:
            conn.send(b"Authentication failed")
            return False
    except Exception as e:
        print(f"Authentication error: {e}")
        return False

def handle_client_connection(conn):
    print("Connection established")
    
    # Authenticate the client
    if not authenticate_client(conn):
        print("Authentication failed, closing connection")
        conn.close()
        return
    
    print("Client authenticated successfully")
    while True:
        try:
            # Process requests as before
            request = conn.recv(1024).decode()
            if not request:
                break
            conn.send(b"OK")
            # Add your existing request handling logic here
        except Exception as e:
            print(f"Error: {e}")
            break
    conn.close()
    print("Connection closed")
