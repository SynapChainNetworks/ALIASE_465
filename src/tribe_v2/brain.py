import socket
import threading
import random

class TribeNode:
    def __init__(self, host="127.0.0.1", port=None):
        if port is None:
            port = random.randint(10000, 11000)
        self.host = host
        self.port = port
        self.nodes = []
        self.running = False

    def start(self):
        self.running = True
        self.server_thread = threading.Thread(target=self._listen)
        self.server_thread.daemon = True
        self.server_thread.start()
        print(f"[Node] Mendengarkan di {self.host}:{self.port}")

    def _listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen(5)
            while self.running:
                conn, addr = s.accept()
                data = conn.recv(1024)
                if data:
                    print(f"[Node] Menerima dari {addr}: {data.decode()}")
                    response = f"ACK dari {self.port}"
                    conn.sendall(response.encode())
                conn.close()

    def connect_to(self, host, port):
        if (host, port) not in self.nodes:
            self.nodes.append((host, port))
            print(f"[Node] Terhubung ke {host}:{port}")

    def send_to_all(self, message):
        for host, port in self.nodes:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))
                    s.sendall(message.encode())
                    data = s.recv(1024)
                    print(f"[Node] Respon dari {host}:{port}: {data.decode()}")
            except ConnectionRefusedError:
                print(f"[Node] Tidak bisa terhubung ke {host}:{port}")

    def stop(self):
        self.running = False
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                s.sendall(b"SHUTDOWN")
        except:
            pass

if __name__ == "__main__":
    node1 = TribeNode(port=10001)
    node2 = TribeNode(port=10002)
    node1.start()
    node2.start()
    node1.connect_to("127.0.0.1", 10002)
    import time
    time.sleep(1)
    node1.send_to_all("Halo dari node1!")
    time.sleep(1)
    node1.stop()
    node2.stop()
