import time
def timeList():
    filename='timedata.txt'
    with open(filename,'a') as f:
        nowtime=(time.strftime('%Y.%m.%d',time.localtime(time.time()))+'\n')
        f.write(nowtime)
        f.close
    return nowtime
