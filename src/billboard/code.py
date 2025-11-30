import board
import busio
import digitalio
import displayio
import os
import storage
import adafruit_ili9341
import adafruit_sdcard
from fourwire import FourWire

# Release any resources currently in use for the displays
displayio.release_displays()

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

display_bus = FourWire(spi, command=board.D10, chip_select=board.D9, reset=board.D6)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

# Make the display context
splash = displayio.Group()
display.root_group = splash

test_bitmap = displayio.OnDiskBitmap("/sd/head-on.bmp")
test_tile_grid = displayio.TileGrid(test_bitmap, pixel_shader=test_bitmap.pixel_shader)

#test_tile_grid.y = (display.height - test_bitmap.height) // 2

splash.append(test_tile_grid)

while True:
    pass
