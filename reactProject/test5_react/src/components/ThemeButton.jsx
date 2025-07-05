import { useContext } from "react"
import { ThemeContext } from "./ThemeProvider"

const ThemeButton =() => {

    const {theme, setTheme} = useContext(ThemeContext)

    const buttonStyle= {
        backgroundColor: theme === "light" ? "black" : "white",
        color: theme === "light" ? "white" : "black",
        border: '1px solid gray',
        padding: '10px 20px',
        cursor: "pointer"
    }
    return (
        <button style={buttonStyle} onClick={()=>setTheme(prev => (prev==="light"?"dark":"light"))}>
            현재 테마: {theme} (클릭하여 변경)
        </button>
    )
}

export default ThemeButton