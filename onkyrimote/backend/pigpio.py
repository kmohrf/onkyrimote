import sys
import time

try:
    import pigpio
except ImportError:
    print(
        "You don’t have the pigpio python library installed. Try 'pip install pigpio'.",
        file=sys.stderr,
    )
    sys.exit(1)

from onkyrimote.backend import Backend


def generate_wave(gpio, command):
    _gpio = 1 << gpio
    yield pigpio.pulse(_gpio, 0, 3000)
    yield pigpio.pulse(0, _gpio, 1000)
    for _ in range(12):
        gap = 2000 if command & 2048 != 0 else 1000
        yield pigpio.pulse(_gpio, 0, 1000)
        yield pigpio.pulse(0, _gpio, gap)
        command *= 2
    yield pigpio.pulse(_gpio, 0, 1000)
    yield pigpio.pulse(0, _gpio, 40000)


class PiGPIOBackend(Backend):
    def __init__(self, gpio, pi=None):
        self.gpio = gpio
        self.pi = pigpio.pi() if pi is None else pi
        self.pi.set_mode(gpio, pigpio.OUTPUT)

    def send_command(self, command):
        self.pi.wave_clear()
        self.pi.wave_add_generic(list(generate_wave(self.gpio, command)))
        self.pi.wave_send_once(self.pi.wave_create())

        while self.pi.wave_tx_busy():
            time.sleep(0.1)
