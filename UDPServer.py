import socket
import random

def start_udp_server():
    server_port = 12000
    # Menggunakan SOCK_DGRAM untuk UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', server_port))
    
    print(f"[STARTING] UDP Health Checker Server berjalan di port {server_port}...")

    while True:
        # Menerima ping dari client
        message, client_address = server_socket.recvfrom(1024)
        print(f"[PING] Diterima dari {client_address}: {message.decode('utf-8')}")
        
        # Simulasi packet loss (opsional, hapus jika tidak diperlukan)
        # if random.randint(1, 10) <= 3: # 30% kemungkinan paket hilang
        #    continue 
            
        # Mengirim balik pesan (echo)
        server_socket.sendto(message, client_address)

if __name__ == "__main__":
    start_udp_server()