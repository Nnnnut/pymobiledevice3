import sys, time
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QThread
from nut.ui.nutFPSI_ui import Ui_iosFps

from nut.threadGetFps import Thread_getFps
from nut.log import Log

log = Log.getLogger('widget')

class NutWidget(QWidget):

    def __init__(self):
        super(NutWidget, self).__init__()
        self.ui = Ui_iosFps()
        self.ui.setupUi(self)

        self.ui.button_start.clicked.connect(self.button_start_clicked)
        self.ui.button_stop.clicked.connect(self.button_stop_clicked)
        self.ui.button_close.clicked.connect(self.button_close_clicked)

        self.keepGetFPS = True
        self.thread = Thread_getFps(window = self)
        self.thread.start()
        

    def button_start_clicked(self):
        self.ui.label_FPS.setText('start')
        
    def button_stop_clicked(self):
        self.ui.label_FPS.setText('stop')
        
    def button_close_clicked(self):
        self.keepGetFPS = False
        self.ui.label_FPS.setText('close')

    def setLableText_FPS(self, num:float):
        self.ui.label_FPS.setText(f'FPS: {num:3.5f}')

    def setLableText_costTime(self, text:str):
        self.ui.label_costTime.setText(f'costTime: {text}')
        
    def setLableText_time(self, num:float):
        self.ui.label_time.setText(f'time: {num:.4f}')

    def frashText(self, data:dict):
        self.setLableText_FPS(data['FPS'])
        self.setLableText_costTime(data['costTime'])
        self.setLableText_time(data['time'])
 
    def closeEvent(self, event):
        log.info(f'closeEvent in')
        self.keepGetFPS = False
        time.sleep(3)
