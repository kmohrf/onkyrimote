import argparse

from onkyrimote.device import SUPPORTED_DEVICES


def _get_args():
    parser = argparse.ArgumentParser(
        "onkymote", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--backend",
        type=str,
        choices={"pigpio"},
        default="pigpio",
        help="The backend to use for controlling the device.",
    )
    parser.add_argument(
        "--gpio", type=int, default=24, help="The GPIO used in the backend."
    )
    parser.add_argument(
        "--device",
        type=str,
        choices=[d.ID for d in SUPPORTED_DEVICES],
        required=True,
        help="The device type to use issue commands for.",
    )
    parser.add_argument(
        "command",
        choices={"power_on", "power_off", "volume_up", "volume_down", "mute", "unmute"},
        help="The command to execute. Currently does not support commands with arguments.",
    )
    return parser.parse_args()


def _resolve_backend(backend_id, args):
    if backend_id == "pigpio":
        from onkyrimote.backend.pigpio import PiGPIOBackend

        return PiGPIOBackend(args.gpio)
    raise ValueError("Unsupported backend: {}".format(backend_id))


def _resolve_device(device_id, backend):
    device_cls = None
    for device in SUPPORTED_DEVICES:
        if device.ID == device_id:
            device_cls = device
            break
    if device_cls is None:
        raise ValueError("Unsupported device: {}".format(device_id))
    return device_cls(backend)


def main():
    args = _get_args()
    backend = _resolve_backend(args.backend, args)
    device = _resolve_device(args.device, backend)
    getattr(device, args.command)()


if __name__ == "__main__":
    main()
