import socket
import threading

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] Client {addr} terhubung.")
    buffer = ""
    try:
        while True:
            # Menerima data dari client
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            
            buffer += data
            # Memisahkan pesan berdasarkan delimiter '\n'
            while '\n' in buffer:
                message, buffer = buffer.split('\n', 1)
                print(f"[{addr}] Pesan diterima: {message}")
                
                # Mengirim balasan ke client
                response = f"Server merespon: {message}\n"
                conn.send(response.encode('utf-8'))
                
    except Exception as e:
        print(f"[ERROR] {addr}: {e}")
    finally:
        conn.close()
        print(f"[DISCONNECTED] Client {addr} terputus.")

def start_tcp_server():
    server_port = 12000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(5) # Melayani N koneksi
    
    print(f"[STARTING] TCP Server berjalan di port {server_port}...")
    
    while True:
        conn, addr = server_socket.accept()
        # Spawn thread baru untuk setiap client yang terhubung
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_tcp_server()