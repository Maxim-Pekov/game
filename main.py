import pygame
import sys

pygame.init()
power = 0
b_amulet = 1
s_amulet = 0
g_amulet = 0
menu = 0
pygame.display.set_caption('Крестики-Нолики', 'Крестик')  # Изменение заголовка окна
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('comicsansms', 50)  # Задание шрифта в переменную
font2 = pygame.font.SysFont('comicsansms', 30)  # Задание шрифта в переменную
font3 = pygame.font.SysFont('comicsansms', 20)  # Задание шрифта в переменную
# text = font.render('Какой-то текст', 1, 'white')  # отображение шрифта в окне приложения
clock = pygame.time.Clock()
FPS = 60

win = pygame.display.set_mode((600, 600))
color = (255, 255, 255)
color2 = (255, 255, 0)
button = pygame.image.load("images/Buttons.png").convert_alpha()
scale = pygame.transform.scale(
    button, (button.get_width() // 4,
               button.get_height() // 4))
button_rect = scale.get_rect(centerx=600//2, bottom=600-20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Обработка события нажатия на крестик закрытия окна
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            """Проверка нажатия кнопки мыши"""
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(x_mouse, y_mouse)
            if x_mouse > button_rect.x and x_mouse < button_rect.x + button_rect.width:
                if y_mouse > button_rect.y and x_mouse < button_rect.y + button_rect.width:
                    # amulet += 1
                    menu = 1

        elif event.type == pygame.USEREVENT and b_amulet or s_amulet or g_amulet:
            x = b_amulet * 0.5 + s_amulet * 5 + g_amulet * 50
            power += x

        elif event.type == pygame.KEYDOWN and pygame.K_SPACE:
            mas = [[0] * 10 for i in range(10)]
            queue = 0



    clock.tick(FPS)

    win.fill('black')
    t = font.render(f'power {power}', 1, 'white')
    a = font.render(f'bronze amulet {b_amulet}', 1, 'white')
    sa = font.render(f'silver amulet {s_amulet}', 1, 'white')
    ga = font.render(f'gold amulet {g_amulet}', 1, 'white')
    buy = font2.render(f'Купить амулет', 1, 'white')
    win.blit(t, (200, 200))
    win.blit(a, (200, 250))
    win.blit(sa, (200, 300))
    win.blit(ga, (200, 350))
    win.blit(scale, button_rect)
    scale.blit(buy, (12, 35))
    if menu:
        b = font3.render(f'amulet bronze - 10 power', 1, 'white')
        b_rect = b.get_rect(left=5, top=5)

        s = font3.render(f'amulet silver - 100 power', 1, 'white')
        s_rect = s.get_rect(left=5, top=30)

        g = font3.render(f'amulet gold - 1000 power', 1, 'white')
        g_rect = g.get_rect(left=5, top=55)
        win.blit(b, b_rect)
        win.blit(s, s_rect)
        win.blit(g, g_rect)
        if event.type == pygame.MOUSEBUTTONDOWN:
            """Проверка нажатия кнопки мыши"""
            x_mouse, y_mouse = pygame.mouse.get_pos()
            if x_mouse > g_rect.x and x_mouse < g_rect.x + g_rect.width:
                if y_mouse > g_rect.y and y_mouse < g_rect.y + g_rect.height:
                    if power > 1000:
                        g_amulet += 1
                        power -= 1000
                        menu = 0
            if x_mouse > s_rect.x and x_mouse < s_rect.x + s_rect.width:
                if y_mouse > s_rect.y and y_mouse < s_rect.y + s_rect.height:
                    if power > 100:
                        s_amulet += 1
                        power -= 100

                        menu = 0
            if x_mouse > b_rect.x and x_mouse < b_rect.x + b_rect.width:
                if y_mouse > b_rect.y and y_mouse < b_rect.y + b_rect.height:
                    if power > 10:
                        b_amulet += 1
                        power -= 10

                        menu = 0
                else:
                    menu = 0

    pygame.display.update()
