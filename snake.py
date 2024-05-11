import turtle
import time
import random

delay = 0.1
body_segments = [] 
score = 0
high_score = 0

windows = turtle.Screen()

#titulo
windows.title("Snake")
#tamaño de la ventana ancho y largo
windows.setup(width=600, height=600)
#color de pantalla
windows.bgcolor("light green")

#elementos para la cabeza
cabeza = turtle.Turtle()
#para que se quede fijo
cabeza.speed(0) #se queda fijo en esa posicion 
#shape para que tenga una forma
cabeza.shape('square')
#color de la cabeza
cabeza.color("green")
#para no dejar rastro de la animacion
cabeza.penup()
#posicion de la snake
cabeza.goto(0,0) #posicion 0,0
#direccion de snake
cabeza.direction = "stop"

#creando la comida para la serpiente
comida = turtle.Turtle()
comida.speed(0) 
comida.shape("circle")
comida.color("red") 
comida.penup() #para que no deje lineas
comida.goto(0,100) #donde se ubica la comida
comida.direction = "stop"

#score
texto = turtle.Turtle()
texto.speed(0)
texto.color("Black")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write(f'score {score}      high score {high_score}', align="center", font=("arial", 24))
def movimiento():
    if cabeza.direction == "up":
        #almacenar el valor actual de la coordenada y
        y = cabeza.ycor()
        cabeza.sety(y + 10)
        
    if cabeza.direction == "down":
        #almacenar el valor actual de la coordenada y
        y = cabeza.ycor()
        cabeza.sety(y - 10)
        
    if cabeza.direction == "right":
        #almacenar el valor actual de la coordenada x
        x = cabeza.xcor()
        cabeza.setx(x + 10)
        
    if cabeza.direction == "left":
        #almacenar el valor actual de la coordenada x
        x = cabeza.xcor()
        cabeza.setx(x - 10)
        
#ahora voy a hacer funciones para que el programa se conecte con el teclado

def DirUp():
    cabeza.direction = "up"
def DirDown():
    cabeza.direction = "down"
def DirRight():
    cabeza.direction = "right"
def DirLeft():
    cabeza.direction = "left"    


#conectar teclado
windows.listen()
windows.onkeypress(DirUp, "Up")   
windows.onkeypress(DirDown, "Down") 
windows.onkeypress(DirRight, "Right") 
windows.onkeypress(DirLeft, "Left") 

        
while True:
    windows.update()
    windows.listen()
    
    #colisiones con la ventana para que choque la serpiente con los bordes y se resetee el juego
    
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        
        #limpiar los segmentos de la serpiente
        for segment in body_segments:
            segment.goto(1000,1000) #para mandar los elementos afuera de la pantalla
    
        #aca si los limpia fuera del for
        body_segments.clear()
        texto.clear()
        texto.write(f'score {score}      high score {high_score}', align="center", font=("arial", 24))
        
        
    
    
    #un condicional para que la comida se desplaze en los rangos puestos (colisiones cabeza vs comida)
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x,y)
        
        #segmento
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0) #se queda fijo en esa posicion 
        nuevo_segmento.shape('square')
        nuevo_segmento.color("yellow")
        nuevo_segmento.penup()
        body_segments.append(nuevo_segmento)
        
        #reinicia los puntos
        score += 10
        if score > high_score:
            high_score = score
        
        texto.clear()
        texto.write(f'score {score}      high score {high_score}', align="center", font=("arial", 24))
    
    totalseg = len(body_segments)

    
    #ahora voy a hacer que los segmentos se peguen a la cola
    for i in range(totalseg - 1, 0, -1):
        x = body_segments[i - 1].xcor()
        y = body_segments[i - 1].ycor()
        body_segments[i].goto(x, y)
        
    if totalseg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        body_segments[0].goto(x, y)
        
    
    movimiento()    
    
    # Colisiones con la serpiente
    for segment in body_segments:
        if segment.distance(cabeza) < 10:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
        
        # Limpiar los segmentos de la serpiente
            for segment in body_segments:
               segment.goto(1000,1000)  # para mandar los elementos afuera de la pantalla
               
            body_segments.clear()
             
            score = 0
            texto.clear()
            texto.write(f'score {score}      high score {high_score}', align="center", font=("arial", 24))        
    

    time.sleep(delay) #para que vaya más lento