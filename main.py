import pygame
from Av import Av
from Shot import Shot
from Player import Player

pygame.init()

width, height = 1800, 1000
display = pygame.display.set_mode((width, height))

shot_pic = pygame.image.load('heart-removebg-preview.png')
shot_pic = pygame.transform.scale(shot_pic, (50, 50))

player_pic = pygame.image.load('WhatsApp_Image_2022-02-14_at_15.17.07-removebg-preview.png')
player_pic = pygame.transform.scale(player_pic, (150, 150))

# sounds :
shooting_sound = pygame.mixer.Sound('hietz.wav')
shooting_sound.set_volume(0.2)

av_kill_sound = pygame.mixer.Sound('ani hoev otha.wav')
av_kill_sound.set_volume(20)

pygame.mixer.music.load('2022-02-12-16-33-45-_online-video-cutter.com_.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)

# av animation
av_pic_array = []
p1 = pygame.image.load('av1-removebg-preview.png')
p1 = pygame.transform.scale(p1, (200, 200))
av_pic_array.append(p1)

p1 = pygame.image.load('av2-removebg-preview.png')
p1 = pygame.transform.scale(p1, (200, 200))
av_pic_array.append(p1)

p1 = pygame.image.load('av3-removebg-preview.png')
p1 = pygame.transform.scale(p1, (200, 200))
av_pic_array.append(p1)

p1 = pygame.image.load('av4-removebg-preview.png')
p1 = pygame.transform.scale(p1, (200, 200))
av_pic_array.append(p1)

av_pic_rect = p1.get_rect()

avs = []
shotArray = []

player = Player(500, 850, player_pic)

loss = False
win = False
score = 0

font = pygame.font.SysFont('segoeui', 100)
font_2 = pygame.font.SysFont('segoeui', 60)
loss_text = font.render('you lost', True, (0, 0, 0))
restart_text = font.render('restart game', True, (0, 0, 0))
win_text = font.render('winner ! ', True, (0, 0, 0))
mazal_tov_text = font.render('ךתוא בהוא ינא בוט לזמ', True, (0, 0, 0))
menu_text = font_2.render('menu', True, (0, 0, 0))


def restart():
    global loss, win, score
    loss, win = False, False
    score = 0
    avs.clear()
    shotArray.clear()
    for x in range(10):
        for y in range(5):
            z = Av(100 * x, 60 * y, av_pic_array)
            avs.append(z)


clock = pygame.time.Clock()
FPS = 100
av_timer = 0

passed_screen = False

restart()
game_loop = True
while game_loop:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        game_loop = False

    pos = (0, 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        print(pos)

    display.fill((100, 100, 100))

    # AV
    if passed_screen:

        score_text = font.render('score : ' + str(score) + " / 50 ", True, (0, 0, 0))
        display.blit(score_text, [50, 800])

        display.blit(menu_text, [50, 50])
        if 50 <= pos[0] <= 195 and 50 <= pos[1] <= 110:
            restart()
            passed_screen = False

        av_timer += 1 / FPS
        if av_timer > 1 / 10:
            for av in avs:
                av.change_animation()
            av_timer = 0

        for av in avs:
            av.display_on_screen(display)
            av.moving()
            if av.y > 900:
                loss = True

        # win :
        if len(avs) == 0:
            win = True

        if win:
            display.blit(win_text, [700, 500])
            display.blit(restart_text, [700, 650])
            display.blit(mazal_tov_text, [300, 800])

            if 700 <= pos[0] <= 1250 and 650 <= pos[1] <= 755:
                win = False
                restart()

        if loss:
            display.blit(loss_text, [700, 500])
            display.blit(restart_text, [700, 650])

            if 700 <= pos[0] <= 1250 and 650 <= pos[1] <= 755:
                loss = False
                restart()

        # PLAYER :

        player.display_on_screen(display)
        player.moving()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            shooting_sound.play()
            shotArray.append(Shot(player.x + 30, player.y, shot_pic, 8))

        for shot in shotArray:
            shot.display_on_screen(display)
            shot.moving()
            if len(shotArray) > 4 and shot in shotArray:
                shotArray.remove(shot)
            for av in avs:
                if shot.getRect().colliderect(av.getRect()) and shot in shotArray:
                    av_kill_sound.play()
                    score += 1
                    avs.remove(av)
                    shotArray.remove(shot)

    else:
        name_text = font.render('Av Invaders', True, (0, 0, 0))
        play_text = font.render('play game', True, (0, 0, 0))
        options_text = font.render('options', True, (0, 0, 0))
        quit_text = font.render('quit', True, (0, 0, 0))

        display.blit(name_text, [550, 300])
        display.blit(play_text, [600, 500])
        display.blit(quit_text, [630, 700])

        #   print(pos)
        if 600 <= pos[0] <= 1030 and 500 <= pos[1] <= 600:
            passed_screen = True
        if 630 <= pos[0] <= 790 and 700 <= pos[1] <= 815:
            quit(0)

    clock.tick(FPS)
    pygame.display.flip()
