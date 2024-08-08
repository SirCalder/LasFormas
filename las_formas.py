#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, SetPen
from std_srvs.srv import Empty
from math import pi, sin, cos, radians
import random

def set_random_pen_color():
    rospy.wait_for_service('turtle1/set_pen')
    try:
        set_pen = rospy.ServiceProxy('turtle1/set_pen', SetPen)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        width = 3  
        set_pen(r, g, b, width, 0)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)



def draw_square(pub):
    
    side = 4.0
    rate = rospy.Rate(0.5)  
    move_cmd = Twist()

    for i in range(5):
        set_random_pen_color()
        move_cmd.linear.x = side
        move_cmd.angular.z = 0
        pub.publish(move_cmd)
        rate.sleep()

        move_cmd.linear.x = 0
        move_cmd.angular.z = pi / 2.01
        pub.publish(move_cmd)
        rate.sleep()

def draw_pentagon(pub):
    side = 2
    rate = rospy.Rate(0.5)
    move_cmd = Twist()

    for i in range(5):
        set_random_pen_color()
        move_cmd.linear.x = side
        move_cmd.angular.z = 0
        pub.publish(move_cmd)
        rate.sleep()

        move_cmd.linear.x = 0
        move_cmd.angular.z = pi / 2.50
        pub.publish(move_cmd)
        rate.sleep()

def draw_hexagon(pub):
    side = 2
    rate = rospy.Rate(0.5)
    move_cmd = Twist()

    for i in range(6):
        set_random_pen_color()
        move_cmd.linear.x = side
        move_cmd.angular.z = 0
        pub.publish(move_cmd)
        rate.sleep()

        move_cmd.linear.x = 0
        move_cmd.angular.z = pi / 3.0
        pub.publish(move_cmd)
        rate.sleep()
    

def draw_triangle(pub):
    
    side = 4.0
    rate = rospy.Rate(0.5)
    move_cmd = Twist()

    for i in range(3):
        set_random_pen_color()
        move_cmd.linear.x = side
        move_cmd.angular.z = 0
        pub.publish(move_cmd)
        rate.sleep()


        move_cmd.linear.x = 0
        move_cmd.angular.z = 2 * pi / 3.01
        pub.publish(move_cmd)
        rate.sleep()



def draw_circle(pub):
    set_random_pen_color()
    rate = rospy.Rate(30)
    move_cmd = Twist()
    move_cmd.linear.x = 2.0
    move_cmd.angular.z = 1.0

    for i in range(360): 
        #set_random_pen_color()
        pub.publish(move_cmd)
        rate.sleep()

def draw_star(pub):
    angle = 144  
    side = 4.0
    points = 5
    rate = rospy.Rate(0.5)  
    move_cmd = Twist()

    for i in range(points):

        set_random_pen_color()
        move_cmd.linear.x = side
        move_cmd.angular.z = 0
        pub.publish(move_cmd)
        rate.sleep()

        move_cmd.linear.x = 0
        move_cmd.angular.z = angle * pi / 180
        pub.publish(move_cmd)
        rate.sleep()



def draw_heart(pub):
    set_random_pen_color()
    rate = rospy.Rate(20)
    move_cmd = Twist()
    
    scale = 0.1  
    center_x = 5.5  
    center_y = 5.5  

    
    for degree in range(0, 361):
        #set_random_pen_color()
        angle = radians(degree)
        x = 16 * sin(angle)**3
        y = 13 * cos(angle) - 5 * cos(2 * angle) - 2 * cos(3 * angle) - cos(4 * angle)
        
        #escala e posição na janela
        x = x * scale + center_x
        y = y * scale + center_y

        #serviço de teletransporte para colocar a tartaruga nas coordenadas x, y calculadas
        try:
            teleport = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
            teleport(x, y, 0)
        except rospy.ServiceException as e:
            rospy.logerr("Service call failed: %s" % e)
        
        rate.sleep()


#limpar o fundo
def clear_background():
    rospy.wait_for_service('clear')
    try:
        clear = rospy.ServiceProxy('clear', Empty)
        clear()
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)


def draw_shape(shape):
    rospy.init_node('turtle_draw_shape', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    #teletransporta a tartaruga
    rospy.wait_for_service('turtle1/teleport_absolute')
    try:
        teleport = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
        teleport(5.5, 5.5, 0)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

    if shape == "quadrado":
        draw_square(pub)
    elif shape == "triangulo":
        draw_triangle(pub)
    elif shape == "circulo":
        draw_circle(pub)
    elif shape == "estrela":
        draw_star(pub)
    elif shape == "corazon":
        draw_heart(pub)
    elif shape == "pentagono":
        draw_pentagon(pub)
    elif shape == "hexagono":
        draw_hexagon(pub)

    elif shape == "limpar":
        clear_background()
    else:
        rospy.loginfo("não encontrado. Tente: quadrado, triangulo, circulo, estrela, limpar")

if __name__ == '__main__':
    while True:
        shape = input("Lista de formas:\nquadrado\ntriangulo\ncirculo\nestrela \nlimpar=limpar tela \nsair=encerrar: ").lower()
        if shape == 'sair':
            break
        draw_shape(shape)