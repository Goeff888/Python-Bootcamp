import hashlib

with open ("dictionary.txt") as file:
    for line in file:
        word = line.strip()
        hashlib.md5(word.encode()).hexdigest() 
        break
    
        
