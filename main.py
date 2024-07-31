import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "Blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")

# def write_state_name(state_name, x, y):
#     pen = turtle.Turtle()
#     pen.hideturtle()
#     pen.penup()
#     pen.goto(x, y)
#     pen.write(state_name, align="center", font=("Arial", 8, "normal"))


# state_list = data["state"].str.title().tolist()
all_states = df["state"].tolist()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # states_to_learn.csv
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states, columns=["Missing_States"])
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        """This uses boolean indexing to filter the DataFrame df. 
        It selects only the rows where the boolean Series is True. 
        Essentially, it returns a subset of df where the state name matches the answer_state."""
        state_date = df[df["state"] == answer_state]
        t.goto(state_date.x.item(), state_date.y.item())
        t.write(state_date["state"].item())

"""either leave here or under while loop both work the same"""
# states_to_learn.csv
# missing_states = []
# for state in all_states:
#     if state not in guessed_states:
#         missing_states.append(state)
# new_data = pandas.DataFrame(missing_states, columns=["Missing_States"])
# new_data.to_csv("states_to_learn.csv")


