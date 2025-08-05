import React from 'react';
import { MdCheckBox, MdCheckBoxOutlineBlank, MdRemoveCircleOutline } from 'react-icons/md';

const listItemStyle = {
    padding: '1rem',
    display: 'flex',
    alignItems: 'center',
    // ListItem 자체의 배경색은 여기서는 설정하지 않음.
    // 홀수/짝수 줄 배경색은 TodoList에서 조건부로 적용하는 것이 일반적.
};

const checkboxStyle = {
    cursor: 'pointer',
    flex: 1,
    display: 'flex',
    alignItems: 'center',
};

const todoTextStyle = { // 할 일 텍스트를 위한 기본 스타일
    marginLeft: '0.5rem',
    flex: 1,
    // 이 기본 스타일에는 색상을 포함하지 않습니다. 색상은 아래에서 조건부로 적용.
};

const deleteStyle = {
    display: 'flex',
    alignItems: 'center',
    fontSize: '1.5rem',
    color: '#ff6b6b', // 삭제 아이콘 색상
    cursor: 'pointer',
};

const TodoListItem = ({ todo, handleDelete, handleOnToggle }) => {
    const { id, text, checked } = todo;

    return (
        <div style={listItemStyle}>
            {/* 체크박스 영역: 클릭 시 토글 함수 호출 */}
            <div style={checkboxStyle} onClick={() => handleOnToggle(id)}>
                {/* 체크 상태에 따라 다른 아이콘 표시 및 색상 적용 */}
                {checked ? (
                    <MdCheckBox style={{ fontSize: '1.5rem', color: '#339af0' }} /> // 체크됨 (파란색)
                ) : (
                    <MdCheckBoxOutlineBlank style={{ fontSize: '1.5rem', color: '#495057' }} /> // 체크 안 됨 (어두운 회색)
                    // 기본 텍스트 색상과 유사하게 설정하여 통일감 부여
                )}
                {/* 할 일 텍스트: 완료 상태에 따라 취소선 및 색상 변경 */}
                <div style={{
                    ...todoTextStyle, // 기본 스타일 적용
                    textDecoration: checked ? 'line-through' : 'none', // 체크되면 취소선
                    color: checked ? '#adb5bd' : '#495057', // ⭐⭐⭐ 여기를 수정 ⭐⭐⭐
                    // checked가 아닐 때는 어두운 색 (#495057, input 배경색과 유사)
                    // checked일 때는 옅은 회색 (#adb5bd)
                }}>
                    {text}
                </div>
            </div>
            {/* 삭제 버튼 영역: 클릭 시 삭제 함수 호출 */}
            <div style={deleteStyle} onClick={() => handleDelete(id)}>
                <MdRemoveCircleOutline />
            </div>
        </div>
    );
};

export default React.memo(TodoListItem);