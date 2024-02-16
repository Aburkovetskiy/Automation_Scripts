import subprocess

def delete_user(username, password):
	subprocess.run(['sudo','userdel','-r',username])
	
def process_users_file(users_file_path):
	with open(users_file_path, 'r') as file:
		for line in file:
			username, password = line.strip().split(':')
			delete_user(username, password)
			
local_users_file_path = '/home/student/Programs/users.txt'
process_users_file(local_users_file_path)
	
