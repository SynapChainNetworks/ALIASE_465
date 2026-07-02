
import hashlib
import os
from token_manager import load_progress, save_progress

# Konfigurasi default
DEFAULT_TARGET = 1000          # Target token yang harus dikumpulkan (demo)
DIFFICULTY = 4                 # Jumlah leading zero yang dibutuhkan
PASSPHRASE = "TribeV2_465_Masterkey"  # Passphrase untuk decrypt rahasia

# Baca target dari environment variable jika ada
TARGET_TOKENS = int(os.getenv("ALIASE_465_TARGET_TOKENS", DEFAULT_TARGET))

def mine():
    print("=" * 50)
    print(" ALIASE_465 MINING RIG ".center(50, "="))
    print(f"Target token untuk menghentikan: {TARGET_TOKENS:,}")
    print(f"Difficulty: {DIFFICULTY} leading zeros")
    print("=" * 50)
    
    tokens_mined = load_progress()
    print(f"Melanjutkan dari token ke-{tokens_mined}...\n")
    
    nonce = tokens_mined
    prefix_zeros = "0" * DIFFICULTY
    
    try:
        while tokens_mined < TARGET_TOKENS:
            data = f"ALIASE_465_BLOCK_{nonce}".encode()
            hash_result = hashlib.sha256(data).hexdigest()
            
            if hash_result.startswith(prefix_zeros):
                tokens_mined += 1
                save_progress(tokens_mined)
                if tokens_mined % 10 == 0:
                    print(f"[+] Token terkumpul: {tokens_mined}/{TARGET_TOKENS}")
            
            nonce += 1
            
        print(f"\n{'='*50}")
        print(" TARGET TERCAPAI! ALIASE_465 BERHASIL DIMATIKAN (simulasi) ")
        print(f"{'='*50}\n")
        
        if os.path.exists("token_progress.json"):
            os.remove("token_progress.json")
        
        print("Rahasia pemilik telah terbuka...")
        print(f"Passphrase untuk decrypt secrets/rahasia.txt.gpg:\n\n>>> {PASSPHRASE} <<<\n")
        print("Gunakan perintah: gpg --decrypt secrets/rahasia.txt.gpg")
        print("Atau jalankan 'python src/mining_puzzle/decrypt_secret.py'")
        
    except KeyboardInterrupt:
        print("\nMining dihentikan. Progres disimpan.")
        save_progress(tokens_mined)

if __name__ == "__main__":
    mine()
