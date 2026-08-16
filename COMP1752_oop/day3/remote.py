from television import Television

class Remote:
    def __init__(self, tv):
        self.tv = tv
    def on(self):
        self.tv.turn_on()
    def off(self):
        self.tv.turn_off()
    def number(self, n):
        self.tv.switch_channel(n)
    def volup(self):
        self.tv.volume_up()
    def voldown(self):
        self.tv.volume_down()
    def mute(self):
        self.tv.mute()

if __name__ == "__main__":
    tv = Television()
    remote = Remote(tv)
    remote.on()
    remote.number(2)
    remote.volup()
    remote.voldown()
    remote.mute()
    remote.mute()

    remote.off()
    remote.number(3)
    remote.mute()

    remote.on()
    remote.number(11)
    remote.voldown()
