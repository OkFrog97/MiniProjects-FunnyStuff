import os
import time

source = [r'"C:\Users\User\Desktop\projects"']
target_dir = '"D:\Backup"'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%H%S') + '.zip'
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print ('Copy complite')
else:
    print ('ATTENTION! Copy error')
