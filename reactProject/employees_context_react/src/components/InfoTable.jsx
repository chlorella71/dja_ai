import React from 'react'
const tStyle={
    borderCollapse: "collapse",
    width: "100%"
}

const cStyle = {
    border: "1px solid black",
    padding: "8px",
    textAlign: "center"
}


const InfoTable = ({info}) => {
    if (!info) return <div>선택된 정보가 없습니다.</div>; // ← 방어 코드 추가
  return (
    <table style={tStyle}>
        <thead>
            <tr>
                {Object.keys(info).map(key=><th style={cStyle}>{key}</th>)}
            </tr>
        </thead>
        <tbody>
            <tr>
                {Object.values(info).map(value=><td style={cStyle}>{value}</td>)}
            </tr>
        </tbody>
        
    </table>
  )
}

export default InfoTable