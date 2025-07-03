import React, { use, useEffect, useState } from 'react'
import axios from 'axios'

const initialState = {
    text: null,
}

const Sentiment = () => {
    const [sentence, setSentence] = useState(initialState)
    const [result, setResult] =useState(null)

    const fetch = async () => {
        try {
            const response = await axios.post("http://localhost:8000/post/predict", {text: sentence.text})
            return response.data
        } catch (error) {
            console.log(error)
        }
    }

    useEffect(() => {
        console.log(result)
        // fetch()
    }, [result])

    const handleSubmit= async (e) => {
        e.preventDefault()
        const response = await fetch()
        setResult(response)
    }

    const handleChange = (e) => {
        setSentence(prev=>(
            {...prev, [e.target.name]: e.target.value}
        ))
    }

  return (
    <>
        <h2>Sentiment</h2>
        <form onSubmit={handleSubmit}>
            <label>문장을 입력하세요</label>
            <input type="text" name="text" onChange={handleChange} />
            <button type="onsubmit">제출</button>
        </form><br />
        <div>대답: </div>
        {/* <div>{result && result}</div> */}
        <div>
            {result ? (
                result.error ? (
                    <span style={{ color: 'red' }}>에러: {result.error}</span>
                ) : (
                    <>
                        <p>감정: {result.greeting[0].label === 'LABEL_0' ? '부정' : '긍정'}</p>
                        <p>신뢰도: {(result.greeting[0].score * 100).toFixed(2)}%</p>
                    </>
                )
            ) : (
                <p>결과 없음</p>
            )}
        </div>
        
    </>
  )
}

export default Sentiment
