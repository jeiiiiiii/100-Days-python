# from turtle import Turtle, Screen
#
# move = 2
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
#
# timmy.color("darkblue")
# timmy.forward(100 * move )
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

pokemon = "Pokemon Name"

table.add_column(pokemon,["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

table.align = "l"


print(table)