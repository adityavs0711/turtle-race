import turtle as t
import random
is_race_on = False
screen = t.Screen()
screen.setup(height=600, width=800)
user_bet = screen.textinput(title="Make you guess.", prompt="Which turtle will win the race? \n"
                                                            "Enter a color: (red/orange/yellow/green/blue/purple)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
winner = ""
if user_bet:
    is_race_on = True

for i in range(0, 6):
    new_turtle = t.Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.setposition(x=-380, y=i * 50 - 125)
    turtle_list.append(new_turtle)

while is_race_on:
    distance = random.randint(0, 10)
    random_turtle = random.choice(turtle_list)
    random_turtle.forward(distance)
    if random_turtle.xcor() > 360:
        is_race_on = False
        winner = random_turtle.pencolor()

if user_bet.lower() == winner:
    print("You won!")
else:
    print(f"You lose. {winner} is the winner.")

screen.exitonclick()
