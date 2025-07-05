import React, {createContext, useContext, useState} from 'react'

export const ThemeContext = createContext(null) //ThemeContext.provider는 main의 Provider와 똑같은 역할 value는 store와 같은것, redux에서는 dispatch와 비슷?

const ThemeProvider = ({children}) => { // children은 App.jsx에서 ThemeProvider 밑에 구성된 ThemeButton, ThemeParagraph를 가리키게됨?
    const [theme, setTheme] = useState("light")
    const contextValue = {theme, setTheme}
  return (
    <>
        <ThemeContext.Provider value= {contextValue}>
            <h2>ThemeProvider</h2>
            <div>{children}</div>
        </ThemeContext.Provider>

    </>
  )
}

// const ThemeButton =() => {

//     const {theme, setTheme} = useContext(ThemeContext)

//     const buttonStyle= {
//         backgroundColor: theme === "dark" ? "white" : "black",
//         color: theme === "dark" ? "white" : "black",
//         border: '1px solid gray',
//         padding: '10px 20px',
//         cursor: "pointer"
//     }
//     return (
//         <button style={buttonStyle} onClick={setTheme}>
//             현재 테마: {theme} (클릭하여 변경)
//         </button>
//     )
// }

// const ThemeParagraph = () => {
//     const {theme} = useContext(ThemeContext)
//     const paragraphStyle = {
//         color: theme === "dark" ? 'white' : 'black',
//         backgroundColor: theme === 'dark' ? '#333': '#eee',
//         padding: '15px',
//         borderRadius: '5px'
//     }
//     return (
//         <>
//             <p style={paragraphStyle}>이 단락은 현재 테마를 나눔</p>
//         </>
//     )
// }


export default ThemeProvider
