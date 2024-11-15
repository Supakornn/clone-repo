import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

def load_key():
    load_dotenv()  
    secret_key = os.getenv("SECRET_KEY")  
    if secret_key is None:
        raise ValueError("SECRET_KEY not found in .env file")
    return secret_key.encode()  

def decrypt_file(filepath, fernet):
    with open(filepath, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(filepath, "wb") as file:
        file.write(decrypted_data)

def decrypt_folder(folder_path, fernet):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            print(f"Decrypting: {filepath}")
            decrypt_file(filepath, fernet)
            print(f"Decrypted: {filepath}")

if __name__ == "__main__":
    key = load_key()
    fernet = Fernet(key)

    decrypt_folder("HACKATHON", fernet)
    decrypt_folder("KMUTT", fernet)
    decrypt_folder("STUPID", fernet)

    print("Decryption process completed.")
