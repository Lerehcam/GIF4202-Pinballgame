import pygame, constants

# ball = pygame.transform.scale(pygame.image.load("img/ball.png"),(40,40))
menu = pygame.transform.scale(pygame.image.load("serialPinball/img/menu.png"),(constants.gameW,constants.gameH))
playButton = pygame.transform.scale(pygame.image.load("serialPinball/img/playbutton.png"),(int(0.3*703),int(0.3*212)))
gameOver = pygame.transform.scale(pygame.image.load("serialPinball/img/GAMEOVER.png"),(constants.gameW,constants.gameH))

brick = pygame.transform.scale(pygame.image.load("serialPinball/img/redthingy.png"),(int(0.3*318),int(0.3*121)))
burst = pygame.transform.scale(pygame.image.load("serialPinball/img/blueburst.png"),(int(0.3*338),int(0.3*338)))
bumper = pygame.transform.scale(pygame.image.load("serialPinball/img/orangeface.png"),(int(0.3*128),int(0.3*128)))
button = pygame.transform.scale(pygame.image.load("serialPinball/img/button.png"),(int(0.3*254),int(0.3*300)))
plunger = pygame.transform.scale(pygame.image.load("serialPinball/img/startbouncything.png"),(20,60))
