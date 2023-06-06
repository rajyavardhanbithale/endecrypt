# Endecrypt
A simple Python library for encryption and decryption, the library contains 10 ciphers and various other cryptography.

*Under Development - Bugs*

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

## Usage
#### Simple Encryption
```python
import endecrypt

#Encryption
message_1 = "hello world"         #Use Small Word
encryption = 'morse'

endecrypt.encode(message_1 ,encryption)
# >> .... . .-.. .-.. ---  .-- --- .-. .-.. -..

#Decryption
message_2 = ".... . .-.. .-.. ---  .-- --- .-. .-.. -.."     # Don't leave space  
decryption = 'morse'

endecrypt.decode(message_2 , decryption)
# >> hello world
```
## Advance Encryption
Advance Encryption, You can use a cipher library that contains five ciphers.
```python
from endecrypt import cipher

# Encryption
message_1 = "Hello World"
encryption = 'affine'        #We Can Use Anything As Variable ex - y = 'affine' 
slop_1 =7
slop_2 = 25

cipher.encode(message_1, encryption , slop_1 , slop_2)
# >> WBYYTXTOYU

#Decryption
message_2 = "WBYYTXTOYU"
decryption = 'affine'          #We Can Use Anything As Variable ex - y = 'affine' 
slop_1 =7
slop_2 = 25

cipher.decode(message_2 , decryption , slop_1 , slop_2)
# >> Hello World
```

###### For More Sample Run examples.py



