from netmiko import ConnectHandler

#create a device using dictionary
R1 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.1.1',
        'username': 'admin',
        'password' : 'pass123',
        'secret' : 'cisco'
        }
R2 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.1.2',
        'username': 'admin',
        'password' : 'pass123',
        'secret' : 'cisco'
        }      
# Next establish the SSH connection
net_connect = ConnectHandler(**R1)
net_connect.enable()
cfg = net_connect.send_config_set(["hostname Router1"])

# Send the command and print the output
verify = net_connect.send_command('show running-config | i hostname')
print(verify)

config_commands = [
        'int loopback 1',
        'ip add 10.1.1.1 255.255.255.0',
        'description aburkovetskiy loopback'
        ]

sendConfig = net_connect.send_config_set(config_commands)
print('{}\n'.format(sendConfig))


#close connection
net_connect.disconnect()

net_connect = ConnectHandler(**R2)
net_connect.enable()

config_commands = [
        'int loopback 1',
        'ip add 10.1.1.2 255.255.255.0',
        'description aburkovetskiy loopback on R2'
        ]

sendConfig = net_connect.send_config_set(config_commands)
print('{}\n'.format(sendConfig))

#close connection
net_connect.disconnect()


