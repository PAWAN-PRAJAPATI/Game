import pygame
from pygame import locals


pygame.init()


pygame.joystick.init() # main joystick device system
pygame.joystick.init()
pygame.joystick.Joystick(0).init()

while 1:
	for e in pygame.event.get(): # iterate over event stack
		print ('event :pygame. ' + str(type))
		if e.type == pygame.locals.JOYAXISMOTION: # 7
			x , y = pygame.joystick.Joystick(0).get_axis(2), pygame.joystick.Joystick(0).get_axis(3)
			print ('x and y : ' + str(x) +' , '+ str(y))
		elif e.type == pygame.locals.JOYBALLMOTION: # 8
			print ('ball motion')
		elif e.type == pygame.locals.JOYHATMOTION: # 9
			print ('hat motion')
		elif e.type == pygame.locals.JOYBUTTONDOWN: # 10
			print ('button down')
		elif e.type == pygame.locals.JOYBUTTONUP: # 11
			print ('button up')
 #####