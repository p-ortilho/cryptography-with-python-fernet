from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('key.txt', 'wb') as fileKey:
    fileKey.write(key)

with open('message.txt', 'rb') as fileMessage:
    file = fileMessage.read()

f = Fernet(key)

encryptingMessages = f.encrypt(file)

with open('message-encrypting.txt', 'wb') as encryptingFile:
    encryptingFile.write(encryptingMessages)