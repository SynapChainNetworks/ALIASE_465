import gnupg
import getpass

def encrypt_file(input_file, output_file):
    gpg = gnupg.GPG()
    passphrase = getpass.getpass("Masukkan passphrase: ")
    with open(input_file, "rb") as f:
        encrypted_data = gpg.encrypt_file(f, recipients=None, 
                                          symmetric=True, 
                                          passphrase=passphrase, 
                                          output=output_file)
    if encrypted_data.ok:
        print(f"File berhasil dienkripsi menjadi {output_file}")
    else:
        print("Gagal:", encrypted_data.status)

if __name__ == "__main__":
    encrypt_file("rahasia.txt", "secrets/rahasia.txt.gpg")
