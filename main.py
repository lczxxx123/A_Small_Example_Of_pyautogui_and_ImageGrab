import time

import pyautogui
from PIL import ImageGrab


    
def getScreen():   
    screen = ImageGrab.grab()
    pix = screen.getdata()
    pix = pix.convert('RGB')
    return pix

def getXY(pix):
    return 150,205

def getHash(aa):
    return aa[0] * 1000000 + aa[1] *1000 + aa[2] 
a = (76,176)
b = (557,176)
c = (76,662)
d = (557,662)
# pix = getScreen()
# for x in range(0,pix.size[0]):
#     for y in range(0,pix.size[1]):
#         print(pix[x * pix.size[0] + y])
#         if pix[x * pix.size[0] + y][1] is not 255:
#             pyautogui.moveTo(y,x)
#             print(x,y)
#             break
#     break

targetScore = 255
count = 0
step = 15
while(True):
    count += 1
    if(count > targetScore):
        break
    #print("now " + str(count) + " try of " + str(targetScore))
    #time.sleep(0.01)
    pix = getScreen()
    # ttt = 0.5
    # pyautogui.moveTo(a)
    # time.sleep(ttt)
    # pyautogui.moveTo(b)
    # time.sleep(ttt)
    # pyautogui.moveTo(c)
    # time.sleep(ttt)
    # pyautogui.moveTo(d)
    # time.sleep(ttt)
    
    d = {}
    for x in range(181,660,step):#76,557):
        for y in range(77,556,step):#176,662):
            # if ((x+y) % 1000 == 0):      
            #     pyautogui.moveTo(y,x)
            #     print(pix[x * pix.size[0] + y])
            tt = getHash(pix[x * pix.size[0] + y])
            d[tt] = d.setdefault(tt,0) + 1
    dd = sorted(d.items(), key=lambda d: d[1],reverse=True)
    # print(dd)
    # print(dd[1][1])
    flag = False
    targetIndex = 1
    failedColor = [221221221,56056056,108108108,139139139,60182222,30092112]
    while (dd[targetIndex][0] in failedColor):
        targetIndex += 1

    for x in range(181,660,step):#76,557):
        for y in range(77,556,step):#176,662):
            # if ((x+y) % 1000 == 0):      
            #     pyautogui.moveTo(y,x)
            #     print(pix[x * pix.size[0] + y])
            tt = getHash(pix[x * pix.size[0] + y])
            if (tt == dd[targetIndex][0]):
                pyautogui.moveTo(y,x)
                #print("catch "+ str(x) + " " + str(y))
                pyautogui.click()
                flag = True
                break
        if flag:
            break



