import pygame, math, time, os, random

w = 1600
h = w * (9 / 16)

clock = pygame.time.Clock()
keys = [0, 0, 0, 0]
keyset = [0, 0, 0, 0]
maxframe = 60
fps = 0
gst = time.time()
speed = 2
notesumt = 0
ingame = True


a = 0
aa = 0

t1 = []
t2 = []
t3 = []
t4 = []


def sum_note(n):
    if n == 1:
        ty = 0  # 노트 y축
        tst = Time  # 노트 소환 시간
        if n == 1:
            t1.append([ty, tst])
        if n == 2:
            t2.append([ty, tst])
        if n == 3:
            t3.append([ty, tst])
        if n == 4:
            t4.append([ty, tst])


while ingame:

    if time > 0.2 * notesumt:
        notesumt += 1
        while a == aa:
            a = random.randomint
        sum_note(a)
        aa = a
        # 노트 랜덤하게 떨어지게 만드는 함수

    TIme = time.time() - gst

    fps = clock.get_fps()

    if fps == 0:
        fps = maxframe

    for event in pygame.event.get():  # 키 눌렀을때 노트 떨어짐(노트 삭제 포함) # 키랑 칸이랑 연결되어 있어야 하는 거 아님?
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

    screen.fill((0, 0, 0))

    for tile_data in t1:
        tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
        pygame.draw.rect(screen, (255, 255, 255), (w / 2 - w / 8, tile_data[0] - h / 100, w / 16, h / 50))
        if tile_data[0] > h - (h / 9):
            t1.remove(tile_data)
    for tile_data in t2:
        tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
        pygame.draw.rect(screen, (255, 255, 255), (w / 2 - w / 16, tile_data[0] - h / 100, w / 16, h / 50))
        if tile_data[0] > h - (h / 9):
            t2.remove(tile_data)
    for tile_data in t3:
        tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
        pygame.draw.rect(screen, (255, 255, 255), (w / 2 + w / 16, tile_data[0] - h / 100, w / 16, h / 50))
        if tile_data[0] > h - (h / 9):
            t3.remove(tile_data)
    for tile_data in t4:
        tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
        pygame.draw.rect(screen, (255, 255, 255), (w / 2 + w / 8, tile_data[0] - h / 100, w / 16, h / 50))
        if tile_data[0] > h - (h / 9):
            t4.remove(tile_data)

    # 감속속도 =============================================================
    keys[0] += (keyset[0] - keys[0]) / (3 * (maxframe / fps))
    keys[1] += (keyset[1] - keys[1]) / (3 * (maxframe / fps))
    keys[2] += (keyset[2] - keys[2]) / (3 * (maxframe / fps))
    keys[3] += (keyset[3] - keys[3]) / (3 * (maxframe / fps))

    clock.tick(maxframe)  # 프레임제한

# 기본 틀 완성. 후에 작업 하면 될듯