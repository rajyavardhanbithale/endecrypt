# Endecrypt
A simple python library for encryption and decryption . Library contain more than 12 (version 1.0) including ciphers and various other cryptography 

### Feature
- Easy to use
- Simple 3 - 4 line code required to convert text to encryption
- Input also accepted
- More feature added Later

------------


### Installation
For **Windows**  and **MAC** User

`pip install endecrypt`
 			**OR**

`python -m pip install endecrypt`

For **Linux** User
`pip3 install endecrypt`

###Ussage
```python
import endecrypt

text = "Hello World 123"
convert_to =  'binary'

endecrypt.encode(text , convert_to)     #User Binary Encryption
output - "1001000 1100101 1101100 1101100 1101111 100000 1010111 1101111 1110010 1101100 1100100"

converted_text = "1001000 1100101 1101100 1101100 1101111 100000 1010111 1101111 1110010 1101100 1100100"
endecrypt.decode(converted_text , convert_to )   #Decrypting Binary
 
```
