from dataclasses import dataclass
from typing import Optional, Union, Iterable
import itertools


class InvalidSubPacket(Exception):
    ...


class UnexpectedEOF(Exception):
    ...


Packet = Union["LitPacket", "OpPacket"]


@dataclass
class PacketHdr:
    version: int
    type_id: int


@dataclass
class LitPacket:
    hdr: PacketHdr
    val: int


@dataclass
class OpPacket:
    hdr: PacketHdr
    len_type_id: int
    sub_packets: list[Packet]


class Parser:
    _HEADER_LENGTH = 6

    def __init__(self):
        self.iter: Optional[Iterable[int]] = None

    def parse(self, encoded: str):
        self.iter = itertools.chain.from_iterable(
            map(int, bin(int(c, 16))[2:].rjust(4, "0")) for c in encoded
        )
        return self._parse_packet()[0]

    def _parse_packet(self) -> tuple[Packet, int]:
        version, type_id = self._read(3), self._read(3)
        hdr = PacketHdr(version, type_id)
        return self._parse_lit(hdr) if type_id == 4 else self._parse_op(hdr)

    def _parse_lit(self, hdr: PacketHdr):
        packet_len = Parser._HEADER_LENGTH
        prefix = 1
        val = 0
        while prefix == 1:
            prefix, rest = self._read(), self._read(4)
            val = (val << 4) | rest
            packet_len += 5
        return LitPacket(hdr, val), packet_len

    def _parse_op(self, hdr: PacketHdr):
        sub_packets: list[Packet] = []
        len_type_id = self._read()
        packet_len = Parser._HEADER_LENGTH + 1
        if len_type_id == 0:
            expected_total_sub_packet_len = self._read(15)
            packet_len += 15
            total_sub_packet_len = 0
            while total_sub_packet_len < expected_total_sub_packet_len:
                sub_packet, sub_packet_len = self._parse_packet()
                sub_packets.append(sub_packet)
                total_sub_packet_len += sub_packet_len
                packet_len += sub_packet_len

            if total_sub_packet_len != expected_total_sub_packet_len:
                raise InvalidSubPacket
        else:
            expected_sub_packet_cnt = self._read(11)
            packet_len += 11
            for _ in range(expected_sub_packet_cnt):
                sub_packet, sub_packet_len = self._parse_packet()
                sub_packets.append(sub_packet)
                packet_len += sub_packet_len

        return OpPacket(hdr, len_type_id, sub_packets), packet_len

    def _read(self, n: int = 1) -> int:
        bits = 0
        for _ in range(n):
            b = next(self.iter, None)
            if b is None:
                raise UnexpectedEOF
            bits = (bits << 1) | b
        return bits


def solve(input: str):
    def sum_versions(packet: Packet):
        if isinstance(packet, LitPacket):
            return packet.hdr.version
        return packet.hdr.version + sum(
            sum_versions(sub_packet) for sub_packet in packet.sub_packets
        )

    parser = Parser()
    return sum_versions(parser.parse(input))
