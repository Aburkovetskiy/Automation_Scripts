import subprocess

def create_user(username, password):
	subprocess.run(['sudo','useradd','-m',username])
	subprocess.run(['sudo','chpasswd'],input=f'{username}:{password}'.encode())
	
def process_users_file(users_file_path):
	with open(users_file_path, 'r') as file:
		for line in file:
			username, password = line.strip().split(':')
			create_user(username, password)
			
local_users_file_path = '/home/student/Programs/users.txt'
process_users_file(local_users_file_path)
	
