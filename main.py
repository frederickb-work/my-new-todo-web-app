import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")


for item in todos:
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.remove(item)
        functions.write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()


st.text_input(label=" ",
              placeholder="What do you want to work on today? ",
              on_change=add_todo, key="new_todo")


