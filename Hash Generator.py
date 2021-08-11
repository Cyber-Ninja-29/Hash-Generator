import hashlib
def encrypt(a):
    result = ""
    s = 4
    for i in range(len(a)):
        char = a[i]
        #uppercase , lowercase , digits
        #uppercase 
        # A -> 65 -> 69 -> E
        if char.isupper():
            result += chr((ord(char)+ s -65) %26 +65)
        #lowercase
        elif char.islower():
            result += chr((ord(char)+ s -97) %26 +97)
        elif char.isdigit():
            x = int(char)
            y = x + 4
            result += str(y)
        else:
            result += char
    return result
mystring1 = input("Enter text to hash : ")
hash_obj = hashlib.blake2b(mystring1.encode())
b = hash_obj.hexdigest()
print(b)