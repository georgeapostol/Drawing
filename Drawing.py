from swampy.World import World


class Point(object):
    """
    this is a point in a given plane
    """


class Timmy(object):   #I named my rectangle Timmy
    """
    this is a rectangle
    """


class Fido(object):    #I like naming shapes, Fido is a circle
    """
    This is a shape with no corners
   """

world = World()


canvas = world.ca(width=1000, height=1000, background='gold') #hell yeah for gold
bbox = [[-150, -100], [150, 100]]
canvas.rectangle(bbox, outline='black', width=2, fill='mediumturquoise')


def draw_timmy(window, box, color):
    left_low = box.corner
    right_high = Point()
    right_high.x = box.corner.x + box.width
    right_high.y = box.corner.y + box.height
    bbox = [[left_low.x, left_low.y], [right_high.x, right_high.y]]
    window.rectangle(bbox, outline='black', width=2, fill=color)

def create_circle(x, y, z):
    c = Fido()
    c.center = Point()
    c.center.x = x
    c.center.y = y
    c.z = z
    return c
def draw_circle(win, c, color):
    win.circle([c.center.x, c.center.y], c.z, outline=None, fill=color)


r = Timmy()
r.width = 250
r.height = 200
r.corner = Point()
r.corner.x = -450
r.corner.y = -30

draw_timmy(canvas, r, 'moccasin')


circle_one = create_circle(-25, 74, 75)
circle_two = create_circle(-150, 0, 35)
circle_three = create_circle(750, -200, 22)

draw_circle(canvas, circle_one, 'grey')
draw_circle(canvas, circle_two, 'peru')
draw_circle(canvas, circle_three, 'limegreen')


r = Timmy()
r.width = 250
r.height = 200
r.corner = Point()
r.corner.x = -750
r.corner.y = -30

draw_timmy(canvas, r, 'moccasin')


def draw_point(window, point):
    window.circle([point.x, point.y], 15, outline=None, fill='black')


p1 = Point()
p1.x = 0
p1.y = 0


p2 = Point()
p2.x = 150
p2.y = 100
draw_point(canvas, p1)
draw_point(canvas, p2)




world.mainloop()
