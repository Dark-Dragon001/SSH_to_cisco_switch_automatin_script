import subprocess
import sys
from netmiko import ConnectHandler

    # IP address of devices
print("Please type the Ip-address of the device you want to connect from the list below:")
print(" switch1 ip: 10.0.0.248 \n switch2 ip: 10.1.0.248 \n switch3 ip: 10.2.0.248")

# Ask for an input.
userInput = input("Please enter an ip address: ")

def getInfo(deviceIP):
    try:
        # Required information to ssh to a device
        device = {
        'device_type': 'cisco_ios',
        'host':   deviceIP,
        'username': 'testuser',
        'password': 'test2015',
        'port' : 22}

        net_connect = ConnectHandler(**device)

        # Show IP address of the device
        ipInfo = net_connect.send_command('show ip interface brief | section Vlan')

        # Show physical ports that are up
        portInfo = net_connect.send_command('show ip int brief | section up')

        # Shows time and date of the device
        tdInfo = net_connect.send_command('sh clock')

        # Show the device model
        devInfo = net_connect.send_command('sh version | section Model')
        
        # Create a txt file write all the information and closes the file.
        f = open(userInput + " deviceInfo.txt", "w")
        f.write("Device IP address: " + ipInfo + "\n" + "---------------------------------------------------------------------------------------------------\n"
        + "Port status that are up: " + portInfo + "\n" + "---------------------------------------------------------------------------------------------------\n"
        + "Time and date info: " + tdInfo + "\n" + "---------------------------------------------------------------------------------------------------\n"
        + "Device Model info:" + devInfo)
        f.close()
        print("Successfully done, look for the txt file in the directory of the script!")
    except:
        sys.exit("Something went wrong, please try again!")


getInfo(userInput)
