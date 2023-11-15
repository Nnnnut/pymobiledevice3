from pymobiledevice3.remote.remote_service_discovery import RemoteServiceDiscoveryService
from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.services.syslog import SyslogService
import sys


# Or via remoted (iOS>=17)
# First, create a tunnel using:
#     $ sudo pymobiledevice3 remote start-quic-tunnel
# You can of course implement it yourself by copying the same pieces of code from:
#     https://github.com/doronz88/pymobiledevice3/blob/master/pymobiledevice3/cli/remote.py#L68
# Now you can simply connect to the created tunnel's host and port

if sys.argv[1] == '--rsd':
    host = sys.argv[2]  # 'fded:c26b:3d2f::1'
    port = sys.argv[3]  # 65177
print(f'--rsd {host} {port}')
with RemoteServiceDiscoveryService((host, port)) as rsd:
    for line in SyslogService(service_provider=rsd).watch():
        # just print all syslog lines as is
        print(line)