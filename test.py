import os
import subprocess

command = "ls -l"
result = subprocess.run(command.split(' '), stdout=subprocess.PIPE, text=True)

try:
    print(result.stdout)
    print("success")

except:
    print("fail")