import pygame, random, time, os
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
surface = pygame.Surface((100,100))


pygame.display.set_caption("Rhythm Game")

title = pygame.image.load("title.jpg")
start_button = pygame.image.load("start.jpg")
exit_button = pygame.image.load("exit.jpg")
background = pygame.image.load("BackGround.jpg")

title = pygame.transform.scale(title, (title_width, title_height))
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
        
        surface.fill((0,0,0))
        
        w = 640
        h = 480

        clock = pygame.time.Clock()
        keys = [0,0,0,0]
        keyset = [0,0,0,0]
        maxframe = 60
        fps = 0
        gst = time.time()
        speed = 2
        notesumt = 0

        a = 0
        aa = 0

        t1 = []
        t2 = []
        t3 = []
        t4 = []

        def sum_note(n):
            if n == 1:
                ty = 0 #노트 y축
                tst = Time #노트 소환 시간
                if n == 1:
                    t1.append([ty,tst])
                if n == 2:
                    t2.append([ty,tst])
                if n == 3:
                    t3.append([ty,tst])
                if n == 4:
                    t4.append([ty,tst])


        while True:
            
            
            
            Time = time.time() - gst

            if Time > 0.2 * notesumt:
                notesumt += 1
                while a == aa:
                    a = random.randint(1, 4)
                sum_note(a) 
                aa = a
                #노트 랜덤하게 떨어지게 만드는 함수

            fps = clock.get_fps()

            if  fps == 0:
                fps = maxframe

            for event in pygame.event.get(): #키 눌렀을때 노트 떨어짐(노트 삭제 포함)
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        keyset[0] = 1
                        if len(t1) > 0:
                            if t1[0][0] > h / 2:
                                del t1[0]
                    if event.key == pygame.K_f:
                        keyset[1] = 1
                        if len(t1) > 0:
                            if t2[0][0] > h / 2:
                                del t2[0]
                    if event.key == pygame.K_j:
                        keyset[2] = 1
                        if len(t1) > 0:
                            if t3[0][0] > h / 2:
                                del t3[0]
                    if event.key == pygame.K_i:
                        keyset[3] = 1
                        if len(t1) > 0:
                            if t4[0][0] > h / 2:
                                del t4[0]
                                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_e:
                        keyset[0] = 0
                    if event.key == pygame.K_f:
                        keyset[1] = 0
                    if event.key == pygame.K_j:
                        keyset[2] = 0
                    if event.key == pygame.K_i:
                        keyset[3] = 0

            for tile_data in t1:
                tile_data[0] = (h/12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
                pygame.draw.rect(screen, (255,255,255),(w / 2 - w / 8, tile_data[0] - h / 100, w / 16 , h / 50))
                if tile_data[0] > h - (h / 9):
                    t1.remove(tile_data)
            for tile_data in t2:
                tile_data[0] = (h/12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
                pygame.draw.rect(screen, (255,255,255),(w / 2 - w / 16, tile_data[0] - h / 100, w / 16 , h / 50))
                if tile_data[0] > h - (h / 9):
                    t2.remove(tile_data)
            for tile_data in t3:
                tile_data[0] = (h/12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
                pygame.draw.rect(screen, (255,255,255),(w / 2 + w / 16, tile_data[0] - h / 100, w / 16 , h / 50))
                if tile_data[0] > h - (h / 9):
                    t3.remove(tile_data)
            for tile_data in t4:
                tile_data[0] = (h/12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
                pygame.draw.rect(screen, (255,255,255), (w / 2 + w / 8, tile_data[0] - h / 100, w / 16 , h / 50))
                if tile_data[0] > h - (h / 9):
                    t4.remove(tile_data)
                    
            #감속속도 =============================================================        
            keys[0] += (keyset[0] - keys[0]) / (3 * (maxframe / fps))
            keys[1] += (keyset[1] - keys[1]) / (3 * (maxframe / fps))
            keys[2] += (keyset[2] - keys[2]) / (3 * (maxframe / fps))
            keys[3] += (keyset[3] - keys[3]) / (3 * (maxframe / fps))
            
            clock.tick(maxframe) #프레임제한
            
    pygame.display.flip()

pygame.display.update()

pygame.quit()
sys.exit()

