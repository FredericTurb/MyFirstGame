import pygame, time, sys 
from sys import exit

pygame.init()
clock = pygame.time.Clock()

# MUSIC 

pygame.mixer.init()
pygame.mixer.music.load('./music/song1.mp3')
pygame.mixer.music.play(loops=-1, start=0)

# SCREEN INIT

pygame.display.set_caption("My First Game")

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surface = pygame.Surface((1920, 1080))
surface.fill('blue')

# IMPORT BACKGROUND PICTURE AND RESCALE 

background = pygame.image.load('./images/night.png')
background = pygame.transform.scale(background, (1920, 1080))
floor = pygame.image.load('./images/floor.png')
floor = pygame.transform.scale(floor, (1950, 400))

# DISPLAY TEXT ON SCREEN

pygame.font.init()
font_timer = pygame.font.Font('./font/Pixeltype.ttf', 94)
font_options = pygame.font.Font('./font/Pixeltype.ttf', 55)
WHITE = (255, 255, 255)
ORANGE = (255, 189, 48)

# CREATES A TIMER

timer = pygame.time.get_ticks()

# CHARACTER INIT

player = pygame.image.load('./images/mycat.png')
player = pygame.transform.scale(player, (350, 350))
player_rect = player.get_rect(center=(100,850))

# VARIABLES FOR MUSIC INPUTS

is_paused = False
m_key_pressed = False

l_pause = False
l_key_pressed = True


# PAUSE MUSIC

def my_pause_music():
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
    else:
        pygame.mixer.music.pause()
        is_paused = True

# CHANGE MUSIC

def my_change_music():
    global l_pause
    if l_pause:
        pygame.mixer.music.load('./music/song1.mp3')
        pygame.mixer.music.play(loops=-1, start=0)
        l_pause = False
    else:
        pygame.mixer.music.load('./music/song2.mp3')
        pygame.mixer.music.play(loops=-1, start=0)
        l_pause = True

going_left = False

while True :

# QUIT PROGRAM WHEN ASKED TO QUIT

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# TIMER CREATION

    seconds = (pygame.time.get_ticks() - timer) // 1000
    timer_display = f"Time: {seconds}"
    text_surface = font_timer.render(timer_display, True, WHITE)
    text_center = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))

# TEXT TO PAUSE / UNPAUSE THE MUSIC

    music_display = "Press M to pause/unpause music"
    text_music_surface = font_options.render(music_display, True, ORANGE)
    text_music_placement = text_music_surface.get_rect(center=(1600, 50))

    change_music_display = "Press L to change the music"
    text_change = font_options.render(change_music_display, True, ORANGE)
    text_change_placement = text_change.get_rect(center=(1600, 100))

# STORES USER INPUT IN KEY    

    key = pygame.key.get_pressed()

# STOP THE MUSIC BY PRESSING M 

    if key[pygame.K_m]:
        if not m_key_pressed:
            my_pause_music()
            m_key_pressed = True
    else:
        m_key_pressed = False

# CHANGE MUSIC

    if key[pygame.K_l]:
        if not l_key_pressed:
            my_change_music()
            l_key_pressed = True
    else:
        l_key_pressed = False


# CHARACTER MOVEMENT 

    if key[pygame.K_q] or key[pygame.K_LEFT]:
        player_rect.move_ip(-20, 0)
        going_left = True
    elif key[pygame.K_d] or key[pygame.K_RIGHT]:
        player_rect.move_ip(20, 0)
        going_left = False
    
    #elif key[pygame.K_z] or key[pygame.K_UP]:
    #    player_rect.move_ip(0, -20)

    #elif key[pygame.K_s] or key[pygame.K_DOWN]:
    #    player_rect.move_ip(0, 20)

    #elif key[pygame.K_SPACE]:
    #    player_rect.move_ip(0, -100)


    # DRAW CHARACTER, SCREEN BACKGROUND AND TEXT 

    screen.blit(background, (0,0))
    screen.blit(floor, (0, 790))
    screen.blit(text_surface, text_center)
    screen.blit(text_music_surface, text_music_placement)
    screen.blit(text_change, text_change_placement)

    if going_left:
        flipped = pygame.transform.flip(player, True, False)
        screen.blit(flipped, player_rect)
    else:
        screen.blit(player, player_rect)

    pygame.display.flip()
    clock.tick(60)