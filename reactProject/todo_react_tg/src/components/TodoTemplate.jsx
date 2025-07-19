import React from 'react'

const templateStyle = {
    width: "512px",
    marginLeft: "auto",
    marginRight: "auto",
    borderRadius: "4px",
    overflow: "hidden",
}

const titleStyle = {
    background: "#22b8cf",
    color: "white",
    height: "4rem",
    fontSize: "1.5rem",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
}

const contentStyle = {
    background: "white"
}

const TodoTemplate = ({children}) => {
  return (
    <div style={templateStyle}>
        <div style={titleStyle}>일정관리</div>
        <div style={contentStyle}>{children}</div>
    </div>
  )
}

export default TodoTemplate