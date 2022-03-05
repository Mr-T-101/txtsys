import time
import math
import os
from pygame import mixer
import pyglet
import datetime
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def desktop():
    now = datetime.today()
    print(f"{now:%c}")
    help = input(bcolors.OKCYAN + '''
    /help for a list of commands
    ''')
    if help == '/help':
        print(bcolors.OKCYAN + '''
        /calculator - Trust your calculator, it's something to count on
        /txt - It's like Microsoft Word... but better
        /sys_edit - No
        /rickroll - Why?
        /end - You will be mist
        More coming soon!
        ''')
    commands = input('')
    if commands == '/calculator':
        pass
    elif commands == '/txt':
        print('remind be to add this later')
    elif commands == '/sys_edit':
        print(bcolors.WARNING + 'Welcome to sys_edit')
        print('''
        /user_details
        /txt settings
        
        ''')
    elif commands == '/rickroll':
        sourceFileDir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(sourceFileDir)
        mixer.init()
        mixer.music.load('rickroll-rick.wav')
        mixer.music.play()
        ag_file = "rickroll-rick.gif"
        animation = pyglet.resource.animation(ag_file)
        sprite = pyglet.sprite.Sprite(animation)

        # create a window and set it to the image size
        win = pyglet.window.Window(width=sprite.width, height=sprite.height)

        # set window background color = r, g, b, alpha
        # each value goes from 0.0 to 1.0
        green = 0, 1, 0, 1
        pyglet.gl.glClearColor(*green)

        @win.event
        def on_draw():
           win.clear()
           sprite.draw()

        pyglet.app.run()
    elif commands == '/end':
        pass
  

def add_user():
    f5 = open('users.txt', 'r+')
    f6 = open('passwords.txt', 'r+')
    new_user = input('USERNAME...')
    f5.write(new_user)
    user_pass = input ('PASSWORD...')
    f6.write(user_pass)
    boot_sequence()
    

def login():
    username = input(bcolors.OKBLUE +'Username...')
    string1 = username
    f = open('users.txt', 'r+')
    flag = 0
    index = 0
    for line in f:
        index += 1
        if string1 in line:
            flag = 1
            break
    if flag == 0:
        print(bcolors.WARNING + 'Username not found')
        add_close = input('Do you want to add a user?')
        if add_close == 'Yes':
            add_user()
        else:
            pass
    else:
        f.close()
        password = input(bcolors.OKGREEN + 'Password...')
        string2 = password
        f1 = open('passwords.txt', 'r+')
        flag2 = 0
        index2 = 0
        for line in f1:
            index2 += 1
            if string2 in line:
                flag2 = 1
                break
        if flag2 == 0:
            print(bcolors.FAIL + "incorrect")
            f1.close()
            pass
        else:
            print(bcolors.OKGREEN + 'Welcome', string1)
            time.sleep(1)
            desktop()


def boot_sequence():
    while True:
     end = input('')
     if end == '/end':
         break
    
     sourceFileDir = os.path.dirname(os.path.abspath(__file__))
     os.chdir(sourceFileDir)
     mixer.init()
     mixer.music.load('boot_sequence_music.wav')
     mixer.music.play()


     time.sleep(2)
     print(bcolors.OKCYAN + '''
     -------------------------------------------------------
     | -------------  ---------------                      |
     |       |              |    ------             ------ |
     |       |  \        /  |    |                  |      |
     |       |    \    /    |    ------  |       |  ------ |
     |       |      \/      |         |  \       |       | |
     |       |      /\      |    -----    -------|  ------ |
     |       |    /    \    |                    |         |
     |       |  /        \  |                   /          |
     |                                         /           |
     -------------------------------------------------------
     ''')
     time.sleep(2)
     print(bcolors.OKGREEN + 'txtsys is a registered trademark')
     time.sleep(2)
     print(bcolors.OKBLUE + 'You are running txtsys v0.1')
     time.sleep(2)
     print(bcolors.FAIL + '(c) Tom Eccleston 2022')
     time.sleep(10)
     mixer.music.pause()
     login()
     
   
boot_sequence()