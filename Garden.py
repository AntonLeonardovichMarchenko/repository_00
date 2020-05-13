# this is os_info

# сбор информации об операционной системе и версии python

# TODO запустить ЭТОТ скрипт и закомитить результат его работы (в файле os_info.txt)

import platform
import sys


info = f"OS info is \n {platform.uname()}\n\n python version is {sys.version} {platform.architecture()}"

print(info)

with open('os_info.txt', 'w') as ff:
    ff.write(info)


