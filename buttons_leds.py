import serial

# set the serial port
ser = serial.Serial('/dev/ttyS1')
ser.close()


def beep_short():
    ser.open()
    ser.write('2')
    ser.close()


def beep_long():
    ser.open()
    ser.write('3')
    ser.close()


def power_led_on():
    ser.open()
    ser.write('4')
    ser.close()


def power_led_flashing():
    ser.open()
    ser.write('5')
    ser.close()


def power_led_off():
    ser.open()
    ser.write('6')
    ser.close()


def status_led_off():
    ser.open()
    ser.write('7')
    ser.close()


def status_green_led_on():
    ser.open()
    ser.write('8')
    ser.close()


def status_green_led_flashing():
    ser.open()
    ser.write('9')
    ser.close()


def status_orange_led_on():
    ser.open()
    ser.write(':')
    ser.close()


def status_orange_led_flashing():
    ser.open()
    ser.write(';')
    ser.close()


# copy led is on the pcb of DS918+
def copy_led_off():
    ser.open()
    ser.write('@')
    ser.close()


def copy_green_led_on():
    ser.open()
    ser.write('A')
    ser.close()


def copy_green_led_flashing():
    ser.open()
    ser.write('B')
    ser.close()


def reset():
    ser.open()
    ser.write('C')
    ser.close()



