import win32api
from time import sleep
import string
import random
from mnemonic import Mnemonic
from termcolor import colored
import os
from bitcoinaddress import Wallet
os.system("")

mnemo = Mnemonic("english")

a=string.ascii_lowercase
b=string.ascii_uppercase
c=string.digits



n=0
stri=""
succ=0
total=0



while True:
    sleep(0.01)
    wallet = Wallet()
    wallet=str(wallet)
    abc=wallet.split(":")

    stri+=(abc[6].split(" ")[1])
    if n == 9803245:
        succ=random.uniform(0.0001, 0.03)
        total+=succ
    print(colored(f"Adress: {stri} | Mnemonic phrase: {mnemo.generate(strength=128)} | BTC: {succ}", "green"))
    stri=""
    win32api.SetConsoleTitle(f"                                                                                         Total verified: {str(n)} | Found BTC: [{total} ~ {int(29000*total)}$]")
    succ=0
    n+=1
    