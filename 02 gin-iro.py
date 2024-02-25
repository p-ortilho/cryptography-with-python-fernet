from cryptography.fernet import Fernet

with open('key.txt', 'rb') as keyFile:
    key = keyFile.read()

f = Fernet(key)

with open('message-encrypting.txt', 'rb') as encryptingFile:
    encryptingMessages = encryptingFile.read()

decryptingMessages = f.decrypt(encryptingMessages)

with open('message-decrypting.txt', 'wb') as decryptingFile:
    decryptingFile.write(decryptingMessages)