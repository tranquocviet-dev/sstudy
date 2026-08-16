class Fan:
    def __init__(self):
        self.speed = 0
        self.status = False
        self.swing = False
        self.MAX_SPEED = 3

    def show(self):
        print(f'Fan running at speed {self.speed}')

    def speed_up(self):
        if self.status == False:
            print('Turn on fan first')
            return
        if self.speed >= self.MAX_SPEED:
            print('Speed already maxed')
            return
        self.speed += 1
        self.show()

    def speed_down(self):
        if self.status == False:
            print('Turn on fan first')
            return
        if self.speed == 1:
            print('Speed already min')
            return
        self.speed -= 1
        self.show()
