import random
import turtle as t

track = t.Screen()
track.setup(width=1.0, height=1.0)

ninjas = []
colors = ["#4289CD","#844C9C","#ED1F24","#F8861C"]
names = ["leonardo","donatello","raphael","michelangelo"]

# Making turtle objects
for ninja_index in range(0,4):
    ninja = t.Turtle(shape="turtle")
    ninja.color(colors[ninja_index])
    ninja.name = names[ninja_index]
    ninja.penup()
    ninja.goto(-730, 150-(100*ninja_index))
    ninja.speed(1)
    ninjas.append(ninja)

# Drawing Finish line
finish = t.Turtle()
finish.pu()
finish.goto(480,250)
finish.pd()
finish.right(90)
finish.forward(500)


# Race
race_on = True
while race_on:
    for ninja in ninjas:
        ninja.forward(random.randint(0,20))
        if ninja.xcor()>460:
            winner = ninja.name
            race_on = False
            break

print(f"Winner is {winner}")


track.exitonclick()