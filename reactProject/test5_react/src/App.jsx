import { useState } from 'react'
import './App.css'
import ThemeButton from './components/ThemeButton'
import ThemeParagraph from './components/ThemeParagraph'
import ThemeProvider from './components/ThemeProvider'

function App() {

  return (
    <>
      <ThemeProvider>
        <div style={{padding: "20px", display: "flex", flexDirection:"column", gap:"20px", minHeight:"100vh"}}>
          <h1>테마 변경 예제</h1>
          <ThemeButton />
          <ThemeParagraph />
        </div>
      </ThemeProvider>
    </>
  )
}

export default App
