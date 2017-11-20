import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame import locals
pygame.joystick.init()
pygame.joystick.Joystick(0).init()
vertices=((1,-1,-1),
(1,1,-1),
(-1,1,-1),
(-1,-1,-1),
(1,-1,1),
(1,1,1),
(-1,-1,1),
(-1,1,1)
)

edges = (
(0,1),
(0,3),
(0,4),
(2,1),
(2,3),
(2,7),
(6,3),
(6,4),
(6,7),
(5,1),
(5,4),
(5,7)
)
color=(
	(1,0,0),
(0,0,1),
(0,1,0),
(1,0,0),
(1,1,0),
(0,1,1),
(1,0,1),
(0,0,1),
(0,1,0),
(1,0,0),
(1,1,0),
(0,1,1),
(1,0,1)
)


surfaces =(
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2),
	(4,0,3,6)
)

def cube():

	glBegin(GL_QUADS)
	for surface in surfaces:
		x=0
		for vertex in surface:
			#glColor3fv(color[x])
			glVertex3fv(vertices[vertex])
			x = x + 1
			glColor3fv(color[x])
	glEnd()


	glBegin(GL_LINES)
	for edge in edges:
			x=0
			for vertex in edge:
				glVertex3fv(vertices[vertex])
				x = x + 2
				glColor3f(0,0,0)
	glEnd()



def main():

	pygame.init()
	display=(1000,800)
	pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
	gluPerspective(50,1,1,300)
	glTranslatef(0,0,-20)

	x_c=0
	y_c=0
	x=0
	y=0
	while True:
		glRotate(4, y_c, x_c, 0.0);
		#glTranslatef(y_c,x_c,1)
		#glPopMatrix();

		for event in pygame.event.get():
			#glPushMatrix();

			x_c=(pygame.joystick.Joystick(0).get_axis(0)*30)
			y_c=(pygame.joystick.Joystick(0).get_axis(1)*30)
			#while(pygame.locals.JOYAXISMOTION):
			x_m=(pygame.joystick.Joystick(0).get_axis(2)*0.3)
			y_m=(pygame.joystick.Joystick(0).get_axis(3)*0.3)


			#glPopMatrix();

			#glRotated(1,x_c,y_c,0)
			print(x_c)
			print(y_c)

			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
		glTranslatef(x_m, y_m, 0)
		#glTranslatef(0.0,0.0,-6)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		cube()
		pygame.display.flip()
		pygame.time.wait(100)

main()






