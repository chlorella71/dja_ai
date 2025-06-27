import React from 'react'

const Info = ({infoData, setInfoData}) => {


    const handleChange = (e) => {
        setInfoData(prev => (
            {...prev, [e.target.name] : e.target.value, [e.target.age] : e.target.age, [e.target.job] : e.target.job}
        ))
    }

    const handleSubmit = (e) => {
        e.preventDefault()
    }


  return (
    <>
      
        <form onSubmit={handleSubmit}>
            <label htmlFor="name">이름:</label>
            <input type="text" id="name" name="name" placeholder={infoData.name} onChange={handleChange} />
            <label htmlFor="age">나이:</label>
            <input type="text" id="age" name="age" placeholder={infoData.age} onChange={handleChange}/>
            <label htmlFor="job">직업:</label>
            <input type="text" id="job" name="job" placeholder={infoData.job} onChange={handleChange}/>
            <input type="submit" value="submit" />
        </form>

        {/* <div>{infoData.name}</div>
        <div>{infoData.age}</div>
        <div>{infoData.job}</div> */}

    </>
  )
}

export default Info