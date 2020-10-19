import os
try:
	import string
except:
	print("Fatal Error String Not Found")
import encDict
import sys
try:
	import base64
except:
	print("Fatal Error Base64 Not Found")		





'''
dictionary is imported form encDeict.py
'''

dict1 = encDict.dict1 
dict2 = encDict.dict2
dict3 = encDict.dict3
dict4 = encDict.dict4
dict5 = encDict.dict5  
dict6 = encDict.dict6
dict7 = encDict.dict7

'''
Data spiritual rebirth have always been widely used utility and one 
among them can be conversion of a string to it’s binary equivalent. 
Let’s discuss certain ways in which this can be done.

encodeion is the strategy by which data is changed over into mystery
code that shrouds the data's actual importance. The study of encoding
and decoding data is called cryptography. In processing, decode1d
information is otherwise called plaintext, and encoded information 
is called ciphertext.
'''
#Keywords

def encode(argv,opti):
	#binary
	if opti == "binary":
		txt_to_bin_converted = ' '.join(format(ord(i), 'b') for i in argv)
		print(txt_to_bin_converted)

	#flipped
	elif opti == "flipped":
		def process_encode(argv):
			return argv[::-1]
		processedtext = process_encode(argv)
		print (processedtext)

	#base64
	elif opti == "base64token":
		message_bytes = argv.encode('ascii')
		base64_bytes = base64.b64encode(message_bytes)
		base64_message = base64_bytes.decode('ascii')
		print(base64_message)


	#ROT13
	elif opti == "rot13conversion":
		def encode(strEnc):
			return strEnc.translate(str.maketrans(dict1, dict2))
		print(encode(str(argv)))

	elif opti == "morse":
		def encode(argv1): 
			cipher = '' 
			for letter in argv1: 
				if letter != ' ': 
					cipher += dict3[letter] + ' '
				else:
					cipher += ' '
			return cipher
		argv1 = argv
		result = encode(argv1) 
		print (result) 
		
#decodedecodedecodedecodedecodedecodedecodedecodedecodedecodedecodedecode

def decode(argv,opti):

	#binary
	if opti =="binary":
		bin_string = argv
		binary_values = bin_string.split()
		ascii_string = ""
		for binary_value in binary_values:
			integers = int(binary_value, 2)
			ascii_char = chr(integers)
			ascii_string += ascii_char

		print(ascii_string)

	#flipped
	elif opti == "flipped":
		def process_decode1(arg):
			return arg[::-1]
		processedtextdecode1 = process_decode1(argv)
		print (processedtextdecode1)

	#base64
	elif opti == "base64token":
		base64_bytes = argv.encode('ascii')
		message_bytes = base64.b64decode(base64_bytes)
		base64_message = message_bytes.decode('ascii')
		print(base64_message)

	#Morse Code
	elif opti == "morse":
		def decode1(argv1): 
			argv1 += ' '
			decipher = '' 
			citext = '' 
			for letter in argv1: 
				if (letter != ' '): 
					i = 0
					citext += letter
				else:
					i += 1
					if i == 2 :
						decipher += ' '
					else:
						decipher += list(dict3.keys())[list(dict3 .values()).index(citext)]
						citext = ''
			return decipher 

		argv1 = argv
		result = decode1(argv1) 
		print (result) 




class cipher():
	def encode(argv,opti,shifta=0,shiftb=0):
		#ROT13
		if opti == "rot13conversion":
			def decode1(strEnc):
				
				return strEnc.translate(str.maketrans(dict2, dict1))

			if shifta or shiftb != 0:
				raise ValueError ("rot13 doesn't require any third and fourth value")
				sys.exit()
			print(decode1(str(argv)))


		elif opti == "caeserconversion":

			if shifta ==0 :
				raise ValueError ("caeser cipher require third value as shift")
				sys.exit()

			if shiftb != 0:
				raise ValueError ("caeser cipher doesn't require any fourth value because it satisfy with third shifts ")
				sys.exit()

			shifts = shifta
			arvg1 = argv
			cipherstring = "" 
			for c in arvg1.upper():
				if c.isalpha(): 
					cipherstring+= dict5[ (dict4[c] + shifts)%26 ]
				else: 
					cipherstring += c
			print (cipherstring)


		elif opti == "affine":
			def egcd(a, b): 
				x,y, u,v = 0,1, 1,0
				while a != 0: 
					q, r = b//a, b%a 
					m, n = x-u*q, y-v*q 
					b,a, x,y, u,v = a,r, u,v, m,n 
					gcd = b 
				return gcd, x, y 
			

			def modinv(a, m): 
				gcd, x, y = egcd(a, m) 
				if gcd != 1:
					return None  
				else:
					return x % m 

			def encode(text, key): 
				 
				return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '')])

			if shifta ==0:
				raise ValueError("Error: you need to assigined third and fourth value try this .cipher('Any Tex',affine,1,1)")

			if shiftb ==0:
				raise ValueError ("Error: you need to assigined the fourth value\n try this .cipher('Any Tex',affine,1,1)")
				sys.exit()

			text = argv
			key = [shifta , shiftb] 
			enc_text = encode(text, key) 
			print(format(enc_text))

		elif opti == "bacon":
			def encode(message): 
			    cipher = '' 
			    for letter in message: 
			       
			        if(letter != ' '):           
			            cipher += dict6[letter] 
			        else: 
			            cipher += ' '

			    return cipher
			message = argv
			result = encode(message.upper())
			print (result)


		elif opti == "a1z26":
			def encode(argv): 
				cipher = '' 
				for letter in argv1: 
					if letter != ' ': 
						cipher += dict7[letter] + ' '
					else:
						cipher += ' '
				return cipher
			argv1 = argv
			result = encode(argv1) 
			print (result)

		elif opti == "vigener":
			def msg_and_key(key1=shifta):
				key1 = shifta
				msg = argv.upper()
				key = key1.upper()
				key_map = ""
				j=0
				for i in range(len(msg)):
					if ord(msg[i]) == 32:
						key_map += " "
					else:
						if j < len(key):
							key_map += key[j]
							j += 1
						else:
							j = 0
							key_map += key[j]
							j += 1
				return msg, key_map


			def create_vigenere_table():
				table = []
				for i in range(26):
					table.append([])

				for row in range(26):
					for column in range(26):
						if (row + 65) + column > 90:
							table[row].append(chr((row+65) + column - 26))
						else:
							table[row].append(chr((row+65)+column))
				return table



			def cipher_encodeion(message, mapped_key):
				table = create_vigenere_table()
				encodeed_text = ""
				for i in range(len(message)):
					if message[i] == chr(32):
						encodeed_text += " "
					else:
						row = ord(message[i])-65
						column = ord(mapped_key[i]) - 65
						encodeed_text += table[row][column]
				print(encodeed_text)


			message, mapped_key = msg_and_key()
			cipher_encodeion(message, mapped_key) 

		elif opti == "railfence":
			def encodeRailFence(text, key): 

			    rail = [['\n' for i in range(len(text))] 
			                  for j in range(key)] 
			      
			    dir_down = False
			    row, col = 0, 0
			      
			    for i in range(len(text)): 

			        if (row == 0) or (row == key - 1): 
			            dir_down = not dir_down 
			          
			        rail[row][col] = text[i] 
			        col += 1
			          
			        if dir_down: 
			            row += 1
			        else: 
			            row -= 1

			    result = [] 
			    for i in range(key): 
			        for j in range(len(text)): 
			            if rail[i][j] != '\n': 
			                result.append(rail[i][j]) 
			    return("" . join(result))

			text = argv
			key = shifta
			print(encodeRailFence(argv, shifta))    			 

		

	def decode(argv,opti,shifta=0,shiftb=0):
		#ROT13
		if opti == "rot13conversion":
			def decode1(strEnc):
				return strEnc.translate(str.maketrans(dict2, dict1))

			if shifta or shiftb != 0:
				raise ValueError ("rot13 doesn't require any third and fourth value")
				sys.exit()
			print(decode1(str(argv)))


		elif opti == "caeserconversion":
			if shiftb != 0:
				raise ValueError ("caeser cipher doesn't require any fourth value")
				sys.exit()
			cipherstring = argv
			shifts = shifta
			arvg1 = argv
			decipherstring = ""
			for c in cipherstring.upper():
				if c.isalpha(): 
					decipherstring += dict5[ (dict4[c] - shifts)%26 ]
				else: 
					decipherstring += c
			print (decipherstring)


		elif opti == "affine":
			def egcd(a, b): 
				x,y, u,v = 0,1, 1,0
				while a != 0: 
					q, r = b//a, b%a 
					m, n = x-u*q, y-v*q 
					b,a, x,y, u,v = a,r, u,v, m,n 
					gcd = b 
				return gcd, x, y 
			

			def modinv(a, m): 
				gcd, x, y = egcd(a, m) 
				if gcd != 1:
					return None # modular inverse does not exist 
				else:
					return x % m 

			def decode(cipher, key): 
				return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ]) 

			text = argv


			if shifta ==0:
				raise Exception("Error: you need to assigined third and fourth value try this .cipher('Any Tex',affine,1,1)")
			if shiftb ==0:
				raise ValueError ("Error: you need to assigined the fourth value try this .cipher('Any Tex',affine,1,1)")
				sys.exit()
		
			key = [shifta, shiftb] 
			enc_text = decode(text, key) 
			print(format(enc_text)) 

			
		elif opti == "bacon":
			def decode1(message): 
			    decipher = '' 
			    i = 0
			    while True : 
			        if(i < len(message)-4): 
			            substr = message[i:i + 5] 
			            if(substr[0] != ' '): 
			                decipher += list(dict6.keys())[list(dict6.values()).index(substr)] 
			                i += 5

			            else:
			                decipher += ' '
			                i += 1 
			        else: 
			            break 

			    return decipher 


			message = "aabbbaabaaababbababbabbba babbaabbbabaaabababbaaabb"
			result = decode1(message.lower()) 
			print (result)


		elif opti == "a1z26":
			def decode1(argv1): 
				argv1 += ' '
				decipher = '' 
				citext = '' 
				for letter in argv1: 
					if (letter != ' '): 
						i = 0
						citext += letter
					else:
						i += 1
						if i == 2 :
							decipher += ' '
						else:
							decipher += list(dict7.keys())[list(dict7 .values()).index(citext)]
							citext = ''
				return decipher 

			argv1 = argv
			result = decode1(argv1) 
			print (result)  


		elif opti == "vigener":
			def msg_and_key(key1=shifta):
				key1 = shifta
				msg = argv.upper()
				key = key1.upper()
				key_map = ""
				j=0
				for i in range(len(msg)):
					if ord(msg[i]) == 32:
						key_map += " "
					else:
						if j < len(key):
							key_map += key[j]
							j += 1
						else:
							j = 0
							key_map += key[j]
							j += 1
				return msg, key_map


			def create_vigenere_table():
				table = []
				for i in range(26):
					table.append([])

				for row in range(26):
					for column in range(26):
						if (row + 65) + column > 90:
							table[row].append(chr((row+65) + column - 26))
						else:
							table[row].append(chr((row+65)+column))
				return table

			def itr_count(mapped_key, message):
				counter = 0 
				result = ""
				for i in range(26):
					if mapped_key + i > 90:
						result += chr(mapped_key+(i-26))
					else:
						result += chr(mapped_key+i)

				for i in range(len(result)):
					if result[i] == chr(message):
						break
					else:
						counter += 1
				return counter				


			def cipher_decodeion(message, mapped_key):
				table = create_vigenere_table()
				decodeed_text = ""
				for i in range(len(message)):
					if message[i] == chr(32):
						decodeed_text += " "
					else:
						decodeed_text += chr(65 + itr_count(ord(mapped_key[i]), ord(message[i])))
				print(decodeed_text)


			message, mapped_key = msg_and_key()
			cipher_decodeion(message, mapped_key)	

		elif opti == "railfence":
			def decodeRailFence(cipher, key): 
			   
			    rail = [['\n' for i in range(len(cipher))]  
			                  for j in range(key)] 
			      
			    dir_down = None
			    row, col = 0, 0
			       
			    for i in range(len(cipher)): 
			        if row == 0: 
			            dir_down = True
			        if row == key - 1: 
			            dir_down = False
			          
			        # place the marker 
			        rail[row][col] = '*'
			        col += 1
			  
			        if dir_down: 
			            row += 1
			        else: 
			            row -= 1

			    index = 0
			    for i in range(key): 
			        for j in range(len(cipher)): 
			            if ((rail[i][j] == '*') and
			               (index < len(cipher))): 
			                rail[i][j] = cipher[index] 
			                index += 1
			          
			    result = [] 
			    row, col = 0, 0
			    for i in range(len(cipher)):            
			        if row == 0: 
			            dir_down = True
			        if row == key-1: 
			            dir_down = False              
			 
			        if (rail[row][col] != '*'): 
			            result.append(rail[row][col]) 
			            col += 1

			        if dir_down: 
			            row += 1
			        else: 
			            row -= 1
			    return("".join(result)) 

			cipher = argv
			key = shifta

			print(decodeRailFence(cipher, key)) 
	  





						

