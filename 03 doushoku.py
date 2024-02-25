from cryptography.fernet import Fernet, MultiFernet

keyOne = Fernet.generate_key()
keyTwo = Fernet.generate_key()

with open('multKey.txt', 'ab') as multKeyFile:
    multKeyFile.write(keyOne + b'\n')
    multKeyFile.write(keyTwo + b'\n')

f = MultiFernet([Fernet(keyOne), Fernet(keyTwo)])

with open('message.txt', 'rb') as fileMessage:
    file = fileMessage.read()

encryptingMessages = f.encrypt(file)

with open('message-mult-encrypting.txt', 'wb') as encryptingFile:
    encryptingFile.write(encryptingMessages)