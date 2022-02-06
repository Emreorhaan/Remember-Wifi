import subprocess
import re

def getListWifi():
    wifiList = []
    passList = []

    getwifiList = str(subprocess.check_output("netsh wlan show profiles").decode(encoding='UTF-8'))
    getwifiList = re.split(':|All User Profile|\r|\\n', getwifiList)

    i = 21

    while i <= len(getwifiList)-4:
        x = getwifiList[i]
        x = x[1:]
        wifiList.append(x)
        i += 4

    for j in range(len(wifiList)):
        getwifipass = str(subprocess.check_output("""netsh wlan show profiles "{}" key=clear""".format(wifiList[j])))
        getwifipass = getwifipass.split("\\n")

        for i in range(len(getwifipass)):
            if "Open" in getwifipass[i] or "Absent" in getwifipass[i]:
                passList.append("No Password")
                break

            else:
                if "Key Content" in getwifipass[i]:
                    wipass = getwifipass[i]
                    wipass = wipass.split(":")
                    wipass[1] = wipass[1].replace("\\r", "")
                    passList.append(wipass[1])
                    break

    return wifiList, passList
    
if __name__ == "__main__":
    
    wifi,Password = getListWifi()
    print("        wifi Name          |     Wifi Password     |")
    print("-"*52)
    for i in range(len(wifi)-4):
        text = wifi[i]
        text += " "*(27-len(wifi[i]))
        text += "|"
        text += "   "
        text += Password[i]
        print(text)
        print("-"*52)

input()

