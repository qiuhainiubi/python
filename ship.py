#外星人入侵小游戏
# ship.py
#管理飞船行为的类
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen): #__init__ 注意是两个短下划线
        super().__init__()
        #让飞船类继承Sprite类
        #参数screen用来指定将飞船绘制到什么地方
        #参数ai_settings让飞船能获取到速度设置
        self.screen = screen
        #加载飞船图像并获取其外接矩形
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        # 复制图片路径后需要将斜杠改为反斜杠
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        #在飞船的属性centerx中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志,玩家按下右箭头键时，将标志设为true，
        # 松开时重新设置为false
        self.moving_right = False
        self.moving_left = False
    
    # 方法update()检查标志状态，标志为true时调整飞船位置
    def update(self):
        #更新飞船的center值，而不是rect
        #在修改self.center的值前检查飞船的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed
        #根据self.center更新rect对象
        self.rect.centerx = self.center
    
    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        #让飞船在屏幕上居中
        self.center = self.screen_rect.centerx
        #我们不需要创建多艘飞船，只需要一个飞船。
        # 在该飞船被撞到时将其居中。根据统计信息ship_left知道飞船次数是否用完。
        
