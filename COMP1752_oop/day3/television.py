class Television:
    def __init__(self):
        self.channel = ['CC', 'No', 'BBC', 'TV360']
        self.current = 0
        self.volume = 5
        self.status = False
        self.maxvol = 10
        self.muted = False
        self.storedvolume = self.volume

    def turn_on(self):
        self.status = True
        self.playing()

    def turn_off(self):
        self.status = False
        print(f'TV is off')

    def switch_channel(self, n):
        # check if TV is off
        if self.status == False:
            print(f'TV is off. Turn on first.')
            return
        # check if number inputted is outside range
        if n < 0 or n >= len(self.channel):
            print('Invalid channel number. Choose between 0 and ', len(self.channel)-1)
            return
        # set channel number if previous conditions is false
        self.current = n
        self.playing()

    def volume_up(self):
        # check if TV is off
        if self.status == False:
            print(f'TV is off. Turn on first.')
            return
        # check if TV is muted
        if self.muted == True:
            print(f'TV is muted. Unmute first.')
            return
        # check if volume is max
        if self.volume >= self.maxvol:
            print('Max volume, cant increase.')
        # increase volume
        self.volume += 1
        self.playing()

    def playing(self):
        print(f'TV is currently playing {self.channel[self.current]} at volume {self.volume}.')


    def volume_down(self):
        # check if TV is off
        if self.status == False:
            print(f'TV is off. Turn on first.')
            return
        # check if TV is muted
        if self.muted == True:
            print(f'TV is muted. Unmute first.')
            return
        # check if volume is max
        if self.volume <= 0:
            print('Min volume, cant decreas.')
        # decrease volume
        self.volume -= 1
        self.playing()

    def mute(self):
        # check if TV is off
        if self.status == False:
            print(f'TV is off. Turn on first.')
            return
        # check if mute is on or off
        if self.muted == False:
            print('TV is muting.')
            self.volume = self.storedvolume
            self.volume = 0
            self.muted = True
            self.playing()
            return
        if self.muted == True:
            print('TV is unmuting.')
            self.volume = self.storedvolume
            self.muted = False
            self.playing()
            return

if __name__ == "__main__":
    tv = Television()
    tv.turn_on()
    tv.switch_channel(2)
    tv.volume_up()
    tv.volume_down()
    tv.mute()
    tv.mute()

    tv.turn_off()
    tv.switch_channel(3)
    tv.mute()

    tv.turn_on()
    tv.switch_channel(10)
    tv.volume_down()
