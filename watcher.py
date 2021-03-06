# -*-coding:Utf-8 -*

from subprocess import *
import os, time, sys

#get the Python files in a dir
def getPyFiles(paths = ['src', 'src/lib'], files = ['input.txt', 'watcher.py', 'script.py']):
    for directory in paths:
        for elmt in os.listdir(directory):
            if elmt.endswith(".py"):
                yield [directory+'/'+elmt, getModificationTime(directory+'/'+elmt)]

    for filename in files:
        yield [filename, getModificationTime(filename)]

#get the modification time of the file
def getModificationTime(filename):
    return os.stat(filename).st_mtime

#print the sleepy snoring fox
def printSleepy():
    print("""  |\      _,,,---,,_           
  /,`.-'`'    -.  ;-;;,_       
 |,4-  ) )-,_..;\ (  `'-'      
'---''(_/--'  `-'\_)  zzz zzz   
                """)

#the main method
def fileWatcher():
    outputFormat = ''

    for arg in sys.argv:
        if arg == '--frequency':
            outputFormat = 'frequency'
        if arg == '--percent':
            outputFormat = 'percent'

    files = list(getPyFiles())
    
    sleepy = 0
    
    while 1:
        for elmt in files:
            if elmt[1] != getModificationTime(elmt[0]):
                if str(elmt[0]) == 'watcher.py':
                    print('********** Please restart the watcher \n \n')
                    elmt[1] = getModificationTime(elmt[0])

                else:
                    print('***** Processing *****')
                    
                    if outputFormat == '':
                        call(['python', 'script.py'])
                    elif outputFormat == 'frequency':
                        call(['python', 'src/script.py', '--frequency'])
                    else:
                        call(['python', 'src/script.py', '--percent'])

                    print('***** End ***** \n')

                    elmt[1] = getModificationTime(elmt[0])
                    sleepy = 0

                    break
            else:
                files = list(getPyFiles())
                sleepy += 1

        if sleepy > 100:
            sleepy = 0
            printSleepy()

        time.sleep(1)

if __name__=='__main__':

    welcome = """ _____                  _   
/  __ \                | |  
| /  \/_ __ _   _ _ __ | |_ 
| |   | '__| | | | '_ \| __|
| \__/\ |  | |_| | |_) | |_ 
 \____/_|   \__, | .__/ \__|
             __/ | |        
            |___/|_|            

__          ___           _           
\ \        / / |         | |          
 \ \  /\  / /| |__   __ _| |_    __ _ 
  \ \/  \/ / | '_ \ / _` | __|  / _` |
   \  /\  /  | | | | (_| | |_  | (_| |
    \/  \/   |_| |_|\__,_|\__|  \__,_|
 _                      _   _  __       _  
| |                    | | (_)/ _|     | | 
| |__   ___  __ _ _   _| |_ _| |_ _   _| | 
| '_ \ / _ \/ _` | | | | __| |  _| | | | | 
| |_) |  __/ (_| | |_| | |_| | | | |_| | | 
|_.__/ \___|\__,_|\__,_|\__|_|_|  \__,_|_| 
     _               _        
    | |             | |       
  __| | __ _ _   _  | |_ ___  
 / _` |/ _` | | | | | __/ _ \ 
| (_| | (_| | |_| | | || (_) |
 \__,_|\__,_|\__, |  \__\___/ 
              __/ |           
             |___/                    
     _                            _   
    | |                          | |  
  __| | ___  ___ _ __ _   _ _ __ | |_ 
 / _` |/ _ \/ __| '__| | | | '_ \| __|
| (_| |  __/ (__| |  | |_| | |_) | |_ 
 \__,_|\___|\___|_|   \__, | .__/ \__|
                       __/ | |        
                      |___/|_|                 
 _ __ ___   ___  ___ ___  __ _  __ _  ___  ___ 
| '_ ` _ \ / _ \/ __/ __|/ _` |/ _` |/ _ \/ __|
| | | | | |  __/\__ \__ \ (_| | (_| |  __/\__ \\
|_| |_| |_|\___||___/___/\__,_|\__, |\___||___/
                                __/ |          
                               |___/            """

    print(welcome)

    fileWatcher()
