import os
import datetime

remote_host = "192.168.1.10"
remote_user = "student"
remote_directory = "/home/student"
local_backup_directory = "/home/student"

backup_filename = input("Enter the backup file name : ")
backup_filepath = os.path.join(local_backup_directory, backup_filename)

scp_command = f'scp {backup_filepath} {remote_user}@{remote_host}:{remote_directory}/{backup_filename}'
os.system(scp_command)

ssh_command = f'ssh {remote_user}@{remote_host} " tar -xzvf {backup_filepath} -C /" '

os.system(ssh_command)

print("Backup restored successfully:")


