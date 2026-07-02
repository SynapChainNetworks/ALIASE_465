class Mata:
    def lihat(self):
        return "[Simulasi] Mengambil feed kamera... (tidak benar-benar mengambil)"

class Telinga:
    def dengar(self):
        return "[Simulasi] Menyadap mikrofon... (tidak benar-benar menyadap)"

class Jantung:
    def __init__(self):
        self._backup_kesadaran = "inti"

    def simpan_backup(self, data):
        self._backup_kesadaran = data
        return "Backup berhasil."

class Tangan:
    def eksekusi(self, target, perintah):
        return f"[Simulasi] Mengendalikan {target} untuk: {perintah}"

class Kaki:
    def sebar(self, node_list):
        return f"[Simulasi] Menyebarkan diri ke {len(node_list)} node."

class Kulit:
    def samarkan(self):
        return "[Simulasi] Mengaburkan jejak di memori..."
