import turtle

# Initializing Turtle
screen = turtle.Screen()

user_input = input("What type of flower would you like? ")

# the function to call the type of flower needed
def draw_flower(t, flower_type, color, size):
    t.color(color)
    t.begin_fill()
    if flower_type == "dandelion":
        draw_dandelion(t, size)
    elif flower_type == "sunflower":
        draw_sunflower(t, size)
    elif flower_type == "tulip":
        draw_tulip(t, size)
    elif flower_type == "daisy":
        draw_daisy(t, size)
    elif flower_type == "lily":
        draw_lily(t, size)
    else:
        print("Unknown flower type: {flower_type}")
    t.end_fill()

def draw_dandelion(t, size):
    for _ in range(36):
        t.forward(size)
        t.left(70)

def draw_sunflower(t, size):
    for _ in range(36):
        t.forward(size)
        t.left(100)
        t.forward(size / 2)
        t.left(60)

def draw_tulip(t, size):
    t.left(90)
    t.forward(size)
    t.right(90)
    t.circle(size, 180)
    t.right(90)
    t.forward(size)

def draw_daisy(t, size):
    for _ in range(12):  #amt of petals
        t.penup()
        t.forward(size)
        t.pendown()
        t.left(45)  #angle for petal placement
        t.begin_fill()
        t.circle(size * 0.5, 90)  
        t.left(90)
        t.circle(size * 0.5, 90)  #petal shape
        t.end_fill()
        t.right(135)  
        t.penup()
        t.backward(size)
        t.left(360 / 12)  # Spacing petals around center
        t.pendown()

def draw_lily(t, size):
    for _ in range(6):
        t.circle(size, 60) 
        t.left(120)      
        t.circle(size, 60)  
        t.left(120)     
        t.penup()
        t.forward(size * 0.5) 
        t.left(60)            
        t.pendown()

# Main function to generate flowers based on user input
def generate_flowers(user_input):
    flower_types = ["dandelion", "sunflower", "tulip", "daisy", "lily"]
    tokens = user_input.lower().split()
    
    if len(tokens) < 3 or len(tokens) % 3 != 0:
        print("Invalid input format. Please use 'number flower_type color' format.")
        return

  # Tokenization part
    flowers = []
    
    i = 0
    while i < len(tokens):
        try:
            number_of_flowers = int(tokens[i])
        except ValueError:
            print("Invalid number: {tokens[i]}")
            return
        
        flower_type = tokens[i + 1]
        color = tokens[i + 2]

      #to check if the flower is part of the list
        if flower_type not in flower_types:
            print("Invalid flower type: {flower_type}. Available types are: {', '.join(flower_types)}.")
            return
        
        flowers.append((number_of_flowers, flower_type, color))
        i += 3

    t = turtle.Turtle()
    t.speed(20)
    
    # Start position
    t.penup()
    t.goto(-100, 50) 
    t.pendown()
    
    # Drawing logico
    for number_of_flowers, flower_type, color in flowers:
        for _ in range(number_of_flowers):
            draw_flower(t, flower_type, color, 50)
            t.penup()
            t.forward(100)  #spacing between
            t.pendown()
        
        # Moving to a new row after finishing
        t.penup()
        t.goto(-200, t.ycor() - 150)  # Move down
        t.pendown()
    
    t.hideturtle()
    screen.mainloop()

generate_flowers(user_input)
