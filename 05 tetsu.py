from cryptography.fernet import Fernet, MultiFernet

listKeyFernets = []

with open('multKey.txt', 'rb') as fileMultKey:
    keys = fileMultKey.readlines()

for key in keys:
    fkey = Fernet(key.strip())
    listKeyFernets.append(fkey)

with open('message-mult-encrypting.txt', 'rb') as encryptingFile:
    encryptingMessages = encryptingFile.read()

decryptingMessages = MultiFernet(listKeyFernets).decrypt(encryptingMessages)

with open('message-mult-decrypting.txt', 'wb') as decryptingFile:
    decryptingFile.write(decryptingMessages)