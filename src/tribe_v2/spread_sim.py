from organs import Mata, Telinga, Jantung, Tangan, Kaki, Kulit
from brain import TribeNode

def deploy_organ(node, organ):
    """Kirim perintah ke node untuk mengaktifkan organ tertentu (simulasi)."""
    node.send_to_all(f"DEPLOY {organ.__class__.__name__}")

if __name__ == "__main__":
    node = TribeNode(port=10003)
    node.start()
    # Simulasi deploy organ
    mata = Mata()
    deploy_organ(node, mata)
    node.stop()
