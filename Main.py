#! /usr/bin/env python3
##
## EPITECH PROJECT, 2020
## ChromePasswords
## File description:
## Main
##

from sys import argv, exit
from Sources.Help import printUsage
from Sources.GetChromePasswords import GetChromePasswords

if __name__ == '__main__':
    if len(argv) == 2 and argv[1] == "-h":
            printUsage()
            exit(0)
    elif len(argv) == 1:
        GetChromePasswords()
        exit(0)
    else:
        exit(1)