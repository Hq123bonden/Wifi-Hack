#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os
import sys
import time
from subprocess import check_call
from colorama import Fore, Style

#Colores
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'

os.system("clear")

############################################################

def banner():
	print("""
 \033[1;37m❰-----------------------------------------------------------------------❱\033[0m

      \033[0;31m██╗    ██╗██╗███████╗██╗        \033[0;32m██╗  ██╗ █████╗  ██████╗██╗  ██╗\033[0m
      \033[0;31m██║    ██║██║██╔════╝██║        \033[0;32m██║  ██║██╔══██╗██╔════╝██║ ██╔╝\033[0m
      \033[0;31m██║ █╗ ██║██║█████╗  ██║ \033[1;37m█████╗ \033[0;32m███████║███████║██║     █████╔╝\033[0m 
      \033[0;31m██║███╗██║██║██╔══╝  ██║ \033[1;37m╚════╝ \033[0;32m██╔══██║██╔══██║██║     ██╔═██╗ \033[0m
      \033[0;31m╚███╔███╔╝██║██║     ██║        \033[0;32m██║  ██║██║  ██║╚██████╗██║  ██╗\033[0m
       \033[0;31m╚══╝╚══╝ ╚═╝╚═╝     ╚═╝        \033[0;32m╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝\033[0m                                                   
                         \033[1;31m---< \033[1;37mCreador: \033[1;32mR3LI4NT \033[1;31m>---\033[0m 

 \033[1;37m❰-----------------------------------------------------------------------❱\033[0m
""")

def menu():
	print(""" \033[0;31m[\033[1;37m1\033[0;31m] \033[0;32mIniciar el modo monitor
 \033[0;31m[\033[1;37m2\033[0;31m] \033[0;32mDetener el modo monitor
 \033[0;31m[\033[1;37m3\033[0;31m] \033[0;32mVer mi interfaz
 \033[0;31m[\033[1;37m4\033[0;31m] \033[0;32mReiniciar red
 \033[0;31m[\033[1;37m5\033[0;31m] \033[0;32mEscanear redes cercanas
 \033[0;31m[\033[1;37m6\033[0;31m] \033[0;32mCapturar Handshake
 \033[0;31m[\033[1;37m7\033[0;31m] \033[0;32mDescifrar clave
 \033[0;31m[\033[1;37m8\033[0;31m] \033[0;32mAtacar redes WPS (\033[1;32mWifite\033[0;32m)\033[0m
 \033[0;31m[\033[1;37m9\033[0;31m] \033[0;32mFalsificar MAC
 \033[0;31m[\033[1;37m10\033[0;31m] \033[0;32mFake AP
 \033[0;32m[\033[1;37m0\033[0;32m] \033[0;31mSalir\033[0m\n
""")

banner()
menu()



def goodbye():
  print("""
 \033[1;37m------------------------------------------------------\033[0m   
\033[1;34m    _____  ____   ____  _____  ______     ________ _ 
   / ____|/ __ \ / __ \|  __ \|  _ \ \   / /  ____| |
  | |  __| |  | | |  | | |  | | |_) \ \_/ /| |__  | |
  | | |_ | |  | | |  | | |  | |  _ < \   / |  __| | |
  | |__| | |__| | |__| | |__| | |_) | | |  | |____|_|
   \_____|\____/ \____/|_____/|____/  |_|  |______(_)\033[0m

     \033[1;31m<\033[1;37mEl poder del usuario radica en su ANONIMATO\033[1;31m>\033[0m 

 \033[1;37m------------------------------------------------------\033[0m 
                                                   
"""+ WHITE + Style.NORMAL)
