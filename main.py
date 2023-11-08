import pygame
import sys

pygame.init()

width = 640
height = 480
title_width = 300
title_height = 100
start_button_width = 100
start_button_height = 50
exit_button_width = 100
exit_button_height = 50

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Rhythm Game")

title = pygame.image.load("title.jpg")
start_button = pygame.image.load("start.jpg")
exit_button = pygame.image.load("exit.jpg")
background = pygame.image.load("BackGround.jpg")

title = pygame.transform.scale(start_button, (title_width, title_height))
start_button = pygame.transform.scale(start_button, (start_button_width, start_button_height))
exit_button = pygame.transform.scale(exit_button, (exit_button_width, exit_button_height))

running = True
game_state = "start"

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and game_state == "start":
            mouse_x, mouse_y = event.pos

            start_button_rect = start_button.get_rect()
            start_button_rect.topleft = (start_button_x, start_button_y)

            if start_button_rect.collidepoint(mouse_x, mouse_y):
                game_state = "play"

            exit_button_rect = exit_button.get_rect()
            exit_button_rect.topleft = (exit_button_x, exit_button_y)

            if exit_button_rect.collidepoint(mouse_x, mouse_y):
                running = False

    screen.blit(background, (0, 0))#배경 화면 그리기
    screen.blit(title, (200, 100))#제목 그리기

    if game_state == "start":

        #버튼의 위치
        start_button_x = width // 2 - 200
        start_button_y = 300
        exit_button_x = width // 2 + 120
        exit_button_y = 300

        #버튼 생성
        screen.blit(start_button, (start_button_x, start_button_y))
        screen.blit(exit_button, (exit_button_x, exit_button_y))

        #다음 화면 구현
    elif game_state == "play":
        pass

    pygame.display.update()

pygame.quit()
sys.exit()