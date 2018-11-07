#!/usr/bin/python3

""" write bootable sector
  mchen

  According with https://github.com/cfenollosa/os-tutorial/tree/master/01-bootsector-barebones, 
  writes
    0xe9 0xfd 0xff 0x00 ...
    ...  ...  ...  0x55 0xaa
  total 512 bytes to a binary file as a bootable disk
"""

BOOT_SECTOR_SZ = 512

INFINITE_JMP  = b'\xE9\xFD\xFF'
BOOTABLE_FLAG = b'\x55\xAA' 
BYTE_STUFFING = b'\x00'

boot_sector = INFINITE_JMP \
        + BYTE_STUFFING * (BOOT_SECTOR_SZ - len(INFINITE_JMP) - len(BOOTABLE_FLAG) ) \
        + BOOTABLE_FLAG

with open("boot_sector_simple.bin", "wb") as fo:
  fo.write(boot_sector)
  fo.close()