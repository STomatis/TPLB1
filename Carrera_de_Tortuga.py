from turtle import *
import turtle
from random import randint
import random

def carreradetortuga():
    title("Carreta de Tortugas")
    mensaje = turtle.Turtle()
    mensaje.penup()
    mensaje.goto(-200,200)
    mensaje.write("Elige un Color de tortuga, un oponente y mira quién gana.¡Hora de correr!",font=20)
    speed(0)
    penup()
    #Dibujar marca en la pista
    goto(-140,140)

    #Ciclo para hacer el marcado de la pista Verticales
    for paso in range(16):
        write(paso, align="Center")
        right(90)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(90)
        forward(20)

    roja = turtle.Turtle()
    roja.color('red')
    roja.shape('turtle')

    roja.penup()
    roja.goto(-140,100)
    roja.pendown()

    verde = turtle.Turtle()
    verde.color('green')
    verde.shape('turtle')

    verde.penup()
    verde.goto(-140,70)
    verde.pendown()

    azul = turtle.Turtle()
    azul.color('blue')
    azul.shape('turtle')

    azul.penup()
    azul.goto(-140,40)
    azul.pendown()

    amarillo = turtle.Turtle()
    amarillo.color('yellow')
    amarillo.shape('turtle')

    amarillo.penup()
    amarillo.goto(-140,10)
    amarillo.pendown()

    #Ciclo para hacer el marcado de la pista Horizontales
    for turno in range(100):
        roja.forward(random.randint(1,5))
        verde.forward(random.randint(1,5))
        azul.forward(random.randint(1,5))
        amarillo.forward(random.randint(1,5))

    if roja.xcor()>verde.xcor() and roja.xcor()>azul.xcor() and roja.xcor()>amarillo.xcor():
        roja.write(" Gano la tortuga Roja")
    else:
        if verde.xcor()>azul.xcor() and verde.xcor()>amarillo.xcor():
            verde.write(" Gano la tortuga Verde")
        else: 
            if azul.xcor()>amarillo.xcor():
                azul.write(" Gano la tortuga Azul")
            else:
                amarillo.write(" Gano la tortuga Amarillo")            
