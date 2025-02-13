# 8 Channel RS485 MODBUS RTU relay board type R421A08

This Python project can control up to 64 individual 8 channel R421A08 relay boards from the command line and GUI. It uses a universal USB - RS485 dongle.

### Project features:

* Python packages for easy application integration.
* Simple command line interface, useful for scripting.
* wxPython GUI tested with Python 3.5 only (Windows 10 and Ubuntu 16.04)
* Unit tests with coverage.



## Hardware

The following hardware is required for this project:

* One or more R421A08 relay boards.
* RS485 - USB dongle.
* Optional: A second RS485 - USB dongle to monitor MODBUS frames.

### R421A08 relay board

![R421A08 board](https://raw.githubusercontent.com/Erriez/R421A08-rs485-8ch-relay-board/master/images/R421A08.png)

* RS485 (binary) interface.
* 8 x 12V Relays: 10A 125VAC / 10A 28VDC.
* 8 status LED's.
* 6 DIP switches for 64 board addresses.
* Board power: 12V DC.
* Current board idle: ~11mA.
* Current one relay: ~26mA.
* Current all relays on: ~220mA.
* Length: 90mm, width: 60mm, height: 20mm.

**WARNING: DO NOT USE THIS RELAY BOARD WITH 230V AC!**  
The distance between relay traces on the PCB are < 2mm without holes for isolation. This is dangerous when using it with high voltages. See the picture above.

### R421B16 relay board

The 16 relay board version works by changing `NUM_RELAYS = 16` in `R421A08.py` as reported by a user in [issue #1](https://github.com/Erriez/R421A08-rs485-8ch-relay-board/issues/1).

### RS485 - USB dongle

This project requires a RS485 - USB dongle which is widely available, for example:

![RS485 - USB dongle](https://raw.githubusercontent.com/Erriez/R421A08-rs485-8ch-relay-board/master/images/RS485_USB_dongle.png)

* On Windows, open the ```Device Manager``` | ```Ports (COM & LPT)``` to find the ```USB-SERIAL CH340 (COMxx)``` serial port.
* On Linux, use the ```dmesg``` command  to find the serial port, such as ```/dev/ttyUSB0```.

## Software 

See `test.py`.

## Documentation

Please refer to the [Wiki page](https://github.com/Erriez/R421A08-rs485-8ch-relay-board/wiki) for installation and usage.



[MODBUS Application Protocol Specification v1.1.b](http://www.modbus.org/docs/Modbus_Application_Protocol_V1_1b.pdf)

The following Python packages are available in this project:

- R421A08 relay board Python package:
  - Read state relay(s).
  - Turn relay(s) on.
  - Turn relay(s) off.
  - Toggle relay(s).
  - Latch relay (One relay on, rest off).
  - Momentary (Turn relay on for one second).
  - Delay (Turn relay on for 1..255 seconds).
  - Single or multiple relay boards.
- Serial MODBUS Python package:
  - MODBUS monitor frames on the RS485 bus
  - Send raw ASCII MODBUS frames

### RS485 RTU MODBUS communication protocol

[MODBUS](https://en.wikipedia.org/wiki/Modbus) is an open binary serial communication protocol, mainly used for PLCs.

- Serial port at 9600 baud, 8 databits, 1 stop, no parity.
- This board supports MODBUS RTU protocol only.
- This board supports 64 addresses, configurable with 6 DIP switches.
- This board does **not** support ASCII mode, but can be send with the Python```--send``` option.
- This board does **not** support AT commands.
- This board does **not** support broadcasts.
- All relays are off after power-on.

