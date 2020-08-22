import time


class Backend:
    def send_command(self, command):
        raise NotImplementedError()

    def send_commands(self, *commands, wait_in_between=0.25):
        first_iteration = True
        for command in commands:
            if first_iteration:
                first_iteration = False
            else:
                time.sleep(wait_in_between)
            self.send_command(command)
