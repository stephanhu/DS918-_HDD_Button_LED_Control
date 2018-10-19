import gpio3


class Disk:

    __detect__ = None
    __enable__ = None

    def __init__(self, __gpio_enable__, __gpio_detect__):

        self.__detect__ = gpio3.LinuxGPIO(__gpio_detect__.gpio)
        # Do not change stuff when it is already set in the right direction and polarity
        if self.__detect__.direction == 'out':
            self.__detect__.direction = 'in'
        if self.__detect__.active_low != __gpio_detect__.polarity:
            self.__detect__.active_low = __gpio_detect__.polarity

        self.__enable__ = gpio3.LinuxGPIO(__gpio_enable__.gpio)
        # Do not change stuff when it is already set in the right direction and polarity
        if self.__enable__.direction == 'in':
            self.__enable__.direction = 'out'
        if self.__enable__.active_low != __gpio_enable__.polarity:
            self.__enable__.active_low = __gpio_enable__.polarity

        # self.__enable__.value = 0

    def enable_disk(self):
        self.__enable__.value = 1

    def disable_disk(self):
        self.__enable__.value = 0

    def check_for_disk(self):
        ret = self.__detect__.value
        return ret











