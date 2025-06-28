import React from 'react'

const Page1 = () => {

    const handleSubmit = (e) => {
        e.preventDefault()
        console.log("target", e.target.key.value)
    }

  return (
    <>
        <div>Page1</div>
        <form onSubmit={handleSubmit} >
            <input name="key" type="text" />
            <button type="submit">제출</button>
        </form>
    </>
  )
}

export default Page1
