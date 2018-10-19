# detect pins (take the real ones, not the from Synology => they have a offset (about 512), look at source code
# for 'ARCH_NR_GPIOS' in include/asm-generic/gpio.h

# detect pins of HDD
GPIO_detect = [452, 334, 331, 330]
GPIO_detect_polarity = [1]
#GPIO_detect_polarity = ["ACTIVE_LOW"]

# enable pins of HDD
GPIO_enable = [455, 454, 453, 443]
# old values wrong order => [443, 453, 453, 455]
GPIO_enable_polarity = [0]
#GPIO_enable_polarity = ["ACTIVE_HIGH"]

DISK_COUNT = len(GPIO_enable)


# ----------------------------------------------------------------------------------------------------------------


class GpioEnable:
    polarity = 'ACTIVE_HIGH'
    gpio = 0

    def __init__(self, __gpio__, __polarity__):
        self.gpio = __gpio__
        self.polarity = __polarity__


class GpioDetect:
    polarity = 'ACTIVE_LOW'
    gpio = 0

    def __init__(self, __gpio__, __polarity__):
        self.gpio = __gpio__
        self.polarity = __polarity__


enable_pins = {}
detect_pins = {}
disk = {}

# error checking

hdd_count_tmp0 = len(GPIO_enable)
hdd_count_tmp1 = len(GPIO_detect)
hdd_count_en_pol = len(GPIO_enable_polarity)
hdd_count_dect_pol = len(GPIO_detect_polarity)
ret = 0

if hdd_count_tmp0 != hdd_count_tmp1:
    print("GPIOs don't match => Every HDD Slot needs a Enable Pin and a Detect Pin! Please look at the disk_setup.py")
    exit(1)

print("This DiskStation using {} HDDs.".format(hdd_count_tmp0))

if hdd_count_en_pol == 1:
    print("Enable Pins with polarity: {}".format(GPIO_enable_polarity))

if hdd_count_dect_pol == 1:
    print("Detect Pins with polarity: {}".format(GPIO_detect_polarity))

if (hdd_count_en_pol < hdd_count_tmp1) & (hdd_count_en_pol > 1):
    print("Parameter missing on Enable Pins! Look at GPIO_enable in disk_setup.py")
    ret = 1

if (hdd_count_dect_pol < hdd_count_tmp1) & (hdd_count_dect_pol > 1):
    print("Parameter missing on Detect Pins! Look at GPIO_enable in disk_setup.py")
    ret = 1

#for Item in GPIO_enable_polarity:
#    if "ACTIVE_HIGH" not in GPIO_enable_polarity and "ACTIVE_LOW" not in GPIO_enable_polarity:
#        print("Wrong parameter in enable polarity: {}".format(GPIO_enable_polarity))
#        ret = 1

#for Item in GPIO_detect_polarity:
#    if "ACTIVE_HIGH" not in GPIO_detect_polarity and "ACTIVE_LOW" not in GPIO_detect_polarity:
#        print("Wrong parameter in detect polarity: {}".format(GPIO_detect_polarity))
#        ret = 1

if ret >= 1:
    exit(1)

# Generate dict for GPIOs usage

for x in range(hdd_count_tmp0):

    disk[x] = {
        "gpio_enable": GPIO_enable[x],
        "gpio_detect": GPIO_detect[x],
    }
    # check if only one parameter for all pins is used
    if hdd_count_dect_pol == 1:
        disk[x]["gpio_detect_polarity"] = GPIO_detect_polarity[0]

    else:
        disk[x]["gpio_detect_polarity"] = GPIO_detect_polarity[x]

    if hdd_count_en_pol == 1:
        disk[x]["gpio_enable_polarity"] = GPIO_enable_polarity[0]

    else:
        disk[x]["gpio_enable_polarity"] = GPIO_enable_polarity[x]

    if hdd_count_en_pol != 1:
        enable_pins[x] = GpioEnable(GPIO_enable[x], GPIO_enable_polarity[x])
    else:
        enable_pins[x] = GpioEnable(GPIO_enable[x], GPIO_enable_polarity[0])

    if hdd_count_dect_pol != 1:
        detect_pins[x] = GpioDetect(GPIO_detect[x], GPIO_detect_polarity[x])
    else:
        detect_pins[x] = GpioDetect(GPIO_detect[x], GPIO_detect_polarity[0])

for i in range(hdd_count_tmp0):
    print(detect_pins[i].gpio)
    print(detect_pins[i].polarity)
    print(enable_pins[i].gpio)
    print(enable_pins[i].polarity)
