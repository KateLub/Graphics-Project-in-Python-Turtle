from turtle import *

"""
This is Monishka's, Kate's, and Vivien's group project
"""
speed(0)
colormode(255)
'''
Monishka's code (drawing the land, sky, sun, rocks, grass shadows and flowers (bottom of code))
'''
#Draw the ground
def draw_land():
    penup()
    setposition(-200,-137)
    pendown()
    color((102, 204, 51))
    pensize(125)
    forward(399)
    penup()
    
#Draw one line of sky
def draw_sky(x,y,colour):
    setposition(x,y)
    pendown()
    pensize(80)
    color(colour)
    forward(399)
    penup()
    
#Call the functions 
draw_land()
#Draw complete sky
draw_sky(-200,-35,(218, 246, 255))
draw_sky(-200,30,(204, 245, 255))
draw_sky(-200,95,(179, 240, 255))
draw_sky(-200,160,(136, 218, 255))

#Draw the sun
penup()
#Set position to begin drawing
setposition(100,140)
pensize(2)
right(90)
#Change color and draw sun
color((255, 217, 102))
pendown()
begin_fill()
circle(40)
end_fill()

#Draw highlight on sun
left(15)
color((242, 220, 120))
begin_fill()
circle(30,301)
end_fill()

#Start drawing the grass
penup()
setposition(-175,-180)
pendown()
left(135)

#Draw a clump of grass
def draw_grass():
#First blade of grass in clump
    length = 10
    left(80)
    forward(length + 5)
    right(160)
    forward(15)
#2nd blade of grass in clump	
    left(160)
    forward(length + 15)
    right(160)
    forward(25)
#3rd blade of grass in clump	
    left(160)
    forward(length)
    right(160)
    forward(10)
#4th blade of grass in clump	
    left(160)
    forward(length + 5)
    right(160)
    forward(15)
    right(100)
    forward(20)
    right(180)
    
#Draw entire clump of grass	
for i in range(4):	
    color((108,171,53))
    begin_fill()
    draw_grass()
    end_fill()
    penup()
    forward(100)
    pendown()

#Draw the rocks
def draw_rocks():
#Draw 1st rock
    color((214,216,211))
    begin_fill()
    circle(10,180)
    end_fill()
    left(90)
    penup()
    forward(44)
    left(89)
#Draw second rock
    begin_fill()
    color((252,252,232))
    circle(13,180)
    end_fill()
    left(90)

#Draw the grass shadows
def grass_shadows(radius):
    begin_fill()
    circle(radius)
    end_fill()

import random
#Random positions for the grass shadows
for  i in range(2):
    x = random.uniform(-180,180)
    radius = random.randint(2,16)
    grass_shadows(radius)
    penup()
    setposition(x,-120)
    pendown()

#Random positions for rocks	
for  i in range(2):
    x = random.uniform(-180,180)
    y = random.randint(-150,-100)
    left(90)
    draw_rocks()
    penup()
    setposition(x,y)
    pendown()
left(1)
penup()

'''
Kate's code(large mountains with snow,green mountains, evergreen trees, and hills)
'''
#Draw the left half of an isoceles triangle
def draw_left_half_triangle(width,height,length, angle):
    pendown()
    begin_fill()
    #Left half of bottom of triangle
    forward(width)
    left(90)
    #Vertical side of triangle (height)
    forward(height)
    left(angle)
    #Drawing hypotenuse (slanted side) of triangle
    forward(length)
    end_fill()
    #Turn so that Tracey is facing East, and move forward to draw the right half of the isoceles triangle
    left((180-angle)+90)
    penup()
    forward(width)

#Draw the right half of the isoceles triangle
def draw_right_half_triangle( width, height, length, angle):
    pendown()
    begin_fill()
    #Right half of the bottom of the triangle
    forward(width)
    #Turning and drawing the hypotenuse (slanted side) of the triangle
    left(360 - (90 + angle))
    forward(length)
    #Turning and moving to draw the vertical side (height) of the triangle
    left(angle)
    forward(height)
    end_fill()
    #Turning, so that Tracey faces the correct direction no matter what she needs to draw next
    penup()
    left(90)
    
#Combining both sides to draw one single triangle, and assigning the sides colors
def draw_full_triangle(shadel_br_mount,shader_br_mount, width, height, length, angle):
    color(shadel_br_mount)
    draw_left_half_triangle(width,height,length, angle)
    color(shader_br_mount)
    draw_right_half_triangle(width,height,length, angle)

#Drawing the snow on the brown (3 big) mountains
def draw_snow(shadel_br_mount,shader_br_mount,shadel_snow,shader_snow,width,height,length,angle):
    #Draw a full triangle (the snow on mountain top)
    draw_full_triangle(shadel_snow,shader_snow,width,height,length,angle)
    #Move into place, to draw the triangular ridges in snow
    penup()
    backward(width)
    left(90)
    backward(1)
    right(90)
    pendown()
#Draw 2 ridges that are the same color as the left side of the mountain
    for i in range(2):
        #Color for ridges on left side of mountain
        color(shadel_br_mount)
        begin_fill()
        #Code to draw a triangle
        for i in range(3):
            forward(width/2)
            left(120)
        end_fill()
        #Move forward to draw next 
        forward(width/2)
    pendown()
    
#Draw 2 ridges that are the same color as the right side of the mountain
    for i in range(2):
        #Color for the right side of mountain
        color(shader_br_mount)
        begin_fill()
        #Code to draw a triangle
        for i in range(3):
            forward(width/2)
            left(120)
        forward(width/2)
        end_fill()
    penup()

#Draw the big brown mountains together with the snow        
def draw_brown_mountains():
    #Draw center mountain
    setposition(-65, -75) 
    draw_full_triangle((181,136,136),(168,126,126), 65, 215, 224.6, 163.18)
    #Draw snow on center mountain
    setposition(-24.5,58.5)
    draw_snow((181,136,136),(168,126,126),(242,235,217),(219,207,188),24.6, 81.6,85.2,163.2)
    
    #Draw left mountain
    setposition(-140,-75)
    draw_full_triangle((181,136,136),(168,126,126),66.5, 190, 201.3, 160.7)
    #Draw snow on left mountain
    setposition(-90,69.5)
    draw_snow((181,136,136),(168,126,126),(238,232,213),(218,211,199),17,48.5,51.4,160.7)
    
    #Draw right mountain
    setposition(0, -75)
    draw_full_triangle((181,136,136),(168,126,126), 67, 185, 196.8, 160.1)
    #Draw snow on right mountain
    setposition(45.5, 50.5)
    draw_snow((181,136,136),(168,126,126),(242,233,225),(212,213,189), 22, 62, 65.8, 160.1)
    
#Draw the green mountains/trees in front of the brown mountains
def draw_green_mountains():
    #Draw 2nd green mountain
    setposition(-180,-75)
    draw_full_triangle((166,179,97),(150,168,69), 40,115,121.7,160.8)
    #Draw 1st green mountain
    setposition(-190,-75)
    draw_full_triangle((148,163,78),(125,147,61), 25, 105, 107.9, 166.6)
    #Draw 3rd green mountain
    setposition(-115, -75)
    draw_full_triangle((125,145,40),(142,157,69), 20, 105, 106.8, 169)
    #Draw 5th green mountain
    setposition(-85, -75)
    draw_full_triangle((164,182,72),(148,163,43), 35, 95, 101, 159.7)
    #Draw 4th green mountain
    setposition(-105, -75)
    draw_full_triangle((166,180,90),(148,167,56), 35, 120, 125, 163.7)
    #Draw 7th green mountain
    setposition(80, -75)
    draw_full_triangle((151,162,94),(132,146,61),30,105,109,164)
    #Draw 6th mountain
    setposition(45, -75)
    draw_full_triangle((155,167,96),(139,148,75),35,120,125,163.7)
    #Draw 8th mountain
    setposition(105, -75)
    draw_full_triangle((155,167,96),(139,148,75),35,125,129.8,164.3)

#Draw the right side of a christmas tree
def draw_right_evergreen(x,y,STARTING_VALUE, ENDING_VALUE, INCREMENT):
#Set position to draw the right side of a 'branch'(triangle) on the cristmans tree
    setposition(x,y)
    def draw_right_side_evergreen(length):
        forward(length/2)
        left(120)
        forward(length)
        right(30)
        backward(length)
        penup()
        #Moving to draw the next triangle/branch
        forward(length-7)
        right(90)
#Repeating the code to draw a triangle/branch, to draw the complete right side of the christmas tree
    for i in range(STARTING_VALUE, ENDING_VALUE, INCREMENT):
        #Filling out and drawing the branches of the christmas tree
        color('darkgreen')
        begin_fill()
        pendown()
        draw_right_side_evergreen(i)
        end_fill()
    left(180)
    
#Draw the left side of a christmas tree
def draw_left_evergreen(x,y,STARTING_VALUE,ENDING_VALUE,INCREMENT):
#Set position and draw a branch/triangle for the left side of an evergreen tree
    setposition(x,y)
    def draw_left_side_evergreen(length):
        forward(length/2)
        right(120)
        forward(length)
        left(30)
        backward(length)
        penup()
        #Moving to draw the next branch/triangle
        forward(length-7)
        left(90)
        
#Drawing the complete left side of the christams tree
    for i in range(STARTING_VALUE, ENDING_VALUE, INCREMENT):
        color('green')
        #Fill out and draw the entire left side of evergreen tree
        begin_fill()
        pendown()
        draw_left_side_evergreen(i)
        end_fill()
        
#Draw a complete evergreen tree        
def draw_full_evergreen(x,y,STARTING_VALUE,ENDING_VALUE,INCREMENT):
    penup()
    #Draw right side and then the left
    draw_right_evergreen(x,y,STARTING_VALUE,ENDING_VALUE,INCREMENT)
    draw_left_evergreen(x,y,STARTING_VALUE,ENDING_VALUE,INCREMENT)
    penup()
    left(180)
    
#Draw all of the evergreens
def draw_all_evergreens():
#Draw evergreens on left side of picture (going from the left, in the right direction)
    draw_full_evergreen(-120,-15, 24,0,-6)
    draw_full_evergreen(-100,-20, 24,0,-4)
    draw_full_evergreen(-80,-15,  27,1,-5)
    draw_full_evergreen(-70,-15,  25,0,-5)
    draw_full_evergreen(-50,-35,  26,0,-4)
    draw_full_evergreen(-40,-15,  24,0,-6)
#Draw the evergreens on the right side of picture (going from the center, to the right)
    draw_full_evergreen(76.5,-15, 20,0,-4)
    draw_full_evergreen(85,-25,   20,0,-6)
    draw_full_evergreen(100,-20,  24,0,-6)
    draw_full_evergreen(120,-20,  24,0,-7)
    draw_full_evergreen(130,-20,  25,0,-5)
    draw_full_evergreen(135,-20,  24,0,-7)
   
#Draw a hill
def draw_hill(shade_hill,x,radius):
    #Color for the hill/semi-circle
    color(shade_hill)
    penup()
    #Set position to start drawing hill
    setposition(x,-75)
    pendown()
    #Draw a filled-out semi-circle
    begin_fill()
    circle(radius,180)
    end_fill()
    right(180)
    
#Draw all of the hills behind the house
def draw_all_hills():
    left(90)
#The farthest layer of hills (before evergreens):
    draw_hill((67,160,45),195,25)
    draw_hill((67,160,45),175,70)
    draw_hill((67,160,45),10,85)
    draw_hill((67,160,45),-160,25)
    #Shadow on the 2nd hill
    draw_hill((62,145,29),155,60)
    #Shadow on the 3rd hill
    draw_hill((62,145,29),-20,70)
#Smaller hills, right behind the triangular and oval trees:
    draw_hill((104,199,58),180,20)
    draw_hill((104,199,58),170,40)
    draw_hill((104,199,58),130,25)
    draw_hill((78,163,39),100,35)
    draw_hill((82,169,54),-10,35)
    draw_hill((82,169,54),-60,20)
    draw_hill((104,199,58),-75,40)
    #Turn to face directly East
    right(90)

#Draw a cloud  
def draw_cloud(x,y,radius):
    #Setposition to draw cloud
    penup()
    setposition(x,y)
    pendown()
    #Set color
    color('white')
    begin_fill()
    #Drawing the uneven 'top' of cloud
    circle(radius,180)
    right(90)
    circle(radius - 2,180)
    right(190)
    circle(radius + 5,180)
    right(100)
    circle(radius + 4,180)
    end_fill()
    penup()
    #Turn to be ready to draw anything else
    left(20)

#Call functions
draw_brown_mountains()
draw_green_mountains()
draw_all_evergreens()
draw_all_hills()
#Random positions for clouds
for  i in range(5):
    x = random.uniform(-180,180)
    y = random.randint(60,170)
    radius = random.randint(5,10)
    draw_cloud(x,y,radius)
    penup()
'''
Vivien's code (triangular grass, triangular trees, oval trees, and house)
'''
speed(0)
#Draw oval trees at the front/on either side of the house
def draw_oval_tree(o_tree_radius, o_tree_x, o_tree_trunk_size):
    #Draw tree trunk
    penup()
    color((138, 92, 68))
    pensize(o_tree_trunk_size)
    setposition(o_tree_x, -73)
    pendown()
    left(90)
    forward(o_tree_radius+3.5)
    right(90)
    #Circle/Bottom part of the leaves 
    pensize(1)
    color((40, 116, 14 ))
    begin_fill()
    circle(o_tree_radius)
    end_fill()
    #Triangle/Top part of the leaves
    left(90)
    forward(o_tree_radius*1.5)
    right(90)
    begin_fill()
    forward(o_tree_radius*0.866)
    for i in range(3):
        left(120)
        forward(o_tree_radius*1.732)
    end_fill()
    #Highlight circle
    backward(o_tree_radius*0.866)
    left(90)
    backward(o_tree_radius*1.5)
    forward(o_tree_radius)
    left(90)
    forward(o_tree_radius/4)
    left(90)
    forward(o_tree_radius*0.75)
    left(90)
    color((62, 127, 34))
    begin_fill()
    circle(o_tree_radius*0.75)
    end_fill()
    #Highlight triangle
    begin_fill()
    left(90)
    forward(o_tree_radius*1.5)
    left(90)
    forward(o_tree_radius*0.5)
    right(120)
    forward(o_tree_radius*1.55)
    right(134)
    forward(o_tree_radius*1.8)
    right(286)
    end_fill()

def draw_t_tree_trunk(t_tree_x, t_tree_trunk_size, t_tree_trunk_length):
    penup()
    setposition(t_tree_x, -73)
    color((138, 92, 68))
    pensize(t_tree_trunk_size)
    pendown()
    left(90)
    forward(t_tree_trunk_length)
    right(90)
    pensize(1)

#draw the grass
def draw_triangle():
    color((63, 144, 26))
    penup()
    setposition(-200, -75)
    pendown()
    for i in range(52):
        begin_fill()
        for i in range(3):
            forward(7)
            left(120)
        end_fill()
        forward(8)

def draw_house_front_half():
    #Draw rectangle
    penup()
    setposition(-55, -75)
    color((207, 170, 128))
    pendown()
    begin_fill()
    for i in range(3):
        forward(67)
        left(90)
        forward(44)
        left(90)
    end_fill()
    #Draw Triangle
    begin_fill()
    right(44.6)
    forward(47)
    left(89.2)
    forward(47)
    left(135.4)
    end_fill()

#Draw the side of house
def draw_house_side():
    forward(67)
    color((138, 92, 68))
    begin_fill()
    for i in range(2):
        forward(67)
        right(90)
        forward(44)
        right(90)
    end_fill()

#Draw roof
def draw_roof():
    forward(67)
    color((185, 139, 95))
    begin_fill()
    for i in range(2):
        left(135.4)
        forward(50)
        left(44.6)
        forward(67)
    end_fill()
    #Draw the edge of roof
    penup()
    left(180)
    forward(134)
    pendown()
    begin_fill()
    forward(3)
    right(135.4)
    forward(49)
    right(90.8)
    forward(3)
    right(90.8)
    forward(47)
    end_fill()
    left(227)
#Move to draw next stripe
def next_stripe_setup():
    right(90)
    forward(8.375)
    left(90)

#This function draws the first half of the stripes on the front of the house
def draw_stripes1():
    #Set position
    penup()
    setposition(-46.625, -75)
    #Draw stripes
    color((202, 163, 124))
    pendown()
    forward(52)
    backward(52)
    next_stripe_setup()
    forward(60.25)
    backward(60.25)
    next_stripe_setup()
    forward(68.7)
    backward(68.7)
    next_stripe_setup()

#This function draws the stripes on the 2nd half of the front of the house & the stripes on the roof
def draw_stripes2(stripe_length):
    #This value sets the position to draw the next line
    setup_stripe_length = 67
    #Draw stripes of 2nd half of house and roof
    forward(stripe_length)
    right(90)
    color((173, 131, 91))
    forward(setup_stripe_length)
    backward(setup_stripe_length)
    left(90)
    color((202, 163, 124))
    backward(stripe_length)
    next_stripe_setup()
    
#This function draws stripes on side of house
def draw_stripes3():
    right(90)
    penup()
    setposition(12, -69.67)
    color((128, 88, 53))
    pendown()
    for i in range(2):
        forward(67)
        left(90)
        penup()
        forward(7.33)
        left(90)
        pendown()
        forward(67)
        right(90)
        penup()
        forward(7.33)
        right(90)
        pendown()
    forward(67)

#Draw stripes from wood on house
def draw_all_stripes():
    draw_stripes1()
    draw_stripes2(77)
    draw_stripes2(68.75)
    draw_stripes2(60.5)
    draw_stripes2(52.25)
    draw_stripes3()

#Draw chimney on the roof of house
def draw_chimney():
    penup()
    color((192, 196, 197))
    setposition(18, -9)
    pendown()
    begin_fill()
    for i in range(3):
        forward(10)
        left(90)
        forward(25)
        left(90)
    end_fill()
    #Draw "rim" of chimney
    color((163, 162, 162))
    pensize(5)
    forward(10)
    pensize(1)
    right(180)
#Draw door on front of house
def draw_door():
    penup()
    setposition(-29.875, -75)
    color((141, 102, 61))
    begin_fill()
    left(90)
    for i in range(2):
        forward(30)
        right(90)
        forward(16.75)
        right(90)
    end_fill()
    #Details on door
    penup()
    setposition(-26.875, -74)
    color((174, 132, 92))
    pendown()
    begin_fill()
    for i in range(2):
        forward(10.5)
        right(90)
        forward(10.75)
        right(90)
    end_fill()
    penup()
    setposition(-26.875, -59.5)
    pendown()
    begin_fill()
    for i in range(2):
        forward(10.5)
        right(90)
        forward(10.75)
        right(90)
    end_fill()
    #Doorknob
    penup()
    color((114, 80, 43))
    setposition(-18.125, -66)
    pendown()
    circle(0.5)
    penup()
    right(90)

#Draw window in form of circle
def draw_circle_window():
    #Outer circle
    penup()
    color((128, 94, 56))
    setposition(-21.5, -30)
    begin_fill()
    circle(8.5)
    end_fill()
    #Inner circle
    setposition(-21.5, -28)
    color((79, 46, 30))
    begin_fill()
    circle(6.5)
    end_fill()
    #Draw cross
    penup()
    pensize(2)
    color((128, 94, 56))
    setposition(-21.5, -28)
    left(90)
    pendown()
    forward(14)
    penup()
    setposition(-28, -21.5)
    right(90)
    pendown()
    forward(14)
    pensize(1)

#Draw rectangular windows on the side of the house
def draw_side_windows():
    #1 window
    penup()
    setposition(26, -47)
    color((81, 73, 72))
    pendown()
    begin_fill()
    for i in range(4):
        forward(14)
        right(90)
    end_fill()
    penup()
    forward(2)
    right(90)
    forward(2)
    left(90)
    color((163, 228, 255))
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()
    setposition(33, -48)
    color((81, 73, 72))
    pensize(2)
    pendown()
    right(90)
    forward(12)
    pensize(1)
    penup()
    left(90)
    #2 window
    penup()
    setposition(54, -47)
    color((81, 73, 72))
    pendown()
    begin_fill()
    for i in range(4):
        forward(14)
        right(90)
    end_fill()
    penup()
    forward(2)
    right(90)
    forward(2)
    left(90)
    color((163, 228, 255))
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()
    setposition(61, -48)
    color((81, 73, 72))
    pensize(2)
    pendown()
    right(90)
    forward(12)
    pensize(1)
    left(90)
    penup()

#Call functions
#Draw 1st triangular tree (counting from the right)
draw_t_tree_trunk(172, 3, 12)
backward(10)
draw_full_triangle((61, 111, 39), (32, 92, 17), 10, 30, 31.62, 161.56)
#2nd triangular tree
draw_t_tree_trunk(145, 5, 8)
backward(15)
draw_full_triangle((61, 111, 39), (32, 92, 17), 15, 60, 61.85, 165.96)
#3rd triangular tree
draw_t_tree_trunk(121, 3, 10)
backward(7)
draw_full_triangle((61, 111, 39), (32, 92, 17), 7, 50, 50.49, 172.01)
#4th triangular tree
draw_t_tree_trunk(-110, 5, 9)
backward(15)
draw_full_triangle((61, 111, 39), (32, 92, 17), 15, 50, 52.2, 163.3)
#5th triangular tree
draw_t_tree_trunk(-150, 5, 11)
backward(15)
draw_full_triangle((61, 111, 39), (32, 92, 17), 15, 75, 76.49, 168.69)

#Draw trees with an oval-like shape of leaves
draw_oval_tree(5, 185, 2)
draw_oval_tree(5, 106, 2)
draw_oval_tree(7, 92, 2.5)
draw_oval_tree(7, -70, 2.5)
draw_oval_tree(9, -95, 3)
draw_oval_tree(9, -180, 3)

#Draw complete house
draw_triangle()
draw_house_front_half()
draw_house_side()
draw_roof()
draw_all_stripes()
draw_chimney()
draw_door()
draw_circle_window()
draw_side_windows()

'''
Code to draw flowers (written by Monishka)
'''
#Draw the flowers
def draw_stem():
    left(90)
    color((108,171,53))
    forward(15)
def draw_petals():
    for i in range(6):
        begin_fill()
        circle(4)
        left(60)
        end_fill()
def draw_centre():
    left(90)
    backward(2)
    right(90)
    begin_fill()
    color("yellow")
    circle(2)
    end_fill()
    penup()
#Draw 3 flowers together
def draw_3_flowers(shade_flowers):
    pendown()
    for i in range(3):
        draw_stem()
        color(shade_flowers)
        draw_petals()
        draw_centre()
        backward(15)
        right(90)
        forward(15)
        pendown()
    penup()
#Draw pink flowers    
penup()
setposition(105,-180)
draw_3_flowers('pink')
#Draw aqua-colored flowers    
setposition(-160,-120)
draw_3_flowers((0, 230, 230))
done()