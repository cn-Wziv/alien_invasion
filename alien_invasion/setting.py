class Setting():
    '''
    用于存储游戏中用到的各种设置
    '''
    def __init__(self):
        # 背景
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船相关
        self.ship_speed_factor = 1.5        # 速度
        self.ship_limit = 3                 # 命

        # 子弹相关
        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = 60, 60, 60
        # 屏幕上出现的最多子弹数
        self.bullet_allowed = 3

        # 外星人相关
        # 外星人移动速度
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        # fleet_direction为1表示向右移，-1表示向左移
        self.fleet_direction = 1