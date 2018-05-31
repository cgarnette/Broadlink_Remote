from broadlink import broadlink
import time
import netaddr
import os

ssid = 'ASUS'
netpass = '180127DB2C'

#Find Bean device and write its info to file
def write_test():
    print('done')
    devices = broadlink.discover(timeout=5)

    if len(devices) > 0:
        print('found it')
        host, mac, devtype = devices[0].get_device_info()
        myBean = broadlink.rm(host, mac, devtype)
        myBean.auth()

        if (not os.path.exists('.//bin')):
                os.makedirs('.//bin')

        with open('.//bin/device_info.txt', 'w+') as device_file:
            device_file.write(str(host[0]) + '\n' + str(host[1]) + '\n' + str(devtype))

        with open('.//bin/device_mac', 'wb+') as device_file:
            device_file.write(mac)
        
#Read Bean info from file and connect to device
def read_test():
    device_info = list()
    with open('.//bin/device_mac', 'rb') as device_file:
        device_info.append(device_file.readline())
    with open('.//bin/device_info.txt', 'r') as device_file:
        for x in device_file.readlines():
            device_info.append(x)
    
    for x in device_info:
        print(x)

    mac = device_info[0]
    host = (str(device_info[1]).strip(), int(str(device_info[2]).strip()))
    devtype = str(device_info[3].strip())

    myBean = broadlink.rm(host, mac, devtype)
    myBean.auth()
    print(myBean)



#write_test()
read_test()