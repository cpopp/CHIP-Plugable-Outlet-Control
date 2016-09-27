import time, sys
from btaps import libbtaps
import CHIP_IO.GPIO as GPIO

def main(argv):
    
    if len(argv) != 2:
        print "USAGE:   python", sys.argv[0], "[Bluetooth address]"
        print "EXAMPLE: python", sys.argv[0], "00:00:FF:FF:00:00"
        sys.exit(0)
    
    btaps = libbtaps.BTaps(argv[1])
    connected = btaps.connect()
    if not connected:
        sys.exit(0)
    
    btaps.set_datetime_now()
    
    try:
        GPIO.setup("XIO-P1", GPIO.IN)
    except:
        # might've already been set as an input
        pass
    
    was_pressed = False
    btaps.set_switch(False)
    
    print("Waiting for button press")
    
    while True:
        value = GPIO.input("XIO-P1")
        is_pressed = value == 0
        
        if was_pressed and not is_pressed:
            print("Button was released")
            btaps.set_switch(False)
            time.sleep(.15)
        elif not was_pressed and is_pressed:
            print("Button was pressed")
            btaps.set_switch(True)
            time.sleep(.15)
    
        was_pressed = is_pressed
        
        time.sleep(.1)
        
if __name__ == '__main__':
    main(sys.argv)

