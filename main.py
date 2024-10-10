import pygame
import sys
import BounceGameStart

# 初始化 Pygame
pygame.init()

# 设置屏幕尺寸
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ZAKUII Follows Mouse")

# 加载机器人图片（确保文件路径正确）
ZAKU_image = pygame.image.load("ZAKUII.png").convert_alpha()
power_image= pygame.image.load("power.png").convert_alpha()
gundam_image= pygame.image.load("gundam.png").convert_alpha()

# Scale the image size
ZAKU_image = pygame.transform.smoothscale(ZAKU_image, (150, 150))

# Get the rectangle area of the image
ZAKU_rect = ZAKU_image.get_rect()


# 获取图片的矩形区域
ZAKU_rect = ZAKU_image.get_rect()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 主循环
running = True
while running:
    # 处理关闭
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取鼠标位置
    mouse_pos = pygame.mouse.get_pos()

    # 将机器人图片的中心对准鼠标位置
    ZAKU_rect.center = mouse_pos

    # 填充背景为黑色
    screen.fill((0, 0, 0))

    # 绘制跟随鼠标的机器人图片
    screen.blit(ZAKU_image, ZAKU_rect)


#生命设定
    myfont = pygame.font.SysFont('monospace', 24)
    life = 3
    life_text = "Life: " + str(life)
    life_surface = myfont.render(life_text, True, (100, 100, 100))  #字体
    screen.blit(life_surface, (20, 20))
    # 血量变化
#碰到高达会减少生命

    #随机出现的能量增加生命


#碰撞体积

    # 刷新屏幕
    pygame.display.update()

# 退出 Pygame
pygame.quit()
sys.exit()