# coding=utf-8
'''
Author:SholWay.
Date:2019.10.01
For:检测网站内容是否有改动,若有则会播放音乐.
'''
import pygame
import time
import os
import sys
website = "http://www.baidu.com/" # 这边更改要监控的网页

def checkNetwork(saveType):
    if(os.system("curl {}>{}".format(website,saveType))):
        print ("Network Connect Error!!!")
        sys.exit()
    
def getMusic():
    if(os.system("curl https://rl01-sycdn.kuwo.cn/89bb4d4be00d0eed1482f0f88658a26b/5d935a67/resource/n3/1/49/4211576901.mp3 --output alert.mp3")):
        print ("Download alert music failure!Check the source or your network before use.")

def playMusic():
    pygame.mixer.init()
    pygame.mixer.music.load('alert.mp3')
    pygame.mixer.music.play(start=0.0)
    time.sleep(1800)

def getPageSource():
    checkNetwork(saveType="newCode")

def main():
    while 1:
        print (50*"-")
        getPageSource() 
        print ('Get web source code done!')
        if ((os.system("diff originalCode newCode"))==0):
            print ("Checked page code didn't change...")
            print (50*"-")
            time.sleep(20)
        else:
            print (50*"--")
            print ("\033[5;31m Warning: Webpage source has been changed! Check it now please!!! \033[0m")
            print ("")
            playMusic()
            

if __name__=='__main__':
    try:
        checkNetwork(saveType='originalCode')
        getMusic()
        main()
    except Exception,err:
        print (err)
        sys.exit()
