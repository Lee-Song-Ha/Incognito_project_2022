import os
import subprocess

command = "echo #PATH"
result = subprocess.run(command.split(' '), stdout=subprocess.PIPE, text=True)

try:
    if '.' in result:
        result.remove('.')

    for i in range (len(result)):
          print(result[i],end="")
   
    print("success")

except:
    print("fail")