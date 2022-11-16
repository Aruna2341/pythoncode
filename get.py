import os, ipaddress

os.system('cls') #os.system will clear at the start of the execution
while True:
    ip = input('enter IP Address:')
    try:
        print(ipaddress.ip_address(ip))
        print('IP valid')
    except:
        print('-' * 50)
        print('IP is not valid')
    finally:
        if ip =='q':
            print('Script Finished')
        break
