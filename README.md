# GPIO Switches
Goal is to use the Power and Volume switches from the Arcade 1 up cabinet to control the power and volume

## Software Installation
### Prerequisits
For volume you need to install `python3-alsaaudio`.
```
sudo apt-get install python3-alsaaudio
```

### Install
```
sudo ./install.sh
```

## Physical Installation
### Volume
* Volume Up: `GPIO 12` (Red wire)
* Volume Down: `GPIO 16` (Blue Wire)

### Power
Power is managed by jumping `GPIO` pins `5` and `6`.
By default this switch will start the pi when it is in low power shutdown.
The included script will shut down the pi when the pin goes low.


# References
* https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi
