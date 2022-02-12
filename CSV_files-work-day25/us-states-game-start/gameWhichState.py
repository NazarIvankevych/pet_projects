# !todo: Need to add user and he must answer on question about states. After he correct, this state must show on the
# map and continue input new values.
# Also we must count answers from 1 to 50.

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# Get click of mouse on the map
# def get_mouse_click_coor(x,y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

guessed_states = []
# Create the while loop to repeat all time answers from user
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct ",
                                    prompt="What`s another state`s name?").title()
    # Exit from game if user want
    if answer_state == 'Exit':
        # Use list-comprehension for better and shorter way
        missing_states = [state for state in all_states if state not in guessed_states]
        wrong_answer = pandas.DataFrame(missing_states)
        wrong_answer.to_csv("learn_states.csv")
        break

    # Check if a user is right and put turtle on the coordinates
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
