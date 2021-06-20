# Build your comfort zone
# Program to build a house and a garden by few clicks
#   graphical interface.

from graphics import *


def main():
    win = GraphWin("", 1000, 750)
    win.setCoords(0.0, 0.0, 10.0, 7.5)
    win.setBackground('sky blue')

    # Bottom left corner of wall(first click)
    bottom_left_corner_of_wall = win.getMouse()

    # Upper right corner of wall(second click)
    upper_right_corner_of_wall = win.getMouse()


    # Draw the wall
    Wall = Rectangle(Point(bottom_left_corner_of_wall.getX(),
                     bottom_left_corner_of_wall.getY()),
              Point(upper_right_corner_of_wall.getX(),
                    upper_right_corner_of_wall.getY()))
    Wall.setFill(color_rgb(255,255,153))
    Wall.setOutline(color_rgb(255,255,153))
    Wall.draw(win)

    # Top of middle of door(third click)
    top_of_middle_of_door = win.getMouse()

    # Building the door
    Door = Rectangle(Point(top_of_middle_of_door.getX()- (upper_right_corner_of_wall.getX()-bottom_left_corner_of_wall.getX())/16,
                     bottom_left_corner_of_wall.getY()),
                        Point(top_of_middle_of_door.getX()+(upper_right_corner_of_wall.getX()-bottom_left_corner_of_wall.getX())/16,
                            top_of_middle_of_door.getY()))
    Door.setFill(color_rgb(80,25,0))
    Door.setOutline(color_rgb(80,25,0))
    Door.draw(win)

    # Planting grass (default)

    Grass_1 = Rectangle(Point(0, 0),
                      Point(10, bottom_left_corner_of_wall.getY()))
    Grass_1.setFill(color_rgb(0,204,0))
    Grass_1.setOutline(color_rgb(0,204,0))
    Grass_1.draw(win)

    Grass_2 = Rectangle(Point(0,bottom_left_corner_of_wall.getY()),Point(bottom_left_corner_of_wall.getX(),top_of_middle_of_door.getY()))
    Grass_2.setFill(color_rgb(0,204,0))
    Grass_2.setOutline(color_rgb(0,204,0))
    Grass_2.draw(win)

    Grass_3 = Rectangle(Point(upper_right_corner_of_wall.getX(),bottom_left_corner_of_wall.getY()),
                        Point(10,top_of_middle_of_door.getY()))
    Grass_3.setFill(color_rgb(0,204,0))
    Grass_3.setOutline(color_rgb(0,204,0))
    Grass_3.draw(win)

    # Building the Corridor (default)

    Corridor = Rectangle(Point(top_of_middle_of_door.getX()- (upper_right_corner_of_wall.getX()-bottom_left_corner_of_wall.getX())/16,
                    0),
                        Point(top_of_middle_of_door.getX()+(upper_right_corner_of_wall.getX()-bottom_left_corner_of_wall.getX())/16,
                             bottom_left_corner_of_wall.getY()))
    Corridor.setFill(color_rgb(192,192,192))
    Corridor.setOutline(color_rgb(192,192,192))
    Corridor.draw(win)

    # Top of middle of window(forth click)
    top_of_middle_of_window = win.getMouse()

    # Building the window

    Window = Rectangle(Point(top_of_middle_of_window.getX()-(top_of_middle_of_door.getX()+(upper_right_corner_of_wall.getX()-bottom_left_corner_of_wall.getX())/16-
                     top_of_middle_of_door.getX()- (upper_right_corner_of_wall.getX()-bottom_left_corner_of_wall.getX())/8),
                        top_of_middle_of_window.getY()-0.5),
                            Point(top_of_middle_of_window.getX()+(top_of_middle_of_door.getX()+(upper_right_corner_of_wall.getX()-bottom_left_corner_of_wall.getX())/16-
                                 top_of_middle_of_door.getX()- (upper_right_corner_of_wall.getX()-bottom_left_corner_of_wall.getX())/8),
                                    top_of_middle_of_window.getY()))
    Window.setFill((color_rgb(224,224,224)))
    Window.setOutline(color_rgb(224,224,224))
    Window.draw(win)

    # Top corner of roof (fifth click)
    top_corner_of_roof = win.getMouse()

    # Building the Roof
    Roof = Polygon(Point(bottom_left_corner_of_wall.getX(),upper_right_corner_of_wall.getY()),
            Point(top_corner_of_roof.getX(), top_corner_of_roof.getY()),
                Point(upper_right_corner_of_wall.getX(), upper_right_corner_of_wall.getY()))
    Roof.setFill(color_rgb(102,51,0))
    Roof.setOutline(color_rgb(102,51,0))
    Roof.draw(win)

    win.getMouse()
    win.close()



main()

