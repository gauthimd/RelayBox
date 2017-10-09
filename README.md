# RelayBox
 This relay box consists of a power switch, a 120VAC to 5VDC USB wall wart, and Raspberry Pi Zero running the Raspbian OS, and a 4 channel relay board. When the power switch is turned on, the Raspberry Pi Zero boots and then runs relays.py as specified in /etc/rc.local. The program relays.py simply updates the relays by checking the file status.json. Any user interface can be created using any framework so long as the output of the program can manipulate the status.json file on the Pi. Currently I log in via secure shell and simply manipulate the file from my laptop using vi. Not very pretty, but it works. 
