import json
import getpass
import hashlib

PASSWORDS_FILE = 'passwords.json'

def get_master_password():
    return getpass.getpass('Enter master password: ')

def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

def load_passwords():
    try:
        with open(PASSWORDS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_passwords(passwords):
    with open(PASSWORDS_FILE, 'w') as file:
        json.dump(passwords, file)

def add_password(passwords):
    website = input('Enter website: ')
    username = input('Enter username: ')
    password = getpass.getpass('Enter password: ')
    hashed_password = hash_password(password)

    passwords[website] = {
        'username': username,
        'password': hashed_password
    }

    save_passwords(passwords)
    print('Password added successfully.')

def get_password(passwords):
    website = input('Enter website: ')

    if website in passwords:
        print(f"Website: {website}")
        print(f"Username: {passwords[website]['username']}")
        print(f"Password: {passwords[website]['password']}")
    else:
        print('Password not found.')

def list_passwords(passwords):
    if passwords:
        print('Stored Passwords:')
        for website in passwords:
            print(f"Website: {website}")
            print(f"Username: {passwords[website]['username']}")
            print(f"Password: {passwords[website]['password']}")
            print('------------------')
    else:
        print('No passwords stored.')

def delete_password(passwords):
    website = input('Enter website: ')

    if website in passwords:
        del passwords[website]
        save_passwords(passwords)
        print('Password deleted successfully.')
    else:
        print('Password not found.')

def main():
    print('Welcome to the Password Manager!')

    master_password = get_master_password()
    hashed_master_password = hash_password(master_password)

    passwords = load_passwords()

    # Check if the entered master password matches the stored hashed password
    if 'master_password' not in passwords:
        passwords['master_password'] = hashed_master_password
        save_passwords(passwords)
        print('Master password set successfully.')
    elif passwords['master_password'] != hashed_master_password:
        print('Incorrect master password. Exiting.')
        return

    while True:
        print('\nMenu:')
        print('1. Add password')
        print('2. Get password')
        print('3. List passwords')
        print('4. Delete password')
        print('5. Exit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            add_password(passwords)
        elif choice == '2':
            get_password(passwords)
        elif choice == '3':
            list_passwords(passwords)
        elif choice == '4':
            delete_password(passwords)
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
