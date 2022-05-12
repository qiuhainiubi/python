#外星人入侵小游戏
# settings.py
#存储外星人入侵小游戏的所有设置的类
class Setting():
    def __init__(self):  #__init__ 注意是两个短下划线
        #初始化游戏的静态设置
        #屏幕设置
        self.screen_width = 1550
        self.screen_height = 800
        #屏幕背景颜色设置
        self.bg_color = (230,230,230)
        
        # 因为rect的centerx等属性只能存储整数值，所以需要对ship类做修改
        self.ship_limit = 3

        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
        #以上代码创建了宽3像素、高15像素的深灰色子弹

        #外星人设置
        self.fleet_drop_speed = 5
        #fleet_drop_speed表示有外星人撞到屏幕边缘时，外星人群向下移动的速度
        
        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1 #speedup_scale用于控制游戏节奏的加快速度
        self.initialize_dynamic_settings()

        #击落外星人得分的提高速度
        self.score_scale = 1.5


    def initialize_dynamic_settings(self):
        #初始化游戏的动态设置
        self.ship_speed = 1.5  # 飞船速度设置为1.5，则移动时每次移动1.5像素
        self.bullet_speed = 1
        self.alien_speed = 0.5
        #fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        self.alien_points = 5 #击落一个外星人得分5


    def increase_speed(self):
        #提高速度设置
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        #为了提高游戏元素的速度，我们设置将每个速度都乘以speedup_scale的值
        self.alien_points = int(self.alien_points * self.score_scale)