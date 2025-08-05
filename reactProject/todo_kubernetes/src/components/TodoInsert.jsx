import React, { useCallback, useState } from 'react';
import { MdAdd } from 'react-icons/md';

const formStyle = {
    display: 'flex',
    background: '#495057',
};

const inputStyle = {
    background: 'none',
    outline: 'none',
    border: 'none',
    padding: '0.5rem',
    fontSize: '1.125rem',
    lineHeight: '1.5',
    color: 'white',
    flex: '1',
};

const buttonStyle = {
    outline: 'none',
    border: 'none',
    background: '#868e96',
    color: 'white',
    paddingLeft: '1rem',
    paddingRight: '1rem',
    fontSize: '1.5rem',
    display: 'flex',
    alignItems: 'center',
    cursor: 'pointer',
    transition: '0.1s background ease-in',
};

const initialTodo = {
    todo: '', // Initialize with an empty string
};

const TodoInsert = ({ handleInsert }) => {
    const [state, setState] = useState(initialTodo);

    const handleChange = useCallback((e) => {
        setState(prev => ({ ...prev, [e.target.name]: e.target.value }));
    }, []); // No dependency on 'state' needed with functional update

    const handleSubmit = useCallback((e) => {
        e.preventDefault();
        // Prevent adding empty todos
        if (!state.todo.trim()) {
            return;
        }
        handleInsert(state.todo); // Pass only the text
        setState(initialTodo); // Reset to initial empty state
    }, [handleInsert, state.todo]); // Include state.todo to access its latest value

    return (
        <form style={formStyle} onSubmit={handleSubmit}>
            <input
                style={inputStyle}
                type="text"
                name="todo"
                value={state.todo} // Controlled component: input value reflects state
                onChange={handleChange}
                placeholder='할 일을 입력하세요'
            />
            <button style={buttonStyle}>
                <MdAdd />
            </button>
        </form>
    );
};

export default TodoInsert;