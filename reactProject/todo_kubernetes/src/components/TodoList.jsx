import React from 'react'; // React import는 이미 되어있습니다.
import TodoListItem from './TodoListItem';

const listStyle = {
    minHeight: '320px',
    maxHeight: '513px',
    overflow: 'auto',
};

const TodoList = ({ todos, handleDelete, handleOnToggle }) => {
    console.log('TodoList 렌더링'); // 렌더링 확인용 (나중에 삭제)

    return (
        <div style={listStyle}>
            {todos.map(todo => (
                <TodoListItem
                    key={todo.id}
                    todo={todo}
                    handleDelete={handleDelete}
                    handleOnToggle={handleOnToggle}
                />
            ))}
        </div>
    );
};

// React.memo로 감싸서 props가 변경될 때만 리렌더링되도록 최적화
export default React.memo(TodoList);