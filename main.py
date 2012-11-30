import sys, os
sys.path.insert(0, os.getcwd()+'/src')
from mainWindow import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
