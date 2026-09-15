import socket

def start_tcp_client():
    server_name = '127.0.0.1'
    server_port = 12000
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((server_name, server_port))
        messages = ["Halo Server", "Ini pesan kedua", "Ini pesan ketiga tanpa delay"]
        
        for msg in messages:
            # Menambahkan delimiter \n di akhir pesan
            full_msg = msg + "\n"
            client_socket.send(full_msg.encode('utf-8'))
            
            # Menerima balasan
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Balasan: {response.strip()}")
            
    except ConnectionRefusedError:
        print("[ERROR] Koneksi ditolak. Pastikan TCPServer.py sudah berjalan.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_tcp_client()