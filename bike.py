import pygame, time, sys
from sys import exit

pygame.init()
clock = pygame.time.Clock()

# MUSIC 

pygame.mixer.init()
pygame.mixer.music.load('./music/song1.mp3')
pygame.mixer.music.play(loops=-1, start=4)

# JUMP SOUND 

jump_sound = pygame.mixer.Sound("./music/scream.mp3")
jump_sound2 = pygame.mixer.Sound("./music/swoosh.mp3")
jump_sound2.set_volume(0.2)
dog_sound = pygame.mixer.Sound("./music/woman.mp3")
dog_sound.set_volume(0.4)
my_zomb = pygame.mixer.Sound("./music/zombax.mp3")
my_zomb.set_volume(5.4)


jump_change = 0


# SCREEN INIT

pygame.display.set_caption("Ride Your Brain")

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

# BACKGROUND SCROLLING 

bg_x1 = 0
bg_x2 = SCREEN_WIDTH
bgf_x1 = 0
bgf_x2 = SCREEN_WIDTH

# DISPLAY TEXT ON SCREEN

pygame.font.init()
font_timer = pygame.font.Font('./font/Pixeltype.ttf', 94)
font_options = pygame.font.Font('./font/Pixeltype.ttf', 55)
WHITE = (255, 255, 255)
ORANGE = (255, 189, 48)

# CREATES A TIMER

timer = pygame.time.get_ticks()

# MAIN CHARACTER INIT

player_or = pygame.image.load('./images/bike.png')
player_or = pygame.transform.scale(player_or, (550, 300))
player = pygame.transform.flip(player_or, True, False)
player_rect = player.get_rect(center=(500,850))

# DOG ENEMY INIT

# FIRST DOG
enemy = pygame.image.load('./images/zombie.png')
flipped_enemy = pygame.transform.scale(enemy,(120, 180))
flipped_enemy = pygame.transform.flip(enemy, True, False)
enemy_rect = flipped_enemy.get_rect(center=(2000, 915))

# SECOND DOG RIGHT

second_enemy = pygame.image.load('./images/zombie.png')
second_enemy = pygame.transform.scale(second_enemy,(260, 350))
second_flipped_enemy = pygame.transform.flip(second_enemy, True, False)
second_enemy_rect = second_flipped_enemy.get_rect(center=(2700, 865))

# DOG LEFT 
enemy_left = pygame.image.load('./images/zombie.png')
enemy_left = pygame.transform.scale(enemy_left,(240, 240))
enemy_left_rect = enemy_left.get_rect(center=(-1000, 915))

# VARIABLES FOR MUSIC INPUTS

is_paused = False
m_key_pressed = False

l_change = 0
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

song_display = "Playing : Ministry - I'm Not An Effigy"
text_song_surface = font_options.render(song_display, True, ORANGE)
text_song_placement = text_song_surface.get_rect(center=(320, 50))

def my_change_music():
    global l_change, song_display, text_song_surface, text_song_placement

    if l_change == 0:
        pygame.mixer.music.load('./music/song2.mp3')
        pygame.mixer.music.play(loops=-1, start=0)  
        song_display = "Richie Filth - Shallow Grave"
        text_song_surface = font_options.render(song_display, True, ORANGE)
        text_song_placement = text_song_surface.get_rect(center=(320, 50))
        l_change += 1
        return

    if l_change == 1:
        pygame.mixer.music.load('./music/song3.mp3')
        pygame.mixer.music.play(loops=-1, start=0)
        song_display = "AgainstMe - This Killed My Ego"
        text_song_surface = font_options.render(song_display, True, ORANGE)
        text_song_placement = text_song_surface.get_rect(center=(320, 50))        
        l_change += 1
        return

    if l_change == 2:
        pygame.mixer.music.load('./music/song4.mp3')
        pygame.mixer.music.play(loops=-1, start=0)
        song_display = "Balvanera - How Much Does The Body Resist ?"
        text_song_surface = font_options.render(song_display, True, ORANGE)
        text_song_placement = text_song_surface.get_rect(center=(390, 50))          
        l_change = 3
        return
    
    if l_change == 3:
        pygame.mixer.music.load('./music/song5.mp3')
        pygame.mixer.music.play(loops=-1, start=4)
        song_display = "Luidji - Gisele (Part 4)"
        text_song_surface = font_options.render(song_display, True, ORANGE)
        text_song_placement = text_song_surface.get_rect(center=(300, 50))          
        l_change = 4
        return
    
    if l_change == 4:
        pygame.mixer.music.load('./music/song1.mp3')
        pygame.mixer.music.play(loops=-1, start=2)
        song_display = "Ministry - I'm Not An Effigy"
        text_song_surface = font_options.render(song_display, True, ORANGE)
        text_song_placement = text_song_surface.get_rect(center=(320, 50))          
        l_change = 0
        return


going_left = False

# GRAVITY

GRAVITY = 2
JUMP_VELOCITY = -40
vertical_velocity = 20
on_ground = True

# DOG RANDOM 

dog_respwaned = 0
dog_left_respwaned = 0
second_dog_respwaned = 0

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
        if player_rect.x > 0:
            player_rect.move_ip(-30, 0)
            going_left = True
    elif key[pygame.K_d] or key[pygame.K_RIGHT]:
        if player_rect.x < 1500 :
            player_rect.move_ip(30, 0)
            going_left = False

# GRAVITY
    if key[pygame.K_SPACE] and on_ground:
        if jump_change == 1: 
            jump_sound2.play()
            jump_change = 0
        else : 
            jump_sound.play()
            jump_change = 1
        vertical_velocity = JUMP_VELOCITY
        on_ground = False

    vertical_velocity += GRAVITY
    player_rect.y += vertical_velocity

    if player_rect.y >= 1050 - player_rect.height:
        player_rect.y = 1050 - player_rect.height
        vertical_velocity = 0
        on_ground = True

# SCREEN SCROLLING WHEN X AXIS REACHED 

    if player_rect.x >= 500:
        bg_x1 -= 20
        bg_x2 -= 20

    if bg_x1 <= -SCREEN_WIDTH:
        bg_x1 = SCREEN_WIDTH
    if bg_x2 <= -SCREEN_WIDTH:
        bg_x2 = SCREEN_WIDTH


# SCREEN FLOOR SCROLLING

    if player_rect.x >= 500:
        bgf_x1 -= 5
        bgf_x2 -= 5

    if bgf_x1 <= -SCREEN_WIDTH:
        bgf_x1 = SCREEN_WIDTH
    if bgf_x2 <= -SCREEN_WIDTH:
        bgf_x2 = SCREEN_WIDTH


# ADDING GRAPHICS 
  
    screen.blit(background,(bg_x1,0))
    screen.blit(background,(bg_x2,0))   
    screen.blit(floor, (bg_x1, 790))
    screen.blit(floor, (bg_x2, 790))

    screen.blit(text_surface, text_center)
    screen.blit(text_music_surface, text_music_placement)
    screen.blit(text_change, text_change_placement)
    screen.blit(text_song_surface, text_song_placement)

    screen.blit(second_flipped_enemy, second_enemy_rect)
    screen.blit(enemy_left, enemy_left_rect)

    
# FLIP WHEN GOING LEFT 
    
    if going_left:
        flipped = pygame.transform.flip(player, True, False)
        screen.blit(flipped, player_rect)
    else:
        screen.blit(player, player_rect)
    screen.blit(flipped_enemy, enemy_rect)



# ENEMY DEPLACEMENT AND RESPAWN

    enemy_rect.x -= 30
    if enemy_rect.x <= -300:
        if dog_respwaned == 1:
            dog_sound.play()
            enemy_rect.x = 4500
            dog_respwaned = 2
        elif dog_respwaned == 2:
            enemy_rect.x = 2000
            dog_respwaned = 0
        else:
            enemy_rect.x = 3500
            my_zomb.play()
            dog_respwaned = 1            

# SECOND ENEMY RIGHT SIDE 

    second_enemy_rect.x -= 25
    if second_enemy_rect.x <= -300:
        if second_dog_respwaned == 1:
            second_enemy_rect.x = 4500
            second_dog_respwaned = 2
        elif second_dog_respwaned == 2:
            second_enemy_rect.x = 2000
            second_dog_respwaned = 0
        else:
            second_enemy_rect.x = 3500
            second_dog_respwaned = 1     


# ENEMY LEFT SIDE

    enemy_left_rect.x += 20
    if enemy_left_rect.x >= 2300:
        if dog_left_respwaned == 1:
            enemy_left_rect.x = -450
            dog_left_respwaned = 2
        elif dog_left_respwaned == 2:
            enemy_left_rect.x = -200
            dog_left_respwaned = 0
        else:
            enemy_left_rect.x = -300
            dog_left_respwaned = 1            

# ENEMY COLLISION 


    pygame.display.flip()
    clock.tick(60)