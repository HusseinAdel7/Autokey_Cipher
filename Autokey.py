import os.path
from sys import platform
import os 
import string
from termcolor import colored
from Crypto.Cipher import DES3
from Crypto.Util import Counter
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random 
from Crypto.Cipher import DES3


os.system('clear') 

print ("\n\n\t\t\t    ------------------")
print(colored('\t\t\t      Cryptography ', 'yellow'))
print ("\t\t\t    ------------------")
print(colored('\n\t     * Written by : ', 'green'),end="")
print(colored(' Hussein Adel', 'white'),end="")
print ("\n\t\t\t     ------------\n")
print (" ===========================================================================\n")
print (colored('\t\t\t\t  ------------','white'))
print(colored('\t\t\t\t    Hello \U0001f600 ', 'yellow'))
print (colored('\t\t\t\t  ------------\n','white'))

#------------------------------------------------------------------------  
#========================================================================
# Auto Key Cipher 

def autokey_Encryption(string,key):
    if len(key) < len(string):
        key = (key + string)[: len(string)] 
    elif len(key) > len(string):
        key = key[: len(string)]
    enc = ""
    s = 0
    check = ''
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i].isupper():
                check = 'A'
            else:
                check = 'a'
            s = (ord(string[i]) - ord(check) + ord(key[i]) - ord(check)) % 26
            enc += chr(s + ord(check))
        else:
            enc += string[i]
    return enc

def autokey_Decryption(c, k):
    alphabets = "abcdefghijklmnopqrstuvwxyz" # this is the english letters
    p = ""
    keyy = []
    for x in k:
        keyy.append(alphabets.find(x))
    i = 0
    j = 0
    for x in c:
      if i >= len(keyy):
        pos = alphabets.find(x.lower()) - alphabets.find(p[j])
        j += 1
      else:
        pos = alphabets.find(x.lower()) - keyy[i]
      if pos < 0:
          pos = pos + 26
      p += alphabets[pos].lower()
      i +=1
    return p



choose =int(input(colored("\n1- Encryption\n2- Decryption\n\nChoice '1' or '2': ", 'white')))
if choose ==1:
    plain_Text =str(input(colored("\nEnter Your Message That You Wanna encrypt :  " , 'green')))
    secret_Key= input(colored("Enter The Secret key : " , 'green'))
    print(autokey_Encryption(plain_Text,secret_Key))

if choose ==2:
    plain_Text =str(input(colored("\nEnter Your Message That You Wanna decrypt :  " , 'green')))
    secret_Key= input(colored("Enter The Secret key : " , 'green'))
    print(autokey_Decryption(plain_Text,secret_Key))
#---------------------------------------------------------------------------------------
print (colored('\n\n\t\t\t\t  ----------','white'))
print(colored('\t\t\t\t    Done \U0001f600 ', 'yellow'))
print (colored('\t\t\t\t  ----------\n','white'))

