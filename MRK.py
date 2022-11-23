import os, platform, time
print('Checking Updates...')
time.sleep(2)
os.system('git pull')
os.system('xdg-open https://www.youtube.com/c/MrQureshiTech')
time.sleep(2)
os.system('xdg-open https://www.youtube.com/channel/UCyUzwD8WYuICl5xf4CGZA5w')
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    import MRKs
    MRKs.Mrks()
elif bit == '32bit':
    import MRKs
    MRKs.Mrks()
