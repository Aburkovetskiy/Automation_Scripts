import os
import datetime

remote_host = "192.168.1.10"
remote_user = "student"
remote_directory = "/home/student"
local_backup_directory = "/home/student"

backup_filename = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + "-server_home_bak" + "tar.gz"
backup_filepath = os.path.join(local_backup_directory, backup_filename)

ssh_command = f'ssh {remote_user}@{remote_host} " tar -czvf - {remote_directory}" > {backup_filepath}'

os.system(ssh_command)

print("Backup created successfully:", backup_filepath)
