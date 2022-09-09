import os
import subprocess

# os.system()
os.system('ls -l')

# os.popen()
stream = os.popen('ls -l')
output = stream.read()
print(output)

# subprocess()
subprocess.run(["ls", "-l"])

# 실행 결과 리턴 받기
result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True)
print(result.stdout)

# 명령어를 하나의 문자열에 입력 및 리스트로 변환
command = "ls -l"
result = subprocess.run(command.split(' '), stdout=subprocess.PIPE, text=True)
print(result.stdout)

# 콘솔에 결과 출력하지 않도록 설정
subprocess.run(["ls", "-l"], stdout=subprocess.DEVNULL)

# Shell Script 실행
subprocess.run(["파일 경로", "arguments"], shell=True)