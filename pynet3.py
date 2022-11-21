from netmiko import ConnectHandler
with open('devices.txt') as routers:
    for IP in routers:
	    Routers = {
		    "device_type": "Cisco_ios",
			"ip": "sandbox-iosxe-latest-l.Cisco.com",
			"username": "developer",
			"password": "Cisco12345"
        }
net_connect=ConnectHandler(**Router)
		
		print('Connecting to' + IP)
		print('-'*79)
        output=net_connect.send_command('sh ip int brief')
		print(output)
		print()
		print('-'*79)
net_connect.disconnect()