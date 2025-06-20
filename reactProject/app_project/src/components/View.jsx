import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector} from 'react-redux'
import { fetchData} from '../redux/reducer'

// 데이터로부터 <tr><td>...</td></tr> 요소 생성
const extractData = (data) => {
    return data.map((datum, idx) => {
        const tdList = Object.entries(datum)
            .filter(([key], index) => key !== 'id') // id 제외
            .map(([key, value], tdIdx) => <td key={tdIdx}>{value}</td>);

        return <tr key={idx}>{tdList}</tr>;
    });
};

const View = ({props}) => {

    const dispatch = useDispatch();

    const {loading, data, error} = useSelector(state => state.view)

    useEffect(() => {
       dispatch(fetchData(props))
    }, [dispatch, props]);

    // 로딩 처리
    if (loading) return <p>Loading...</p>;

    if (!data || data.length === 0) return <p>No data available.</p>;

    // 에러 처리
    if (error) return <p>Error...!</p>

    const headers = Object.keys(data[0]).filter((key) => key !== 'id');

    return (
        <>
            <h3>View</h3>
            <table border="1">
                <thead>
                    <tr>
                        {headers.map((header, idx) => (
                            <th key={idx}>{header}</th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {extractData(data)}
                </tbody>
            </table>
        </>
    );
};

export default View;

// import axios from 'axios';
// import React, { useEffect, useState } from 'react';

// // 데이터로부터 <tr><td>...</td></tr> 요소 생성
// const extractData = (data) => {
//     return data.map((datum, idx) => {
//         const tdList = Object.entries(datum)
//             .filter(([key], index) => key !== 'id') // id 제외
//             .map(([key, value], tdIdx) => <td key={tdIdx}>{value}</td>);

//         return <tr key={idx}>{tdList}</tr>;
//     });
// };

// const View = ({props}) => {
//     const [data, setData] = useState(null);

//     useEffect(() => {
//         const fetch = async () => {
//             try {
//                 const url = `http://localhost:3001/${props}`;
//                 const response = await axios.get(url);
//                 setData(response.data);
//             } catch (err) {
//                 console.error(err);
//             }
//         };
//         fetch(props);
//     }, [props]);

//     // 로딩 처리
//     if (!data) return <p>Loading...</p>;

//     const headers = Object.keys(data[0]).filter((key) => key !== 'id');

//     return (
//         <>
//             <h3>View</h3>
//             <table border="1">
//                 <thead>
//                     <tr>
//                         {headers.map((header, idx) => (
//                             <th key={idx}>{header}</th>
//                         ))}
//                     </tr>
//                 </thead>
//                 <tbody>
//                     {extractData(data)}
//                 </tbody>
//             </table>
//         </>
//     );
// };

// export default View;