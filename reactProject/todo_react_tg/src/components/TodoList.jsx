import React from 'react'
import TodoListItem from './TodoListItem'

const listStyle = {
    minHeight: "320px",
    maxHeight: "513px",
    overflow: "auto"
}




const TodoList = ({todos}) => {
  return (
    <div style={listStyle}>
        {todos.map(todo=>(
            <TodoListItem
                key={todo.id}
                todo={todo}
            />
        ))}
    </div>
  )
}

export default TodoList