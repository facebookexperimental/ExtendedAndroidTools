import unittest
from jdwp.serialization.serializer import JDWPPacketHeader, JDWPPacket, serialize_jdwp_packet


class TestJDWPPacketSerialization(unittest.TestCase):
    def test_jdwp_packet_serialization(self):
        header = JDWPPacketHeader(15, 1, 0x80, 2, 3)

        payload = b"Sample Payload"
        packet = JDWPPacket(header, payload)

        serialized_packet = serialize_jdwp_packet(packet)
        self.assertEqual(len(serialized_packet), 15)


if __name__ == '__main__':
    unittest.main()
