import React, { useCallback, useRef, useState } from 'react';
import TodoTemplate from './TodoTemplate';
import TodoInsert from './TodoInsert';
import TodoList from './TodoList';

const initialTodos = [
    {
        id: 1,
        text: "HTML 공부",
        checked: true
    },
    {
        id: 2,
        text: "CSS 공부",
        checked: true
    },
    {
        id: 3,
        text: "JavaScript 공부",
        checked: true
    },
    {
        id: 4,
        text: "React 공부",
        checked: true
    }
];

const style = {
    marginTop: "10rem",
    marginBottom: "auto",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
};

const Todo = () => {
    const [todos, setTodos] = useState(initialTodos);
    // Initialize nextId to be one greater than the last id in initialTodos
    // to ensure uniqueness when adding new items.
    const nextId = useRef(initialTodos.length > 0 ? Math.max(...initialTodos.map(todo => todo.id)) + 1 : 1);

    const handleInsert = useCallback((text) => {
        setTodos(prev => [
            ...prev,
            {
                id: nextId.current, // Use the current nextId
                text,
                checked: false, // Typically new todos are unchecked by default
            }
        ]);
        nextId.current += 1; // Increment for the next todo
    }, []); // No dependencies needed for functional setTodos update

    const handleDelete = useCallback((id) => {
        setTodos(prevTodos => prevTodos.filter(todo => todo.id !== id));
    }, []); // No dependencies needed for functional setTodos update

    const handleOnToggle = useCallback((id) => {
        setTodos(prev => (
            prev.map(todo => (
                todo.id === id ? { ...todo, checked: !todo.checked } : todo
            ))
        ));
    }, []); // No dependencies needed for functional setTodos update

    return (
        <div style={style}>
            <TodoTemplate>
                <TodoInsert handleInsert={handleInsert} />
                <TodoList
                    todos={todos}
                    handleDelete={handleDelete}
                    handleOnToggle={handleOnToggle}
                />
            </TodoTemplate>
        </div>
    );
};

export default Todo;