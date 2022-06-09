
from cryptography.fernet import Fernet

if __name__ == '__main__':
    # code pour chiffrer un fichier
    key = Fernet.generate_key()
    with open('filekey.key','wb') as filekey:
        filekey.write(key)

    with open('filekey.key','rb') as filek:
        key =filek.read()
    fernet = Fernet(key)
    with open('test_2.pdf', 'rb') as file:
        orignal = file.read()

    encrypted = fernet.encrypt(orignal)
    with open('test_encrypt.pdf','wb') as encrypted_file:
        encrypted_file.write(encrypted)

    # code pour déchiffrer un fichier
    with open('test_encrypt.pdf','rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)
    with open('test_decrypt.pdf','wb') as dec_file:
        dec_file.write(decrypted)