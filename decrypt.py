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
			
	
def crackCaesarCipher(ciphertext):
	for key in range(26):
		decryptedText = implementCaesarCipher(ciphertext, key, decrypt=True)
		print(f"Key {key}: {decryptedText}")
		
while True:
	encryptedText = input("Please Enter the name of the file to be decrypted or press Enter to Quit:")
	if not encryptedText:
		print(f"Thank you. Happy Hacking.")
		break
	else:
		with open(encryptedText, "r") as f:
			ciphertext = f.read()
			
		crackCaesarCipher(ciphertext)
			
	
		
