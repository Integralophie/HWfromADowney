import turtle
import math
bob = turtle.Turtle()
def polygon(n,r):
    for i in range(n):
        bob.fd(r)
        bob.lt(360/n)


#polygon(5,150)

def circle(t,r):
    for i in range(360):
        t.fd(2*math.pi*r/360)
        t.lt(1)


#circle(bob,100)

def arc(t,r,angle):
    for i in range(angle):
        t.fd(2*math.pi*r/360)
        t.lt(1)

#arc(bob,100,90)


def flowerblade(t,n,r):
# n is the number of step used to create one flower blade
# r is the radius of the flower
    for i in range(n):
        t.fd(2*math.pi*r/360)
        t.lt(1)
    t.lt(180-n)
    for i in range(n):
        t.fd(2*math.pi*r/360)
        t.lt(1)
#flowerblade(bob,50,100)

def flower(t,n,r,m):
    # m is the number of blades
    for i in range(m):
        flowerblade(t,n,r)
        ang = 360/m-180-n
        t.lt(ang)


#flower(bob,n=20,r=1000,m=10)


# to make the flower blades overlap, increase n value to increase the curvature of each arc
# decrease r value accordingly to avoid making the flower too big


def pies(t,n,r):
# n is the number of slices of the pie
# r is the length of the inner radius
    for i in range(n):
        pieceofpie(t,n,r)
        t.lt(180)

def pieceofpie(t,n,r):
    t.fd(r)
    t.lt((180-360/n)/2)
    t.fd(2*math.cos((180-360/n)/2)*r)
    t.lt((180-360/n)/2)
    t.fd(r)

pies(bob,5,100)
