import { useContext } from "react"
import { ThemeContext } from "./ThemeProvider"

const ThemeParagraph = () => {
    const {theme} = useContext(ThemeContext)
    const paragraphStyle = {
        color: theme === "dark" ? 'white' : 'black',
        backgroundColor: theme === 'dark' ? '#333': '#eee',
        padding: '15px',
        borderRadius: '5px'
    }
    return (
        <>
            <p style={paragraphStyle}>이 단락은 현재 테마를 반영</p>
        </>
    )
}

export default ThemeParagraph