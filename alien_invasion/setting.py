class Setting():
    '''
    用于存储游戏中用到的各种设置
    '''
    def __init__(self):
        # 背景
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # 飞船相关
        self.ship_limit = 3                 # 命

        # 子弹相关
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 屏幕上出现的最多子弹数
        self.bullet_allowed = 3

        # 外星人相关
        # 外星人移动速度
        self.fleet_drop_speed = 10

        # 以什么速度加快游戏节奏
        self.speedup_scale = 1.1

        # 外星人点数提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # 初始化岁游戏进行而变化的设置
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # 记分
        self.alien_points = 50

        # fleet_direction为1表示向右，-1表示向左
        self.fleet_direction = 1




    def increase_speed(self):
        # 提高速度设置
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

