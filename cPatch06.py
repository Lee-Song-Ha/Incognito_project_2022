import os

command = "echo $PATH"
stream = os.popen(command)
result = stream.read()


try:
    resultList = list(result)
    if "." in resultList:
        print("PATH START")

        # 패치!

    else:
        print("No Problem")

    print("success")

except:
    print("fail")