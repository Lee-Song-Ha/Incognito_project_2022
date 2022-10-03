# /etc/passwd 파일의 퍼미션과 소유자를 확인
# /etc/passwd 파일의 소유자 및 권한 변경 (소유자 root, 권한 644)

import os

command = "echo $PATH"
stream = os.popen(command)
result = stream.read()

try:
    print(result)
    print("success")

except:
    print("fail")