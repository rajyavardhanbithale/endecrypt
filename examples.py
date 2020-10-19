
import random
import endecrypt
from endecrypt import cipher


print("\n")
print("1.) binary")
print("\n")
endecrypt.encode("Hello World 123", 'binary')
endecrypt.decode("1001000 1100101 1101100 1101100 1101111 100000 1010111 1101111 1110010 1101100 1100100", 'binary')

print("\n")
print("2.) flipped")
print("\n")
endecrypt.encode("Hello World 123", 'flipped')
endecrypt.decode("dlroW olleH", 'flipped')

print("\n")
print("3.) Base64")
print("\n")
endecrypt.encode("Hello World", 'base64token')
endecrypt.decode("SGVsbG8gV29ybGQ=", 'base64token')

print("\n")
print("4.) Morse_Code")
print("\n")
endecrypt.encode("hello world",'morse')
endecrypt.decode(".... . .-.. .-.. ---  .---- ..--- ...--", 'morse')


#################################################

print("\n\n Class Ciphers")

print("\n")
print("5.) ROT13")
print("\n")
cipher.encode("Hello World", 'rot13conversion')
cipher.decode("Uryyb Jbeyq", 'rot13conversion')


print("\n")
print("6.) caeser")
print("\n")
cipher.encode("Hello World 123", 'caeserconversion',7)
cipher.decode("OLSSV DVYSK", 'caeserconversion',7)


print("\n")
print("7.) affine")
print("\n")
cipher.encode("Hello World 123", 'affine',7,25)
cipher.decode("WBYYTXTOYU", 'affine',7,25)


print("\n")
print("8.) bacon")
print("\n")
cipher.encode("Hello World", 'bacon')
cipher.decode("aabbbaabaaababbababbabbba", 'bacon')


print("\n")
print("9.) a1z26")
print("\n")
cipher.encode("Hello World", 'a1z26')
cipher.decode("8 5 12 12 15  23 15 18 12 4", 'a1z26')


print("\n")
print("10.) vigener")
print("\n")
cipher.encode("Hello World 132", 'vigener','abcd')
cipher.decode("HFNOO XQULE", 'vigener','abcd')


print("\n")
print("11.) railfence")
print("\n")
cipher.encode("Hello World 123", 'railfence',3)
cipher.decode("Horel ollWd", 'railfence',3)


