import sys, os, json
from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.remote.remote_service_discovery import RemoteServiceDiscoveryService
from pymobiledevice3.services.dvt.dvt_secure_socket_proxy import DvtSecureSocketProxyService

from PySide6.QtWidgets import QApplication
from nut.nutWidget import NutWidget

from nut.log import Log

log = Log.getLogger('Nut')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = NutWidget()
    win.show()
    
    ret = app.exec()
    sys.exit(0)
