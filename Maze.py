import turtle

window = turtle.Screen()
window.bgcolor("black")
window.title("Maze")
window.setup(700,700)

#Buat pulpen
class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("white")
		self.penup()
		self.speed(0)

#Create level list
level = [""]

#define first level
level_1 = [
"11111111111",
"00001000001",
"11101011101",
"10001010001",
"10111010111",
"10100010001",
"10101010101",
"10101010101",
"10101010101",
"10001010100",
"11111111111"]

#Add maze to maze list
level.append(level_1)

#buat map
def setup_maze(level):
	for y in range(len(level)):
		for x in range(len(level[y])):
			character = level[y][x]
			#penentuan koordinat x dan y
			pos_x = -288 + (x * 24)
			pos_y = 288 - (y * 24)
			
			if character == "1":
				pen.goto(pos_x, pos_y)
				pen.stamp()
				
#buat instance class
pen = Pen()

setup_maze(level[1])

while True:
	pass