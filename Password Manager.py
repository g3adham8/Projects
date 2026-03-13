import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes




def get_valid_key(master_pwd):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(master_pwd.encode())
    return base64.urlsafe_b64encode(digest.finalize())


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    try:
        file = open("key.key", "rb")
        key = file.read()
        file.close()
        return key
    except FileNotFoundError:
        return b""


main_pwd = input("what is your master password? ")

 Fernet
combined_key = get_valid_key(load_key().decode() + main_pwd)
fer = Fernet(combined_key)


def view():
    try:
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                if "|" not in data:
                    continue
                user, passw = data.split("|")
              
                decrypted_pwd = fer.decrypt(passw.encode()).decode()
                print(f"user => {user} , password => {decrypted_pwd}")
    except Exception as e:
        print("Error: Could not read file or master password is incorrect!")


def add():
    pn = input("Enter your Account name : ").strip()
    pwd = input("Enter your Password : ").strip().lower()
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open('password.txt', 'a') as f:
        f.write(f"{pn}|{encrypted_pwd}\n")


while True:
    mode = input(
        "\nwould you like to add new password or view the existing ones? (add / view / q ): ").strip().lower()
    if mode == 'q':
        break
    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print("invalid word!")
        continue

