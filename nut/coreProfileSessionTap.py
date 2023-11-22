from pymobiledevice3.services.dvt.dvt_secure_socket_proxy import DvtSecureSocketProxyService
from pymobiledevice3.services.remote_server import Tap, MessageAux
# from pymobiledevice3.services.dvt.instruments.core_profile_session_tap import CoreProfileSessionTap
from pymobiledevice3.services.dvt.instruments.core_profile_session_tap import STACKSHOT_HEADER
import typing, uuid, time, struct
from nut.log import Log

logger = Log.getLogger('corePro')

class NutCoreProfileSessionTap(Tap):

    IDENTIFIER = 'com.apple.instruments.server.services.coreprofilesessiontap'

    def __init__(self, dvt: DvtSecureSocketProxyService, time_config: typing.Mapping, filters: typing.Set = None):
        """
        :param dvt: Instruments service proxy.
        :param time_config: Timing information - numer, denom, mach_absolute_time and matching usecs_since_epoch,
        timezone.
        :param filters: Event filters to include, Include all if empty.
        """
        self.dvt = dvt
        self.stack_shot = None
        self.uuid = str(uuid.uuid4())

        if filters is None:
            filters = {830472984}

        config = {
            'tc': [{
                'csd': 128,  # Callstack frame depth.
                'kdf2': filters,  # Kdebug filter, receive all classes.
                'tk': 3,  # Kind.
                'uuid': self.uuid,
            }],  # Triggers configs
            'rp': 100,  # Recording priority
            'bm': 0,  # Buffer mode.
            'ur': 2000,
        }

        super().__init__(dvt, self.IDENTIFIER, config)

    def _kperf_data(self, messages):
        _list = []
        p_record = 0
        m_len = len(messages)
        if m_len % 64 != 0:
            return _list
        while p_record < m_len:
            _list.append(struct.unpack('<QLLQQQQLLQ', messages[p_record:p_record + 64]))
            p_record += 64
        return _list
        
    def restart(self, sleep_time = 5):
        # stop
        self.channel.stop(expects_reply=False)

        time.sleep(sleep_time)

        # start
        # self.channel = self._dvt.make_channel(self._channel_name)
        self.channel.setConfig_(MessageAux().append_obj(self._config), expects_reply=False)
        self.channel.start(expects_reply=False)

        # first message is just kind of an ack
        self.channel.receive_plist()
        return self

    def getFPS(self, timeout: int = None):
        start = time.perf_counter()
        
        NANO_SECOND = 1e9
        MACH_TIME_FACTOR = 125 / 3
        last_frame = None
        frame_count = 0
        time_count = 0

        skip_count = 0
        skip_time = time.perf_counter()
        
        while timeout is None or time.time() <= start + timeout:
            data = self.channel.receive_message()
            if data.startswith(STACKSHOT_HEADER) or data.startswith(b'bplist'):
                if skip_count > 20:
                    skip_count = -1
                    logger.error(f'goin restart, time: {time.perf_counter()-skip_time:.3f}s')
                    self.restart()
                if skip_count >= 0:
                    skip_count = skip_count+1
                else:
                    logger.info(f'wait service restart')
                    time.sleep(1)
                # Skip not kernel trace data.
                continue
            skip_count = 0
            skip_time = time.perf_counter()
            # print(f'Receiving trace data ({len(data)}B)')
            for args in self._kperf_data(data):
                _time, code = args[0], args[7]
                if code == 830472984:
                    if not last_frame:
                        last_frame = _time
                    else:
                        this_frame_cost = (_time - last_frame) * MACH_TIME_FACTOR
                        time_count += this_frame_cost
                        last_frame = _time
                        frame_count += 1
                
                if time_count > NANO_SECOND:
                    run_time_sec = time.perf_counter() - start
                    logger.info(f'FPS: {frame_count / time_count * NANO_SECOND:3.5f}, costTime: {run_time_sec//3600%60:02.0f}:{run_time_sec//60%60:02.0f}:{run_time_sec%60:02.0f}, time: {time_count / NANO_SECOND:.4f}')
                    frame_count = 0
                    time_count = 0