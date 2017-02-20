import pygame
import random

WIDTH = 500
HEIGHT = 700
FPS = 60



KEY_UP = 273
KEY_DOWN = 274
KEY_RIGHT = 275
KEY_LEFT = 276

WHITE = (255, 255, 255)
YELLOW = (250, 250, 210)




class Player_1(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # create a plain rectangle for the sprite image
        self.image = pygame.image.load('images/alien.png').convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = 250
        self.rect.bottom = 690
        self.speedx = 0
        self.shield = 100

    def update(self):
        # any code here will happen every time the game loop updates

        # keystate = pygame.key.get_pressed()  #holds key pressed down
        # if keystate[pygame.K_LEFT]:
        #     self.speedx = -3
        # if keystate[pygame.K_RIGHT]:
        #     self.speedx = 3

        self.rect.x += self.speedx

        if self.rect.right > WIDTH:        #keeps player on screen
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


    def attack(self):
        laser = Weapon(self.rect.centerx, self.rect.top)
        allsprites.add(laser)
        lasers.add(laser)
        lasersound.play()

        # if event.type == pygame.KEYDOWN:
        #     # activate the cooresponding speeds
        #     # when an arrow key is pressed down
        #     if event.key == KEY_LEFT:
        #         self.speedx = -4
        #     elif event.key == KEY_RIGHT:
        #         self.speedx = 4
        # if event.type == pygame.KEYUP:
        #     # deactivate the cooresponding speeds
        #     # when an arrow key is released
        #     if event.key == KEY_LEFT:
        #         self.speedx = 0
        #     elif event.key == KEY_RIGHT:
        #         self.speedx = 0

class OceanPlayer_1(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # create a plain rectangle for the sprite image
        self.image = pygame.image.load('images/submarine.png').convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = 250
        self.rect.bottom = 690
        self.speedx = 0

    def update(self):

        self.rect.x += self.speedx

        if self.rect.right > WIDTH:        #keeps player on screen
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


    def attack(self):
        laser = Weapon(self.rect.centerx, self.rect.top)
        allsprites.add(laser)
        lasers.add(laser)
        lasersound.play()



class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/enemy.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange( 0, 700)  #appear within screen
        self.rect.y = random.randrange( -100, - 40)   #appear on top of screen
        self.rectspeed = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.rectspeed
         #when enemy falls off of screen appears in random section
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange( 0, 700)  #appear within screen
            self.rect.y = random.randrange( -100, - 40)   #appear on top of screen
            self.rectspeed = random.randrange(1, 8)

class OceanEnemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/octopus.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange( 0, 700)  #appear within screen
        self.rect.y = random.randrange( -100, - 40)   #appear on top of screen
        self.rectspeed = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.rectspeed
         #when enemy falls off of screen appears in random section
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange( 0, 700)  #appear within screen
            self.rect.y = random.randrange( -100, - 40)   #appear on top of screen
            self.rectspeed = random.randrange(1, 8)

class Weapon(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/lasergreen.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = - 10

    def update(self):
        self.rect.y += self.speed
        #kill if it moves to the bottom
        # if self.rect.bottom < 0:
        #     self.kill()                #kill deletes any object



#
#
#can't add explode to ^ class
# class Target(pygame.sprite.Sprite):
#
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load('images/lasergreenshot.png').convert_alpha()
#         self.rect = self.image.get_rect()
#         self.rect.bottom = y
#         self.rect.centerx = x




# initialize pygame and create window
pygame.init()
pygame.mixer.init()     #starts sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aliens")
clock = pygame.time.Clock()

background = pygame.image.load('images/scenebackup.png').convert_alpha()
background_rect = background.get_rect()
startbackground = pygame.image.load('images/alienoceanbackground2.png').convert_alpha()
startbackground_rect = startbackground.get_rect()

ocean_background = pygame.image.load('images/ocean3.png').convert_alpha()
oceanbackground_rect = ocean_background.get_rect()

alientext = pygame.image.load('images/alienstext.png').convert_alpha()
oceantext = pygame.image.load('images/oceantext.png').convert_alpha()
lasersound = pygame.mixer.Sound('sounds/laser2.wav')
enemysound1 = pygame.mixer.Sound('sounds/exposion3.wav')
enemysound2 = pygame.mixer.Sound('sounds/explosions2.wav')

allenemy_sounds = [enemysound1, enemysound2]


pygame.mixer.music.load('sounds/flickersong.wav')
pygame.mixer.music.set_volume(0.4)      #music volume, for menu later
pygame.mixer.music.play(loops=-1)   #music loops around




font_name = pygame.font.match_font('Verdana')  #font works on all computer


def text(surf,text,size,x,y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, YELLOW)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)                       #center on page
    surf.blit(text_surface, text_rect)

def draw_health(surf,x,y,pct):
    if pct < 0:
        pct = 0

    bar_length = 100
    bar_height = 10

    fill = (pct / 100) * bar_length
    outline_rect = pygame.Rect(x,y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surf, YELLOW, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)   #how wide you want line to be

# displayscene = 1  #broken

def start_screen():
    screen.blit(startbackground, startbackground_rect)
    # screen.blit(alientext, (80,20) )
    # screen.blit(oceantext, (50,300))
    # text(screen,'Press 1 to play Aliens | Please 2 to play Little Submarine', 15, 250, 600)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:        #starts when key is pressed once
                if event.key == pygame.K_1:
                    displayscene = 1
                    waiting = False



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    displayscene = 2
                    waiting = False

            if event.type == pygame.QUIT:
                pygame.quit()



# allsprites = pygame.sprite.Group()
# enemy = pygame.sprite.Group()
# lasers = pygame.sprite.Group()
# player = Player_1()
#
# ocean_sprites = pygame.sprite.Group()
# oceanenemy = pygame.sprite.Group()
# oceanplayer = OceanPlayer_1()
#
#
#
# allsprites.add(player)
# ocean_sprites.add(oceanplayer)
# allsprites.add(target)
#
# for i in range(11):
#     e = Enemy()
#     allsprites.add(enemy)
#     enemy.add(e)
    # l = OceanEnemy()
    # ocean_sprites.add(oceanenemy)
    # oceanenemy.add(l)
    # t = Target()
    # allsprites.add(target)
    # target.add(t)



game_over = True

Game_play = True
# Game loop
while Game_play:

    if game_over == True:
        start_screen()
        game_over = False
        allsprites = pygame.sprite.Group()
        enemy = pygame.sprite.Group()
        lasers = pygame.sprite.Group()
        player = Player_1()
        allsprites.add(player)
        score = 0
        for i in range(11):
            e = Enemy()
            allsprites.add(enemy)
            enemy.add(e)

    # elif game_over == True:
    #     start_screen()
    #     game_over = False
    #     allsprites = pygame.sprite.Group()
    #     enemy = pygame.sprite.Group()
    #     player = OceanPlayer_1()
    #     allsprites.add(oceanplayer)
    #     score = 0
    #     for i in range(11):
    #         l = OceanEnemy()
    #         allsprites.add(oceanenemy)
    #         oceanenemy.add(l)

    # keep loop running at the right speed
    # clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            Game_play = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.attack()

        if event.type == pygame.KEYDOWN:
            # activate the cooresponding speeds
            # when an arrow key is pressed down
            if event.key == KEY_LEFT:
                player.speedx = -4
            elif event.key == KEY_RIGHT:
                player.speedx = 4
        if event.type == pygame.KEYUP:
            # deactivate the cooresponding speeds
            # when an arrow key is released
            if event.key == KEY_LEFT:
                player.speedx = 0
            elif event.key == KEY_RIGHT:
                player.speedx = 0


    # Update
    allsprites.update()   #updating sprites

    #check to see if player attack hits enemy,
    #collide sprite groups, group of lasers and group of enemy
    collide_laser = pygame.sprite.groupcollide(lasers, enemy, True, True)
    # collide_target = pygame.sprite.groupcollide(target, enemy, True, True)

    #when you collide with enemy the for statement repopulates enemy
    for i in collide_laser:
        enemysound1.play()
        score += 1
        e = Enemy()
        allsprites.add(e)
        enemy.add(e)
        # l = OceanEnemy()
        # ocean_sprites.add(oceanenemy)
        # oceanenemy.add(l)


    #checks if player and enemy collides, collide sprite with group
    collide = pygame.sprite.spritecollide(player, enemy, True)
    for i in collide:
        player.shield -= 10
        if player.shield <= 0:
            game_over = True



    for i in collide:
        e = Enemy()
        allsprites.add(e)
        enemy.add(e)
        # l = OceanEnemy()
        # ocean_sprites.add(oceanenemy)
        # oceanenemy.add(l)


    # Draw / render
    screen.blit(background, background_rect)
    allsprites.draw(screen)

    # draw_health(screen, 5, 5, player.shield)

    text(screen,"Health:" + str(player.shield), 27, 100, 10)

    text(screen,str(score), 27, 450, 10)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
