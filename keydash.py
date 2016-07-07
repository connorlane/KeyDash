from Crypto.PublicKey import RSA
import os.path
from collections import namedtuple

AuthorizedKeyFile = os.path.expanduser("~/.ssh/authorized_keys")

KeyType = namedtuple('Key', ['KeyObj', 'Identifier'] )
def GetAuthorizedKeyList(file):
    AuthorizedKeyList = []
    with open(AuthorizedKeyFile, 'r') as file:
        for line in file:
            key = RSA.importKey(line)
            AuthorizedKeyList.append(KeyType(key, line.split()[-1]))

    return AuthorizedKeyList

def SetAuthorizedKeyList(keyList, file):
    backupFilePath = file + ".old"
    if os.path.exists(backupFilePath):
        os.remove(backupFilePath)
    os.rename(file, backupFilePath)
    with open(file, 'w') as authorizedKeyFile:
        for key in keyList:
            authorizedKeyFile.write(key.KeyObj.exportKey('OpenSSH'))
            authorizedKeyFile.write(" ")
            authorizedKeyFile.write(key.Identifier)
            authorizedKeyFile.write('\n')
 
