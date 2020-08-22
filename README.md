# onkyrimote

A python-library and command line utility for controlling Onkyo receivers that support the RI protocol.

## Installation

onkyrimote can be installed via pip.

```sh
pip install onkyrimote
onkyrimote --help
```

You may also check-out the repository and set the `PYTHONPATH=.` environment variable set.

```sh
# inside the checked-out repository directory
PYTHONPATH=. onkyrimote --help
```

## Usage

### With a Raspberry Pi

onkyrimote is modular, but currently only supports [pigpio](http://abyz.me.uk/rpi/pigpio/) meaning that your receiver has to be connected to a Raspberry Pi. Thanks to pigpiod you can run onkyrimote directly on the Pi or on another computer, if the Pi is reachable via network [1].

You’ll need the pigpio python library to continue. You can (and should) install it with your systems package manager (e.g. `apt install python3-pigpio` on Debian, Raspbian, and Raspberry Pi OS) or you may also use pip (`pip install pigpio`).

If you successfully connected your receiver to your Raspberry Pi the following command should turn it on. In case you have a different device, this command might not work. You can look at the onkyrimote help – `onkyrimote --help` – for a list of supported devices. Contributions with new devices are welcome too! 

```sh
onkyrimote --gpio 17 --device onkyo_txsr304 power_on
```

If you want use onkyrimote via the network, you can set the `PIGPIO_ADDR` and `PIGPIO_PORT` environment variables. The following command does the same as above but pigpiod is running on a host with the IP-Address `192.168.0.16` and on port `8765` (instead of the default `8.8.8.8`):

 ```sh
PIGPIO_ADDR=192.168.0.16 PIGPIO_PORT=8765 onkyrimote --gpio 17 --device onkyo_txsr304 power_on
 ```

[1]: Many distributions start pigpiod in a way that it cannot be reached via network, but only locally. If that is the case for you, you can edit the corresponding systemd unit. Run `systemctl edit pigpiod` and include the following configuration in the editor that is opened:

```
[Service]
ExecStart=
ExecStart=/usr/bin/pigpiod
```

### With another platform

No other backends have been implemented yet. Feel free to contribute one!


## Acknowledgements

Thanks go out to the [onkyo-rpi](https://github.com/ahaack/onkyo-rpi) and [onkyo-ri](https://github.com/docbender/Onkyo-RI) projects that have similar goals and have been used for reference!
