import pygame
import math
import time
import os
import random
import sys

#초기화

pygame.init()

width = 800
height = 800
title_width = 400
title_height = 150
start_button_width = 200
start_button_height = 100
exit_button_width = 225
exit_button_height = 100
help_button_width = 205
help_button_height = 100
start_button_x = width // 2 - 100
start_button_y = 350
exit_button_x = width // 2 - 110
exit_button_y = 550
help_button_x = width // 2 - 100
help_button_y = 450

screen = pygame.display.set_mode((width, height))

#게임 제목
pygame.display.set_caption("Rhythm Game")

title = pygame.image.load("title_yellow.png")
start_button = pygame.image.load("start.png")
exit_button = pygame.image.load("exit.png")
help_button = pygame.image.load("help.png")
background = pygame.image.load("BackGround.jpg")
image_note = pygame.image.load("1.png")

title = pygame.transform.scale(title, (title_width, title_height))
start_button = pygame.transform.scale(start_button, (start_button_width, start_button_height))
exit_button = pygame.transform.scale(exit_button, (exit_button_width, exit_button_height))
help_button = pygame.transform.scale(help_button, (help_button_width, help_button_height))

keys_to_check = [pygame.K_q, pygame.K_w]

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

            help_button_rect = help_button.get_rect()
            help_button_rect.topleft = (help_button_x, help_button_y)

            if help_button_rect.collidepoint(mouse_x, mouse_y):
                game_state = help

    screen.blit(background, (0, 0))#배경 화면 그리기

    if game_state == "start":
        #버튼 생성
        screen.blit(start_button, (start_button_x, start_button_y))
        screen.blit(exit_button, (exit_button_x, exit_button_y))
        screen.blit(help_button, (help_button_x, help_button_y))

        #제목 생성
        screen.blit(title, (200, 100))

    elif game_state == "help":
        screen.blit(background, (0, 0))
        help_text = pygame .font.Font(None, 36).render("이것은 도움말 화면입니다", True, (255, 255, 255))
        screen.blit(help_text, (width // 2 - 150, height // 2 - 50))

        #게임 기능 구현
    elif game_state == "play":
        font_test = pygame.font.SysFont(None, 50)
        point1 = 0
        point2 = 0
        judge_rect1 = pygame.draw.line(screen, (255, 255, 255), (50, 650), (350, 650), int(8)) # 판정선 그리기(검은색), (surface, color, start_point, end_point, width)
        judge_rect2 = pygame.draw.line(screen, (255, 255, 255), (450, 650), (750, 650), int(8))
        pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 800), int(8))

        rect_note = image_note.get_rect()

        if rect_note.colliderect(judge_rect1):  # 노트랑 판정선 충돌
            if pygame.key.get_pressed()[keys_to_check[0]]:  # q 키를 눌렀을 때
                point1 += 1
        if rect_note.colliderect(judge_rect2):  # 노트랑 판정선 충돌
            if pygame.key.get_pressed()[keys_to_check[1]]:  # w 키를 눌렀을 때
                point2 += 1

        text_point = font_test.render(str(point1), True, (255, 182, 193)) # 색상 핑크색
        background.blit(text_point, (50, 30)) # 텍스트 좌표
        text_point = font_test.render(str(point2), True, (255, 182, 193))  # 색상 핑크색
        background.blit(text_point, (750, 30))  # 텍스트 좌표

        text_point = font_test.render("P1", True, (255, 255, 255))
        background.blit(text_point, (180,680 ))  # 텍스트 좌표
        text_point = font_test.render("P2", True, (255, 255, 255))
        background.blit(text_point, (580,680 ))  # 텍스트 좌표

    pygame.display.update()

pygame.quit()
sys.exit()

