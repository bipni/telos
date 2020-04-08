import os
import re
import platform

class GPUInformation:

    @staticmethod
    def get_gpu():
        operating_system = platform.system()

        if operating_system.lower() == 'linux':
            cards = []
            format_cards = []
            devices = []
            value = []

            os.chdir('/dev/dri')

            list_of_drivers = os.popen('ls -l').read()
            drivers = list_of_drivers.split('\n')

            for driver in drivers:
                cards.append(driver)
            
            for card in cards:
                format_cards.append(re.sub(' +', ' ', card))

            for format_card in range(len(format_cards)):
                devices.append(format_cards[format_card].split(' '))

            for device in range(len(devices)):
                if devices[device][len(devices[device]) - 1][:len(devices[device][len(devices[device]) - 1])-1] == 'card':
                    if (devices[device][len(devices[device]) - 1][0]) == 'c':
                        c = 'char'
                    else:
                        c = 'block'
                    
                    s = 'readlink ' + '/sys/dev/' + c + '/' + devices[device][4][:len(devices[device][4]) - 1] + '\\' + ':' + devices[device][5] + '/device/driver'
                    addr = '/dev/dri/' + devices[device][len(devices[device]) - 1]

                    gAddr = os.popen(s).read()
                    gpuType = gAddr.split('/')

                    if gpuType[len(gpuType)-1] == 'amdgpu\n':
                        gpuName = 'AMD'
                        flag = True
                    elif gpuType[len(gpuType)-1][0:1] == 'i':
                        gpuName = 'Intel'
                        flag = True
                    else:
                        gpuName = 'NVIDIA'
                        flag = False
                    value.append([addr, gpuName, flag])

            return value

def run():
    return GPUInformation.get_gpu()