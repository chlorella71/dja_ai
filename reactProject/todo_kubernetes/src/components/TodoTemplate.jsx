import React from 'react'; // Children은 React에서 가져올 필요 없음 (prop으로 사용)

const templateStyle = {
    width: '512px',
    marginLeft: 'auto',
    marginRight: 'auto',
    borderRadius: '4px',
    overflow: 'hidden',
};

const titleStyle = {
    background: '#22b8cf',
    color: 'white',
    height: '4rem',
    fontSize: '1.5rem',
    display: 'flex', // 'diplay' -> 'display' 오타 수정
    alignItems: 'center',
    justifyContent: 'center',
};

const contentStyle = {
    background: 'white', // 현재 코드에서 큰 문제는 없지만, 필요시 조정 가능
};

// props로 'children'을 받도록 수정
const TodoTemplate = ({ children }) => {
    return (
        <div style={templateStyle}>
            <div style={titleStyle}>일정관리</div>
            {/* children prop을 사용하여 자식 요소 렌더링 */}
            <div style={contentStyle}>{children}</div>
        </div>
    );
};

export default TodoTemplate;