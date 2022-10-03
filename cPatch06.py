import os

command = "echo $PATH"
stream = os.popen(command)
result = stream.read()


try:
    resultList = list(result)
    if "." in resultList:
        print("PATH START")

        resultList.remove(".")
        path = ''.join(resultList)

        pathCommand = ("PATH=%s" %path)
        os.system(pathCommand)
        print("PATH END")

    else:
        print("No Problem")

    print("success")

except:
    print("fail")