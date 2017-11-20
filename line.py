import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
pygame.joystick.init()
pygame.joystick.Joystick(0).init()
vertices=[
    [0,0,0],
    [1,1,0],
    [2,0,0]
]

edges=(
    (0,1),
    (1,2)
)

def line():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display=(1000,1000)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    gluPerspective(50,1,1,300)
    glTranslate(0,0,-10)
    theta=0
    theta1=0
    theta2=0
    while True:
        for event in pygame.event.get():
            x_c = -(pygame.joystick.Joystick(0).get_axis(0)*0.10)
            y_c =(pygame.joystick.Joystick(0).get_axis(1)*0.10)
            z_c = (pygame.joystick.Joystick(0).get_axis(2)*0.10)
        theta = (theta + (360)* x_c*0.001) % 360
        theta2 = (theta2 + (360) * z_c * 0.001) % 360
        theta1= (theta1 + (360)* (y_c)*0.001) % 360

        vertices[1][2]=vertices[1][2]+z_c
        vertices[1][2] = vertices[1][2] + z_c
        vertices[2][2] = vertices[2][2] + z_c
        vertices[2][2] = vertices[2][2] + z_c
            #y_c = (pygame.joystick.Joystick(0).get_axis(1) * 30)
        vertices[1][0]=(2)**(1/2) * math.cos(theta)
        vertices[1][1]=(2)**(1/2) * math.sin(theta)

        dis=(2)**(1/2)
        vertices[2][0]=vertices[1][0]+dis*math.cos(theta1+theta2)
        vertices[2][1]=vertices[1][1]+dis*math.sin(theta1)
        disz=((2)**(1/2))*math.cos(theta)
        vertices[1][0]=disz*math.cos(theta2)
        vertices[1][2] = disz * math.sin(theta2)

        #vertices[2][0]=2*math.cos(theta2+theta1)
        vertices[2][2] = 2 * math.sin(theta2)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        line()
        pygame.display.flip()
        pygame.time.wait(100)
        print(x_c,y_c,z_c)



main()