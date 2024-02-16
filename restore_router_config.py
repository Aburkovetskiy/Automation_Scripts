from netmiko import ConnectHandler

#Create device object using a dictionary
R2 = {
'device_type' : 'cisco_ios',
'ip' : '192.168.1.2',
'username' : 'admin',
'password' : 'pass123',
'secret' : 'pass123'
	}

#new code 1
backup_file = input("Enter the name of the backup file to restore: ")
with open(backup_file, 'r') as file:
	backup_config = file.read()

#establish SSH connection
net_connect = ConnectHandler(**R2)

#new code 2
net_connect.enable()
net_connect.config_mode()

output = net_connect.send_command_timing(backup_config)

print("Configuration restored")

net_connect.exit_config_mode()

#Close Connection
net_connect.disconnect()
