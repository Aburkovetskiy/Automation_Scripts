import string
import random

def generate_password(length):
	characters = string.ascii_letters + string.digits
	password = ''.join(random.choice(characters)for _ in range(length))
	return password
	
def save_passwords_to_file(passwords, filename):
	with open(filename, "w") as file:
		for password in passwords:
			file.write(password + '\n')
			
password_length = (int(input("Enter the length of the password: ")))
num_passwords = int(input("Enter the number of passwords to create: "))
output_file = input("Enter the filename to save the passwords in: ")

passwords = []

for _ in range(num_passwords):
	password = generate_password(password_length)
	passwords.append(password)
	
save_passwords_to_file(passwords, output_file)
print(f"{num_passwords}password of length {password_length} saved to {output_file}")

	
