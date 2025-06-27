import Td from "./Td"

const Tr = ({infos}) => {
    return(
        <>
            <tr>
                {Object.values(infos).map((value, idx) => (<Td key={idx} value={value}/>))}
            </tr>
        </>
    )
}

export default Tr