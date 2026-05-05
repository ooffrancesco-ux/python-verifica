import random
        
print(ord("A"))

inputUtente = input("Scrivere \"semplice\" per generare password semplice o \"complicato\" per generare password complessa  ")
while(inputUtente != "semplice" and inputUtente != "complicato" ):
    inputUtente = input("Errore: scrivere \"semplice\" per generare password semplice o \"complicato\" per generare password complessa  ")

password=""
if (inputUtente == "semplice"):
    for i in range(8):
        
        while(True):
            carattere = chr(random.randint(0,2**7))
            if( (ord("A") <= ord(carattere) and ord(carattere) <= ord("Z")) or (ord("a") <= ord(carattere) and ord(carattere) <= ord("z")) or (ord("0") <= ord(carattere) and ord(carattere) <= ord("9")) ):
                password = password + carattere
                break



else:
    for i in range(20):
        password = password  + chr(random.randint(0,2**7))
print(password)