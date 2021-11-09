import os
import subprocess

root = "D:"
dirlist = [item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item))]
print(dirlist)
for i in dirlist:
    try:
        if i == 'donttouch':
            'не трогать!'
            continue
        elif os.path.isdir(fr"{root}\{i}\venv"):
            subprocess.Popen(["powershell", rf"{root}\{i}\venv\scripts\Activate.ps1"], stdout=subprocess.PIPE)
            subprocess.Popen(
                ["powershell", rf"{root}\{i}\venv\scripts\python.exe -m pip freeze > {root}\{i}\requirements.txt"],
                stdout=subprocess.PIPE)
            subprocess.Popen(["powershell", rf"{root}\{i}\venv\scripts\deactivate.bat"], stdout=subprocess.PIPE)
            subprocess.Popen(["powershell", rf"{root}\{i}\venv\scripts\deactivate"], stdout=subprocess.PIPE)
            subprocess.Popen(["powershell", rf"rm -r {root}\{i}\venv"], stdout=subprocess.PIPE)
            print('Успех')
    except:
        print('Ошибка')
