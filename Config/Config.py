##
## EPITECH PROJECT, 2020
## ChromePasswords
## File description:
## Config
##

import os

GoogleChrome = {
    'env' : os.getenv('LOCALAPPDATA'),
    'LoginData' : '\\Google\\Chrome\\User Data\\Default\\Login Data',
    'LocalState' : r'%LocalAppData%\Google\Chrome\User Data\Local State',
}