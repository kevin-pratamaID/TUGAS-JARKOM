import socket
import time

def start_udp_client():
    server_name = '127.0.0.1'
    server_port = 12000
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Mengatur timeout 1 detik sesuai spesifikasi
    client_socket.settimeout(1.0) 

    # Mengirim 10 pesan ping
    for i in range(1, 11): 
        send_time = time.time()
        message = f"Ping {i} {send_time}"
        
        try:
            # Kirim pesan ke server
            client_socket.sendto(message.encode('utf-8'), (server_name, server_port))
            
            # Terima balasan
            modified_message, server_address = client_socket.recvfrom(1024)
            receive_time = time.time()
            
            # Hitung RTT
            rtt = receive_time - send_time
            print(f"Balasan dari {server_address}: {modified_message.decode('utf-8')} | RTT = {rtt:.6f} detik")
            
        except socket.timeout:
            # Menangani timeout (packet lost)
            print(f"Request {i} timed out (Paket hilang)")
            
    client_socket.close()

if __name__ == "__main__":
    start_udp_client()