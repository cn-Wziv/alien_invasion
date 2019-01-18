class Setting():
    '''
    用于存储游戏中用到的各种设置
    '''
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5