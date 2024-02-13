import pygame, sys  # impordib pygame'i ja sys funktsiooni
pygame.init()   # initsialiseerib pygame

screenX = 640   # määrab ekraani x-telje suuruse
screenY = 480   # määrab ekraani y-telje suuruse
screen = pygame.display.set_mode([screenX, screenY])    # määrab ekraani display
pygame.display.set_caption("Ülesanne4")     # display nimetus
clock = pygame.time.Clock()     # initsialiseerib kella

bg = pygame.image.load("bg_rally.jpg")  # laeb taustapildi

red_car = pygame.image.load("f1_red.png")   # laeb punase auto
red_car = pygame.transform.scale(red_car, [45, 90])     # määrab auto suuruse
screen.blit(red_car, [300, 350])    # punase auto asukoha

blue_car = pygame.image.load("f1_blue.png")     # laeb sinise auto
blue_car = pygame.transform.scale(blue_car, [45, 90])   # määrab auto suuruse
screen.blit(blue_car, [170, 50])    # määrab auto asukoha

posX, posY = 0, 0   # taustapildi asukoht
speedY = 3  # tasuta kiirus
posX_blue, posY_blue = 170, 50  # sinise auto asukoht
speedY_blue = 2     # sinise auto kiirus

while True:     # et aken oleks piisavalt kaua lahti kuniks ise selle ristist kinni panen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    posY += speedY  # see kood liigutab tasutapilti ülespoole
    if posY >= screenY:
        posY = 0

    # kuvab tasutapilti ekraanil
    screen.blit(bg, (posX, posY))
    screen.blit(bg, (posX, posY - screenY))

    # kuvab punast autot ekraanil
    screen.blit(red_car, [300, 350])

    # kuvab sinist autot ekraanil
    screen.blit(blue_car, (posX_blue, posY_blue))
    screen.blit(blue_car, (posX_blue, posY_blue - screenY))

    pygame.display.flip()   # graafika kuvamine ekraanil

    # liigutab sinist autot alla ja algusesse, kui see on ekraanist väljas
    posY_blue += speedY_blue
    if posY_blue >= screenY:
        posY_blue = 0

    clock.tick(60)  # määrab fps'i

pygame.quit()