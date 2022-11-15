##Spiderman Drawing in python

from turtle import *

speed(13) # Painting speed control
bgcolor("#990000")
pensize(10)
penup()
goto(0,50)
pendown()
circle(-120)
penup()
circle(-120,-60)
pendown()
pensize(5)
right(50)
circle(70,55)
right(85)
circle(75,58)
right(90)
circle(70,55)
right(90)
circle(70,58)

# body
penup()
pensize(10)
goto(80,15)
pendown()
seth(92)
fd(135)
seth(125)
circle(30,135)
seth(190)
fd(50)
seth(125)
circle(30,135)
seth(275)
fd(90)

# Arm 1
penup()
pensize(10)
goto(92,-150)
seth(240)
pendown()
fd(80)
left(10)
circle(-28,185)

# Arm 2
penup()
goto(0,50)
seth(0)
pensize(10)
circle(-120,-60)
seth(200)
pendown()
fd(72)
left(20)
circle(30,150)
left(20)
fd(20)
right(15)
fd(10)
pensize(5)
fillcolor("#3366cc")
begin_fill()
seth(92)
circle(-120,31)
seth(200)
fd(45)
left(90)
fd(52)
end_fill()
fd(-12)
right(90)
fd(40)
penup()
right(90)
fd(18)
pendown()
right(86)
fd(40)
penup()
goto(-152,-86)
pendown()
left(40)
circle(35,90)
# Body coloring
penup()
goto(-80,116)
seth(10)
pensize(5)
pendown()
begin_fill()
fillcolor("#3366cc")
fd(155)
seth(-88)
fd(37)
seth(195)
fd(156)
end_fill()
penup()
goto(-75,38)
seth(15)
pendown()
begin_fill()
fd(158)
seth(-88)
fd(55)
seth(140)
circle(120,78)
end_fill()
# Arm 1 To color
penup()
fillcolor("#3366cc")
pensize(5)
goto(75,-170)
pendown()
begin_fill()
seth(240)
fd(30)
right(90)
fd(17)
end_fill()
fd(10)
left(80)
fd(55)
penup()
left(90)
fd(15)
pendown()
left(85)
fd(55)
penup()
goto(43,-225)
left(84)
pendown()
circle(60,51)
speed(0)

# Body vertical lines
for i in range(3):
  penup()
  goto(-70+i*15,135)
  seth(-90)
  pendown()
  pensize(5)
  fd(15-2*i)

for i in range(3):
  penup()
  goto(36 + i * 15, 156)
  seth(-90)
  pendown()
  pensize(5)
  fd(15 - 2 * i)
  a = -60
  b = 70

for i in range(4):
  penup()
  goto(a,b)
  a=a+40
  b=b+10
  seth(-90)
  pendown()
  pensize(5)
  fd(26)

def oo (li,jing):
  penup()
  goto(0,50)
  seth(0)
  circle(-120, li)
  pendown()
  right(jing)
  pensize(5)
  oo(-60,110)
  fd(130)
  oo(-28,96)
  fd(140)
  oo(9,89)
  fd(144)
  oo(42,70)
  fd(160)
  oo(80,60)
  fd(130)
  penup()
  goto(-80,-40)
  right(160)
  pendown()
  right(50)
  circle(70,45)
  right(75)
  circle(70,38)
  right(50)
  circle(70,45)
  right(90)
  circle(70,48)
  penup()
  goto(-53,-70)
  pendown()
  left(40)
  circle(70,30)
  right(50)
  circle(70,20)
  right(50)
  circle(70,38)
  right(70)
  circle(70,24)
  penup()
  goto(-19,-105)
  left(72)
  pendown()
  fd(22)
  right(60)
  fd(22)
  oo(-140,80)
  circle(-90,120)
  penup()
  oo(140,100)
  circle(90,13)
  pendown()


right(-50)
circle(70,45)
right(75)
circle(70,38)
right(50)
circle(70,36)
penup()
goto(22,-185)
right(70)
pendown()
fd(72)
penup()
goto(-40,-182)
right(38)
pendown()
fd(70)
speed(10)
# The left eye
penup()
pensize(7)
goto(-15,-110)
seth(0)
pendown()
pensize(10)
begin_fill()
left(130)
fd(110)
right(250)
circle(90,60)
circle(40,120)
fillcolor("#F5FFFA")
end_fill()

# Right eye
penup()
goto(5,-110)
pendown()
begin_fill()
right(30)
fd(110)
right(-250)
circle(-90,60)
circle(-40,120)
end_fill()
done()