from pysnes.cartrige import ROMHeader
from pysnes.helper import open_as_byte_array
from unittest import skip
from os.path import abspath, dirname, join

here = abspath(dirname(__file__))
ROM_DIR = abspath(join(here, '..', 'rom'))


@skip
def test_parse_header0():
    ROM_NAME = 'DonkeyKongCountry.smc'
    ba = open_as_byte_array(join(ROM_DIR, ROM_NAME))
    header = ROMHeader(ba)
    assert header.name.decode('utf-8') == 'DONKEY KONG COUNTRY  '
    assert hex(header.addr) == '0x81c0'
    assert hex(header.makeup) == '0x31'
    assert header.reset_int_addr == 0x8000


@skip
def test_parse_header1():
    ROM_NAME = 'SecretofMana.smc'
    ba = open_as_byte_array(join(ROM_DIR, ROM_NAME))
    header = ROMHeader(ba)
    assert header.name.decode('utf-8') == 'Secret of MANA       '
    assert hex(header.addr) == '0xffc0'
    assert hex(header.makeup) == '0x21'
    assert header.reset_int_addr == 0x8004


@skip
def test_parse_header2():
    ROM_NAME = 'Terranigma.smc'
    ba = open_as_byte_array(join(ROM_DIR, ROM_NAME))
    header = ROMHeader(ba)
    assert header.name.decode('utf-8') == 'TERRANIGMA D         '
    assert hex(header.addr) == '0x101c0'
    assert hex(header.makeup) == '0x31'
    assert header.reset_int_addr == 0x8000


def test_parse_header3():
    ROM_NAME = 'ca65.smc'
    ba = open_as_byte_array(join(ROM_DIR, ROM_NAME))
    header = ROMHeader(ba)
    assert (
        header.name.decode('utf-8')
        == 'CA65 EXAMPLE\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    )
    assert hex(header.addr) == '0x7fc0'
    assert hex(header.makeup) == '0x30'
    assert header.reset_int_addr == 0x8000
