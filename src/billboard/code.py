import board
import busio
import digitalio
import displayio
import storage
import time
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
screen = displayio.Group()
display.root_group = screen

image_files = [
    "/sd/head-on.bmp",
    "/sd/haribo-sad.bmp",
    "/sd/smoke-tarrlytons.bmp",
    "/sd/dinosaurs.bmp",
    "/sd/obey-tiled.bmp",
    "/sd/sti.bmp",
]

# Temp placeholder before loop below
screen.append(displayio.Group())

while True:
    for file in image_files:
        bmp = displayio.OnDiskBitmap(file)

        screen[0] = displayio.TileGrid(bmp, pixel_shader=bmp.pixel_shader)
        time.sleep(5)
