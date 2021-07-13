from create import create
from check import check
from color import color, get_color
from judge import *
import pygame

# 生成矩阵并修改，分类坐标集合
make = check(create(40, 30))
raw = make[0]
block = 20  # 方块大小
all_num = make[2]  # 待消除方块数
size_raw = make[0].shape  # 高, 宽
size = (make[0].shape[1] * block, make[0].shape[0] * block)
# 每种元素规定一种随机颜色
color_list = []
temp = []
for elements in make[1]:
    color(color_list, elements[0])
white = [0, (255, 255, 255)]
color_list.append(white)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("连连看")
level = 0


# 方块未选中画面
def rect(num_, x_, y_):
    position = (x_, y_, block, block)
    color_ = get_color(color_list, num_)
    pygame.draw.rect(screen, color_, position, 0)
    pygame.display.update()


# 方块选中画面
def rect1(num_, x_, y_):
    position_bg = (x_, y_, block, block)
    position = (x_ + 1, y_ + 1, block - 2, block - 2)
    color_bg = (0, 0, 0)
    color_ = get_color(color_list, num_)
    pygame.draw.rect(screen, color_bg, position_bg, 0)
    pygame.draw.rect(screen, color_, position, 0)
    pygame.display.update()


while True:
    # 初始化界面
    if level == 0:
        for i in range(0, size_raw[0]):
            for j in range(0, size_raw[1]):
                rect(raw[i, j], j * block, i * block)
        level += 1
    if level == 1:
        pass
    if all_num == 0:
        pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 获取坐标，计算对应矩阵位置
            pos = pygame.mouse.get_pos()
            xx = int((pos[0] - pos[0] % block) / block)
            yy = int((pos[1] - pos[1] % block) / block)
            if raw[yy, xx] == 0:
                pass
            else:
                # 添加到临时列表
                temp.append((xx, yy))
            if len(temp) == 1:
                # 加载选中方块
                rect1(raw[temp[0][1], temp[0][0]], temp[0][0] * block, temp[0][1] * block)
            if len(temp) == 2:
                # 相同说明重复点击，则取消，加载未选中方块
                if temp[0] == temp[1]:
                    rect(raw[temp[0][1], temp[0][0]], temp[0][0] * block, temp[0][1] * block)
                else:
                    # 判断这两个坐标是否连通
                    a = judge(raw, temp[0][1], temp[0][0], temp[1][1], temp[1][0])
                    if a is True:
                        # 消除
                        raw[temp[0][1], temp[0][0]] = 0
                        raw[temp[1][1], temp[1][0]] = 0
                        rect(0, temp[0][0] * block, temp[0][1] * block)
                        rect(0, temp[1][0] * block, temp[1][1] * block)
                        all_num -= 1
                    else:
                        # 加载未选中，无事发生
                        rect(raw[temp[0][1], temp[0][0]], temp[0][0] * block, temp[0][1] * block)
                # 选中2个坐标后清除临时列表
                temp.clear()
