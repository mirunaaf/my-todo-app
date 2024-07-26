import streamlit as st
import functions

# Declare todos variable - Gets todo list from todos.txt
todos = functions.get_todos()

# Create a function that gets the user input value and adds it in the todo list
def add_todo():
    todo_toadd = st.session_state["new_todo"] + "\n"
    print(todo_toadd)
    todos.append(todo_toadd)
    functions.write_todos(todos)


# Return a title instance
st.title("My Todo App")

# Creates text
st.write("The app that will increase your productivity.")

for index, todo in enumerate(todos):
# Creates checkbox with the todos from the todos.txt
    checkbox = st.checkbox(todo, key=todo) #stores each checkbox in a variable
    if checkbox:
        # Remove the todo checked from the list
        todos.pop(index)
        functions.write_todos(todos)
        # Delete the pair selected(from session_state dictionary)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add a new todo:",
              on_change=add_todo, key='new_todo')


#visualize the updated session_state dictionary
#st.session_state