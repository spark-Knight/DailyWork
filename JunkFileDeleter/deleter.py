import os
import subprocess
import shutil


del_dir = r'C:\Windows\temp'
pObj = subprocess.Popen('rmdir /S /Q %s' % del_dir, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
# recreate the deleted parent dir in case it get deleted
os.makedirs(os.path.dirname(del_dir), exist_ok=True)
rTup = pObj.communicate()
rCod = pObj.returncode
if rCod == 0:
    print ("Success: Cleaned Windows Temp Folder")
else:
    print ("Fail: Unable to Clean Windows Folder")



# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

del_dir = r'C:\Users\Sid\AppData\Local\Temp'
pObj = subprocess.Popen('rmdir /S /Q %s' % del_dir, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
# recreate the deleted parent dir in case it get deleted
os.makedirs(os.path.dirname(del_dir), exist_ok=True)
rTup = pObj.communicate()
rCod = pObj.returncode
if rCod == 0:
    print ("Success: Cleaned Windows %Temp% Folder")
else:
    print ("Fail: Unable to Clean Windows Folder") 
