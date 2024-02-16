import sys

def implementCaesarCipher(message, key, decrypt=False):
	result = ""
	for character in message:
		if character.isalpha():
			shift = key if not decrypt else -key
			if character.islower():
				result +=chr(((ord(character)-ord("a")+shift)% 26)+ord("a"))
			else:
				result +=chr(((ord(character)-ord("A")+shift)% 26)+ord ("A"))
		else: 
			result += character
	return result 
	
textToEncrypt = input("Please Enter your text/message to encrypt: ")
key = int(input("Please specify the shift length [Enter between 1 and 25]: "))

f = open("secret.enc", "w")
f.write(implementCaesarCipher(textToEncrypt, key))
f.close

print("Your message has been encrypted. \n")
