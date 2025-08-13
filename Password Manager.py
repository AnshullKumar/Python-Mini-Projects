from cryptography.fernet import Fernet #This is used for encryption and decryption


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key(): 
    with open("key.key", "rb") as key_file:
        return key_file.read()

    
#write_key() 
#Run write_key() only once to generate the key and save it to a file
key = load_key() 
fer = Fernet(key)

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        

while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add) Or press q to quit: ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
