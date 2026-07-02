#!/usr/bin/env python3
import gnupg
import os

SECRET_FILE = "secrets/rahasia.txt.gpg"
PASSPHRASE = os.getenv("ALIASE_465_PASSPHRASE", "TribeV2_465_Masterkey")

def decrypt():
    if not os.path.exists(SECRET_FILE):
        print(f"File {SECRET_FILE} tidak ditemukan. Pastikan ada di folder secrets/")
        return
    
    gpg = gnupg.GPG()
    with open(SECRET_FILE, "rb") as f:
        decrypted_data = gpg.decrypt_file(f, passphrase=PASSPHRASE)
    
    if decrypted_data.ok:
        print("=== ISI RAHASIA PEMILIK ===")
        print(str(decrypted_data))
        print("============================")
    else:
        print("Gagal mendekripsi. Passphrase salah atau file rusak.")
        print("Status:", decrypted_data.status)

if __name__ == "__main__":
    decrypt()
