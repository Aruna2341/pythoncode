from netmiko import ConnectHandler
 
#First create the device object using a dictionary
with
Router = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port":"22"
}
 
# Next establish the SSH connection
net_connect = ConnectHandler(**CSR)
 
# Then send the command and print the output

output_runconfig = net_connect.send_command('show run')
print (output_runconfig)
 
# Finally close the connection
net_connect.disconnect()

