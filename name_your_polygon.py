import turtle

response = input("Hey stranger! Can you please tell me the number of sides, length of each side, line color and fill color for a polygon of your choice?")
response_list = response.split()

# assign your reponses to variables
sides = int(response_list[0])
length = int(response_list[1])
linecolor = response_list[2]
fillcolor = response_list[3]

# compute the interior angle of the polygon
angle = 180 - (((180*sides)-360) / sides)

# build your screen and turtle
screen = turtle.Screen()
polly = turtle.Turtle()
polly.shape()
polly.color(linecolor)
polly.fillcolor = (fillcolor)
polly.begin_fill()

# iterate over the number of sides
for side in range(sides):
    polly.forward(length)
    polly.left(angle)

polly.end_fill()
