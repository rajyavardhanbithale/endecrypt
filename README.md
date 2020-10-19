# Endecrypt
A simple python library for encryption and decryption . Library contain 10 (version 1.0) including ciphers and various other cryptography 

###### Donate To Programmer [Donate] - 
bc1q9xu6n7cks0gddgqhdp4nqf7je2jetge0ys9sx7knf5653ukpkgmsptykwy

Bitcoin
[![Donate To Programmer](https://i.imgur.com/F23EQ9v.png "Donate To Programmer")](https://i.imgur.com/F23EQ9v.png "Donate To Programmer")

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
In Advance Encryption we can use cipher text this library contain 5 ciphers more added later
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

#### Like my work -
###### Donate To Programmer [Donate] - 
bc1q9xu6n7cks0gddgqhdp4nqf7je2jetge0ys9sx7knf5653ukpkgmsptykwy

Bitcoin 
[![Donate To Programmer](https://i.imgur.com/F23EQ9v.png "Donate To Programmer")](https://i.imgur.com/F23EQ9v.png "Donate To Programmer")
