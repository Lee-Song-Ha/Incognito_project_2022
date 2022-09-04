import os
import subprocess

# os.system()
os.system('echo Hello SYSTEM')

# subprocess.call()
result_call = subprocess.call('echo Hello CALL', shell=True)
print(result_call)

# subprocess.run()
# 기본적인 사용방법 (명령어 + 인자값(실행옵션))
subprocess.run(['echo', 'Hello RUN'], shell=True, encoding='utf-8')

# 리턴 값을 좀 더 상세히
subprocess.CompletedProcess(args=['echo', 'Hello RUN'], returncode=0)

# capture_output 인자를 True로 해줄 경우 실행된 결과를 stdout 인자에 저장
result_sub = subprocess.run(['echo', 'Hello RUN'], shell=True, capture_output=True, encoding='utf-8')
print(result_sub.stdout)

# subprocess.check_output()
subprocess.check_output('echo Hello CHECK_OUTPUT', shell=True, encoding='utf-8')

# 변수에 저장하여 출력하는것도 stdout 사용없이 바로바로 확인
result_check = subprocess.check_output('echo Hello CHECK_OUTPUT', shell=True, encoding='utf-8')
print(result_check)