import os, platform, time
print('Checking Updates...')
time.sleep(2)
os.system('https://www.youtube.com/c/MrQureshiTech')
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    import Mrk
    Mrk.riaz()
elif bit == '32bit':
    import Mrk32
    Mrk32.riaz()
