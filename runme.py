import datetime
import pyautogui
import sys
import json

while True:
    a = input("모드 설정:\n1: 좌표 확인\n2: 설정확인\n3: 실행\n4: 프로그램 종료\n: ")
    #use pyautogui to determine the coordinate of the current mouse location
    if a == '1':
        print(pyautogui.position())
        print("="*10)
        print("X좌표와 Y좌표를 setting.json에 입력해주세요")
    elif a == "2":
        with open("setting.json", encoding='UTF8') as f:
            jsondata = json.load(f)
            f.close()

        xcoor = jsondata["mouse_coordinate"]["x"]
        ycoor = jsondata["mouse_coordinate"]["y"]

        hr = jsondata["time"]["hour"]
        min = jsondata["time"]["minute"]

        msg = jsondata["inputmessage"]
        print("="*45)
        print(f"\nX좌표: {xcoor}, Y좌표: {ycoor}\n\n전송 시간: {hr}시 {min}분\n\n전송메세지: {msg}\n")
        print("="*45)

    elif a == "3":
        with open("setting.json", encoding='UTF8') as f:
            jsondata = json.load(f)
            f.close()

        print("프로그램이 돌아가기 시작합니다. 카카오톡을 열어주세요")
        print("\n")
        print("="*40)
        print("\n")

        xcoor = jsondata["mouse_coordinate"]["x"]
        ycoor = jsondata["mouse_coordinate"]["y"]

        hr = str(jsondata["time"]["hour"])
        min = str(jsondata["time"]["minute"])

        if len(hr) == 1:
            hr = "0"+hr
        
        if len(min) == 1:
            min = "0"+min

        while True:
            currenttime = str(datetime.datetime.now())

            timeonly = currenttime[11:].split(":")

            currenthr = timeonly[0]
            currentmin = timeonly[1]

            if currenthr == hr and currentmin == min:
                pyautogui.click(x=xcoor, y=ycoor)
                print("완료되었습니다")
                break
    else:
        sys.exit()