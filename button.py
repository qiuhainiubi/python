#胡小小Python学习之路
#外星人入侵小游戏
# button.py
#创建按钮的类
import pygame.font
#模块font可以将文本渲染到屏幕上


class Button():
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #设置按钮的尺寸和其他属性
        self.width, self.height = 150, 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 36)

        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        #按钮rect的center属性设置为屏幕的rect的center属性可以实现按钮居中

        #按钮标签只需创建一次
        self.prep_msg(msg) #msg表示要显示在按钮上的文本

    def prep_msg(self, msg):
    #将msg渲染为图像，并使其在按钮上居中
        self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    #绘制按钮到屏幕上
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)