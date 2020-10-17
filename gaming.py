import pygame
import random
pygame.init()

window  = pygame.display.set_mode((500,500)) # e command tho screen display aytadi with (500 width, 800 height)


pygame.display.set_caption("Vinshoot")


screenwidth = 500
  


x = 250
y = 420
#x1 = 450
#y1 = 10
width = 40
height = 40
velocity = 80


background = pygame.image.load('R6.png')
pygame.display.set_icon(background)

car = pygame.image.load("R6.png")  # iikada load chestunam mana transformer image ni hero gadni(loading transformer image)
caar = car.get_rect()

enemy_size = 20
enemy_pos = [random.randint(400,450),10]
clock = pygame.time.Clock()  # ee command vala enemy melaga padtadu ledaa chala speed ga padtadu(boxes are dropping slowly)



run = True

 

 # while chala avasram because mana condition true unantha varaku screen display chestadi

while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		

	keys = pygame.key.get_pressed()


	if keys[pygame.K_LEFT] and caar.x > 0:
		caar.x = caar.x- velocity

	if keys[pygame.K_RIGHT] and caar.x < 500 - width:
		caar.x = caar.x + velocity

	if keys[pygame.K_UP] and caar.y > 0:
		caar.y = caar.y - velocity


	if keys[pygame.K_DOWN] and caar.y <500- width -20:
		caar.y = caar.y + velocity

	window.fill((66,245,206))



	window.blit(car,caar)
	if enemy_pos[1] >= 0 and enemy_pos[1] < 500:
		enemy_pos[1] += 10
	else:
		enemy_pos[1] = 0

	clock.tick(1) #ikada exceute chestam 1 frame per second

	
	pygame.draw.rect(window,(247,7,7),(enemy_pos[0],enemy_pos[1],width,height))


	pygame.display.update()


pygame.quit()


