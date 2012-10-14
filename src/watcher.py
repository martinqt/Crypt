from subprocess import *
import os, time

#get the python files in a dir
def getPyFiles(path = 'src'):
	for elmt in os.listdir(path):
		if elmt.endswith(".py"):
			yield [elmt, getModificationTime('src/'+elmt)]

#get the modification yime of the file
def getModificationTime(file):
	return os.stat(file).st_mtime

#print the sleepy snoring fox
def printSleepy():
	print("""  |\      _,,,---,,_           
  /,`.-'`'    -.  ;-;;,_       
 |,4-  ) )-,_..;\ (  `'-'      
'---''(_/--'  `-'\_)  zzz zzz   
				""")

#the main method
def fileWatcher():
	files = list(getPyFiles())
	
	sleepy = 0
	
	while 1:
		for elmt in files:
			if elmt[1] != getModificationTime('src/'+elmt[0]):
				if str(elmt[0]) == 'watcher.py':
					print('********** Please restart the watcher \n \n')
					elmt[1] = getModificationTime('src/'+elmt[0])

				else:
					print('***** Processing *****')
					call(['python', 'src/script.py'])				
					print('***** End ***** \n')

					elmt[1] = getModificationTime('src/'+elmt[0])
					sleepy = 0

					break
			else:
				sleepy += 1

		if sleepy > 120:
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
            |___/|_|            0.3a
             											 
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
