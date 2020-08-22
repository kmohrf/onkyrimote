import enum

from onkyrimote.device import Device
from onkyrimote.protocol import ChannelControl, PowerControl, VolumeControl


class TXSR304(ChannelControl, PowerControl, VolumeControl, Device):
    ID = "onkyo_txsr304"
    NAME = "Onkyo TX-SR304"

    class Channel(enum.Enum):
        CD = "cd"
        DVD = "dvd"
        VIDEO2 = "video2"

    COMMAND_CHANNEL_CD = 0x20
    COMMAND_CHANNEL_DVD = 0x120
    COMMAND_CHANNEL_VIDEO2 = 0x1A0
    COMMAND_POWER_OFF = 0x1AE
    COMMAND_POWER_ON = 0x1AF
    COMMAND_VOLUME_MUTE = 0x1A4
    COMMAND_VOLUME_UP = 0x1A2
    COMMAND_VOLUME_DOWN = 0x1A3

    volume_up = Device.sender(COMMAND_CHANNEL_VIDEO2, COMMAND_VOLUME_UP)
    volume_down = Device.sender(COMMAND_CHANNEL_VIDEO2, COMMAND_VOLUME_DOWN)
    mute = Device.sender(COMMAND_CHANNEL_VIDEO2, COMMAND_VOLUME_MUTE)
    unmute = Device.sender(
        COMMAND_CHANNEL_VIDEO2, COMMAND_VOLUME_UP, COMMAND_VOLUME_DOWN
    )

    power_off = Device.sender(COMMAND_CHANNEL_VIDEO2, COMMAND_POWER_OFF)
    power_on = Device.sender(COMMAND_POWER_ON)

    def set_channel(self, channel: Channel):
        try:
            channel_code = {
                self.Channel.CD: self.COMMAND_CHANNEL_CD,
                self.Channel.DVD: self.COMMAND_CHANNEL_DVD,
                self.Channel.VIDEO2: self.COMMAND_CHANNEL_VIDEO2,
            }[channel]
        except KeyError as exc:
            raise ValueError(f"Unsupported channel: {str(channel.value)}") from exc
        return self.backend.send_command(channel_code)
