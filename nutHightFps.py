import sys, os, json, logging
from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.remote.remote_service_discovery import RemoteServiceDiscoveryService
from pymobiledevice3.services.dvt.dvt_secure_socket_proxy import DvtSecureSocketProxyService
import nut.coreProfileSessionTap as nut
# from nut.log import Log

log = logging.getLogger('Nut')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        assert os.path.isfile(sys.argv[1]), f'输入参数不是一个文件，{sys.argv[1]}'

        log.info(f'ios17 hight Fps get')

        RSD_json_path = sys.argv[1]
        if not os.path.isfile(RSD_json_path):
            log.info(f'wait for {RSD_json_path}')
            while not os.path.isfile(RSD_json_path):
                pass

        with open(RSD_json_path, 'r') as f:
            RSD_info = json.load(f)

        log.info(f'start tunnel done: {RSD_info.get("host")} {RSD_info.get("port")}')

        with RemoteServiceDiscoveryService((RSD_info.get("host"), RSD_info.get("port"))) as rsd:
            with DvtSecureSocketProxyService(rsd) as dvt:
                with nut.NutCoreProfileSessionTap(dvt, {}, None) as tap:
                    tap.getFPS()
    else:
        log.info(f'ios16 hight Fps get')
        lockdown = create_using_usbmux()
        with DvtSecureSocketProxyService(lockdown) as dvt:
            with nut.NutCoreProfileSessionTap(dvt, {}, None) as tap:
                tap.getFPS()
