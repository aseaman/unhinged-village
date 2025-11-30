import board
import displayio
from fourwire import FourWire

import adafruit_ili9341

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_cs = board.D9
tft_dc = board.D10

display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D6)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

# Make the display context
splash = displayio.Group()
display.root_group = splash

test_bitmap = displayio.OnDiskBitmap("/images/head-on.bmp")
test_tile_grid = displayio.TileGrid(test_bitmap, pixel_shader=test_bitmap.pixel_shader)

#test_tile_grid.y = (display.height - test_bitmap.height) // 2

splash.append(test_tile_grid)

while True:
    pass
