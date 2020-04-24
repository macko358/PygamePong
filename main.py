# Import the pygame library and initialise the game engine
import pygame
import time
import sys
from paddle import Paddle
from ball import Ball

pygame.init()

pygame.font.get_fonts()
pygame.mixer.pre_init(44100, -16, 1, 512)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SILVER = (105, 105, 105)

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong: by Marco Gava!")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 0
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 690
paddleB.rect.y = 200

ball = Ball(RED, 20, 20)
ball.rect.x = 345
ball.rect.y = 195

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add the car to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Initialise player scores
scoreA = 0
scoreB = 0

counter = 0

pygame.mixer.music.load('Pong!.mp3')
image = pygame.image.load('PongSmall.jpg')
pygame.font.init()
myFont = pygame.font.SysFont('hooge 05_53', 65)
smallFont = pygame.font.SysFont('hooge 05_53', 20)
Space = pygame.font.SysFont('hooge 05_53', 17)
largeFont = pygame.font.SysFont('hooge 05_53', 85)
largerFont = pygame.font.SysFont('hooge 05_53', 120)


def pause():
    paused = True
    while paused:
        for event_pause in pygame.event.get():
            if event_pause.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event_pause.type == pygame.KEYDOWN:
                if event_pause.key == pygame.K_c:
                    paused = False
                elif event_pause.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.fill(BLACK)
        textSurface = largerFont.render('I I', False, (255, 255, 255))
        screen.blit(textSurface, (295, 45))
        textSurface = largeFont.render('PAUSED', False, (255, 255, 255))
        screen.blit(textSurface, (175, 160))
        pygame.draw.rect(screen, SILVER, (219, 280, 260, 60))
        textSurface = smallFont.render('PRESS C TO CONTINUE', False, (255, 255, 255))
        screen.blit(textSurface, (223, 300))

        pygame.display.update()


introOn = True
while introOn:
    screen.fill(BLACK)
    textSurface = myFont.render('PONG! 2020', False, (255, 255, 255))
    screen.blit(textSurface, (110, 25))
    textSurface = smallFont.render('By Marco Gava', False, (255, 255, 255))
    screen.blit(textSurface, (400, 85))
    textSurface = smallFont.render('PRESS P', False, (255, 255, 255))
    screen.blit(textSurface, (25, 225))
    textSurface = smallFont.render('TO PAUSE', False, (255, 255, 255))
    screen.blit(textSurface, (25, 249))
    pygame.draw.rect(screen, SILVER, (211, 380, 260, 60))
    textSurface = Space.render('[PRESS SPACE TO PLAY!]', False, (255, 255, 255))
    screen.blit(textSurface, (220, 403))
    screen.blit(image, (195, 130))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            pygame.quit()  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                pygame.quit()
        # User did something
        if event.type == pygame.KEYDOWN:  # If user clicked close
            if event.key == pygame.K_SPACE:
                introOn = False  # Flag that we are done so we exit this loop

countOn = True
while countOn:
    clock = pygame.time.Clock()

    counter, text = 3, '3'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('hooge 05_53', 150)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'PONG!'
        else:
            screen.fill((0, 0, 0))
            screen.blit(font.render(text, True, (255, 255, 255)), (100, 190))
            pygame.display.flip()
            clock.tick(60)
            if counter <= -1:
                countOn = False
                break
            continue

    pygame.display.update()

PLAYSOUNDEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PLAYSOUNDEVENT, 1000)
exitGame = 60

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                carryOn = False
            elif event.key == pygame.K_p:
                pause()


        elif event.type == PLAYSOUNDEVENT:
            exitGame -= 1
            if exitGame <= 0:
                carryOn = False


    # Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

        # --- Game logic should go here
    all_sprites_list.update()

    # Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
        ball.change_color((0, 255, 0))
        counter = 1
        # pygame.mixer.music.load('Pong!.mp3')
        pygame.mixer.music.play(0)

    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
        ball.change_color((0, 255, 0))
        counter = 1
        # pygame.mixer.music.load('Pong!.mp3')
        pygame.mixer.music.play(0)

    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
        ball.change_color((0, 255, 0))
        counter = 1
        # pygame.mixer.music.load('Pong!.mp3')
        pygame.mixer.music.play(0)

    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]
        ball.change_color((0, 255, 0))
        counter = 1
        # pygame.mixer.music.load('Pong!.mp3')
        pygame.mixer.music.play(0)

        # Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()
        counter = 1
        # pygame.mixer.music.load('Pong!.mp3')
        pygame.mixer.music.play(0)

    if counter > 0:
        counter += 1

    if counter > 10:
        ball.change_color((255, 0, 0))
        counter = 0

    # --- Drawing code should go here
    # First, clear the screen to black.
    screen.fill(BLACK)
    # Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)

    # Display scores:
    player = pygame.font.SysFont("hooge 05_53", 28)
    font = pygame.font.SysFont("hooge 05_53", 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (240, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))
    textSurface = player.render('P1', False, (255, 255, 255))
    screen.blit(textSurface, (85, 15))
    textSurface = player.render('P2', False, (255, 255, 255))
    screen.blit(textSurface, (575, 15))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


# Once we have exited the main program loop we can stop the game engine:
conclusionOn = True
while conclusionOn:
    screen.fill(BLACK)
    if scoreA > scoreB:
        textSurface = myFont.render('PLAYER 1 WINS!', False, (255, 255, 255))
        screen.blit(textSurface, (58, 200))
    elif scoreA < scoreB:
        textSurface = myFont.render('PLAYER 2 WINS!', False, (255, 255, 255))
        screen.blit(textSurface, (58, 200))
    else:
        textSurface = myFont.render('YOU DREW!', False, (255, 255, 255))
        screen.blit(textSurface, (150, 200))



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            pygame.quit()  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                pygame.quit()
        # User did something
        if event.type == pygame.KEYDOWN:  # If user clicked close
            if event.key == pygame.K_SPACE:
                conclusionOn = False  # Flag that we are done so we exit this loop


pygame.quit()
