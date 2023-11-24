import sys, os, json

from PySide6.QtCore import QThread

from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.remote.remote_service_discovery import RemoteServiceDiscoveryService
from pymobiledevice3.services.dvt.dvt_secure_socket_proxy import DvtSecureSocketProxyService

from nut.coreProfileSessionTap import NutCoreProfileSessionTap
from nut.log import Log

log = Log.getLogger('widget')

class Thread_getFps(QThread):
    def __init__(self, window = None):
        super().__init__()
        self.window = window
        log.info(f'{self.window}')

    def run(self):
        if len(sys.argv) > 1:
            log.info(f'ios17 hight Fps get')

            RSD_json_path = sys.argv[1]
            if not os.path.isfile(RSD_json_path):
                log.info(f'waiting file: {RSD_json_path}')
                while not os.path.isfile(RSD_json_path):
                    pass
                log.info(f'file found: {RSD_json_path}')

            with open(RSD_json_path, 'r') as f:
                RSD_info = json.load(f)

            log.info(f'start tunnel done: {RSD_info.get("host")} {RSD_info.get("port")}')

            with RemoteServiceDiscoveryService((RSD_info.get("host"), RSD_info.get("port"))) as rsd:
                with DvtSecureSocketProxyService(rsd) as dvt:
                    with NutCoreProfileSessionTap(dvt, {}, None) as tap:
                        tap.getFPS(window = self.window)
        else:
            log.info(f'ios16 hight Fps get')
            lockdown = create_using_usbmux()
            with DvtSecureSocketProxyService(lockdown) as dvt:
                with NutCoreProfileSessionTap(dvt, {}, None) as tap:
                    tap.getFPS(window = self.window)
