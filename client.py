import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443

def start_client():
    
    context = ssl.create_default_context()
    
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    secure_client = context.wrap_socket(client_socket, server_hostname=HOST)
    
    try:
        secure_client.connect((HOST, PORT))
        print("[+] Securely connected to Fingerprint Server.")
        print("Enter targets to fingerprint in 'IP:PORT' format (e.g., 93.184.216.34:80). Type 'exit' to quit.")
        
        while True:
            target = input("\nTarget (IP:PORT)> ")
            if not target:
                continue
            
            secure_client.sendall(target.encode())
            
            if target.lower() == 'exit':
                break
                
            response = secure_client.recv(4096).decode()
            print(f"[Server Response] {response.strip()}")
            
    except Exception as e:
        print(f"[-] Connection error: {e}")
    finally:
        secure_client.close()

if __name__ == "__main__":
    start_client()