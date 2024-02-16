from netmiko import ConnectHandler

#add a device
R2 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.1.2',
        'username': 'admin',
        'password' : 'pass123',
        'secret' : 'cisco'
        }
# Next establish the SSH connection
net_connect = ConnectHandler(**R2)
net_connect.enable()
cfg = net_connect.send_config_set(["hostname Router2"])

# Send the command and print the output
verify = net_connect.send_command('show running-config | i hostname')
print(verify)

config_commands = [
        'int FastEthernet0/1',
        'ip add 172.16.1.1 255.255.255.0',
        'description interface for connecting stuff'
        ]
        
sendConfig = net_connect.send_config_set(config_commands)
print('{}\n'.format(sendConfig))

#close connection
net_connect.disconnect()
