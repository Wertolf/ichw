import turtle
import threading
import math
def move1(t,n,k,l):
    t.left((90*k)/n)
    t.forward(l)
def move2(t,i,j):
    t.left(i)
    t.forward(j)
def move3(t,x,y):
    t.goto(x,y)
def mercury():
    m = turtle.Turtle()
    m.shape("circle")
    m.color("blue")
    m.speed(0)
    m.up()
    m.goto(40,0)
    m.down()
    m.left(90)
    a,b = 40,35
    for x in range(40,-41,-5):
        y = math.sqrt(b**2-(b**2/a**2)*x**2)
        move3(m,x,y)
    for x in range(-40,41,5):
        y = math.sqrt(b**2-(b**2/a**2)*x**2)
        z = -y
        move3(m,x,z)
def venus():
    v = turtle.Turtle()
    v.shape("circle")
    v.color("green")
    v.speed(0)
    v.up()
    v.goto(80,0)
    v.down()
    v.left(90)
    a,b = 80,70
    for x in range(80,-81,-5):
        y = math.sqrt(b**2-(b**2/a**2)*x**2)
        move3(v,x,y)
    for x in range(-80,81,5):
        y = math.sqrt(b**2-(b**2/a**2)*x**2)
        z = -y
        move3(v,x,z)

def earth():
    e = turtle.Turtle()
    e.shape("circle")
    e.color("red")
    e.speed(0)
    e.up()
    e.goto(120,0)
    e.down()
    e.left(90)
    a,b = 120,90
    for x in range(120,-121,-5):
        y = math.sqrt(b**2-(b**2/a**2)*x**2)
        move3(e,x,y)
    for x in range(-120,121,5):
        y = math.sqrt(b**2-(b**2/a**2)*x**2)
        z = -y
        move3(e,x,z)
def mars():
    ma = turtle.Turtle()
    ma.shape("circle")
    ma.color("black")
    ma.speed(0)
    ma.up()
    ma.goto(160,0)
    ma.down()
    ma.left(90)
    a,b = 160,60
    for x in range(160,-161,-5):
        y = math.sqrt(b**2-(b**2/a**2)*x**2)
        move3(ma,x,y)
    for x in range(-160,161,5):
        y = math.sqrt(b**2-(b**2/a**2)*x**2)
        z = -y
        move3(ma,x,z)

def jupiter():
    j = turtle.Turtle()
    j.shape("circle")
    j.color("orange")
    j.speed(0)
    j.up()
    j.goto(200,0)
    j.down()
    j.left(90)
    a,b = 200,100
    for x in range(200,-201,-5):
        y = math.sqrt(b**2-(b**2/a**2)*x**2)
        move3(j,x,y)
    for x in range(-200,201,5):
        y = math.sqrt(b**2-(b**2/a**2)*x**2)
        z = -y
        move3(j,x,z)

def saturn():
    s = turtle.Turtle()
    s.shape("circle")
    s.color("hotpink")
    s.speed(0)
    s.up()
    s.goto(250,0)
    s.down()
    s.left(90)
    a,b = 250,90
    for x in range(250,-251,-5):
        y = math.sqrt(b**2-(b**2/a**2)*x**2)
        move3(s,x,y)
    for x in range(-250,251,5):
        y = math.sqrt(b**2-(b**2/a**2)*x**2)
        z = -y
        move3(s,x,z)
def main():
    wd = turtle.Screen()
    s = turtle.Turtle()
    s.shape("circle")
    s.color("yellow")
    threads = []
    t1 = threading.Thread(target=mercury)
    threads.append(t1)
    t2 = threading.Thread(target=venus)
    threads.append(t2)
    t3 = threading.Thread(target=earth)
    threads.append(t3)
    t4 = threading.Thread(target=mars)
    threads.append(t4)
    t5 = threading.Thread(target=jupiter)
    threads.append(t5)
    t6 = threading.Thread(target=saturn)
    threads.append(t6)
    for t in threads:
        t.setDaemon(True)
        t.start()
    #n = 150
    #for i in range(n): #let the planets start their show!
        #move1(m,n,12,5)
        #move1(v,n,8,6)
        #move1(e,n,7,7)
        #move1(ma,n,6,8)
        #move1(j,n,5,9)
        #move1(s,n,4,10)

    wd.exitonclick()
if __name__ =="__main__":
    main()
