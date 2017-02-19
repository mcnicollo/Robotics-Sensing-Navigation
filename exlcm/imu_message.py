"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class imu_message(object):
    __slots__ = ["yaw", "pitch", "roll", "magx", "magy", "magz", "accelx", "accely", "accelz", "gyrox", "gyroy", "gyroz"]

    def __init__(self):
        self.yaw = 0.0
        self.pitch = 0.0
        self.roll = 0.0
        self.magx = 0.0
        self.magy = 0.0
        self.magz = 0.0
        self.accelx = 0.0
        self.accely = 0.0
        self.accelz = 0.0
        self.gyrox = 0.0
        self.gyroy = 0.0
        self.gyroz = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(imu_message._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">dddddddddddd", self.yaw, self.pitch, self.roll, self.magx, self.magy, self.magz, self.accelx, self.accely, self.accelz, self.gyrox, self.gyroy, self.gyroz))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != imu_message._get_packed_fingerprint():
            raise ValueError("Decode error")
        return imu_message._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = imu_message()
        self.yaw, self.pitch, self.roll, self.magx, self.magy, self.magz, self.accelx, self.accely, self.accelz, self.gyrox, self.gyroy, self.gyroz = struct.unpack(">dddddddddddd", buf.read(96))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if imu_message in parents: return 0
        tmphash = (0xaea9131432012057) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if imu_message._packed_fingerprint is None:
            imu_message._packed_fingerprint = struct.pack(">Q", imu_message._get_hash_recursive([]))
        return imu_message._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

