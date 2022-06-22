import time
import R421A08
import sys

SERIAL_PORT="/dev/ttyUSB2"

if __name__ == '__main__':
    print('Getting started R421A08 relay board\n')

    # Create MODBUS object
    _modbus = R421A08.Modbus(serial_port=SERIAL_PORT)

    # Open serial port
    try:
        _modbus.open()
    except R421A08.SerialOpenException as err:
        print(err)
        sys.exit(1)

    # Create relay board object
    board = R421A08.R421A08(_modbus, address=1)

    print('Status all relays:')
    board.print_status_all()
    time.sleep(1)

    print('Turn relay 1 on')
    board.on(1)
    time.sleep(1)

    print('Turn relay 1 off')
    board.off(1)
    time.sleep(1)

    print('Toggle relay 8')
    board.toggle(8)
    time.sleep(1)

    print('Latch relays 6 on, all other relays off')
    board.latch(6)
    time.sleep(1)

    print('Turn relay 4 on for 5 seconds, all other relays off')
    board.delay(4, delay=5)
    time.sleep(6)

    print('Turn relays 3, 7 and 8 on')
    board.toggle_multi([3, 7, 8])
    time.sleep(1)

    print('Turn all relays on')
    board.on_all()
    time.sleep(1)

    print('Turn all relays off')
    board.off_all()
    time.sleep(1)