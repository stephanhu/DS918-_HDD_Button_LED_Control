#!/usr/bin/python3

import gpio_class
import disk_setup
import time
import buttons_leds


# set the power button led on... flashing is annoying

buttons_leds.power_led_on()
buttons_leds.beep_long()
buttons_leds.status_orange_led_flashing()

# get the count of hdds
hdd_count = disk_setup.DISK_COUNT

hdd = {}

# Setup GPIOs

for x in range(0, hdd_count):
    hdd[x] = gpio_class.Disk(disk_setup.enable_pins[x], disk_setup.detect_pins[x])

hdd_detect = {}
hdd_detect_old = {}
for x in range(0, hdd_count):
    hdd_detect[x] = 0
    hdd_detect_old[x] = 0

while 1:

    for x in range(0, hdd_count):
        hdd_detect[x] = hdd[x].check_for_disk()

    for x in range(0, hdd_count):
        # enable disk only on rising edge
        if hdd_detect[x] != hdd_detect_old[x] and hdd_detect[x]:
            hdd[x].enable_disk()
            print("Enable HDD:", x)

        # disable disk only on falling edge
        if hdd_detect[x] != hdd_detect_old[x] and not hdd_detect[x]:
            hdd[x].disable_disk()
            print("HDD removed:", x)

    for x in range(0, hdd_count):
        hdd_detect_old[x] = hdd_detect[x]

    # wait a little bit
    time.sleep(0.1)

if __name__ == '__main___':
    pass
