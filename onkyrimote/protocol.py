class ChannelControl:
    def set_channel(self, channel):
        raise NotImplementedError()


class PowerControl:
    def power_off(self):
        raise NotImplementedError()

    def power_on(self):
        raise NotImplementedError()


class VolumeControl:
    def volume_up(self):
        raise NotImplementedError()

    def volume_down(self):
        raise NotImplementedError()

    def mute(self):
        raise NotImplementedError()

    def unmute(self):
        raise NotImplementedError()
