import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
pygame.joystick.init()
pygame.joystick.Joystick(0).init()
vertices=[
    [0,0,0],
    [1,0,0],
    [2,0,0],
    [0,0,-6],
    [0,0,6],
    [6,0,0],
    [-6,0,0],
    [0,6,0],
    [0,-6,0]
]

edges=(
    (0,1),
    (1,2),
    (3,4),
    (5,6),
    (7,8)
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
    glTranslate(0,0,-100)
    theta=0
    theta1=0
    theta2=0
    mta=0
    k=1
    while k:

        for event in pygame.event.get():
            mx_c = -(pygame.joystick.Joystick(0).get_axis(0)*0.15)
            my_c =-(pygame.joystick.Joystick(0).get_axis(1)*0.15)
            z_c = (pygame.joystick.Joystick(0).get_axis(2)*0.14)
            w_c =(pygame.joystick.Joystick(0).get_axis(3)*0.14)
        x_c=w_c
        y_c=-0.99999*w_c
        x_c=x_c+mx_c
        y_c=y_c+mx_c+my_c
        if(k==0):
            glRotate(20, 45, 45, 45);
            k=1
        theta = (theta + (360)* x_c*0.001) % 360
        theta2 = (theta2 + (360) * z_c * 0.001) % 360
        theta1= (theta1 + (360)* (y_c)*0.001) % 360
        theta2=0

        vertices[1][0]=(2)**(1/2) * math.cos(theta)
        vertices[1][1]=(2)**(1/2) * math.sin(theta)
        d=((vertices[2][0]**2+vertices[2][1]**2)**(1/2))
        #vertices[2][0]=d*math.cos(theta)
        #vertices[2][1] = d * math.sin(theta)
        dis=(2)**(1/2)
        vertices[2][0]=vertices[1][0]+dis*math.cos(theta1+theta2)
        vertices[2][1]=vertices[1][1]+dis*math.sin(theta1)
        disz=((2)**(1/2))*math.cos(theta)
        vertices[1][0]=disz*math.cos(theta2)
        vertices[1][2] = disz * math.sin(theta2)

        #vertices[2][0]=2*math.cos(theta2+theta1)
        vertices[2][2] = 2 * math.sin(theta2)


        print(vertices[2][0],vertices[2][1])
        print(d)
        x=2
        y=2
        #if(vertices[2][0]/vertices[2][1]>x/y):
         #   k=0

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        line()
        pygame.display.flip()
        pygame.time.wait(100)

main()