import React, {useEffect, useState} from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { fetchProducts } from '../redux/reducerSlices/productSlice';
// import 'ag-grid-community/styles/ag-grid.css'
import 'ag-grid-community/styles/ag-theme-alpine.css'
import 'ag-grid-community/styles/ag-theme-quartz.css'
import { AgGridReact } from 'ag-grid-react';
import { PaginationModule, ClientSideRowModelModule, ModuleRegistry, ValidationModule} from 'ag-grid-community';

ModuleRegistry.registerModules([ClientSideRowModelModule, PaginationModule, ValidationModule])


// example = {
//       "id": "A1",
//       "name": "Laptop",
//       "price": 1200,
//       "category": "Electronics",
//       "inStock": true
//     }

const Products = () => {
    const {loading, data, error} = useSelector(state=>state.products)
    const dispatch = useDispatch()
    const [rowData, setRowData] = useState([])
    const columnDefs=[
        { headerName: 'ID', field: 'id', flex: 1},
        { headerName: '이름', field: 'name', flex: 1},
        { headerName: '가격', field: 'price', flex: 1},
        { headerName: '카테고리', field: 'category', flex: 1},
        { headerName: '재고', field: 'inStock', flex: 1, cellRenderer: (params) => (params.value ? 'O': 'X')},
    ]

    useEffect(()=>{
        dispatch(fetchProducts())
    }, [dispatch])
    useEffect(()=>{
        setRowData(data)
    }, [data])
  return (
    <>
      <h2>Products</h2>
      {loading && <p>Data loading...</p>}
      {error && <p>{error}</p>}
      {!loading && data.length === 0 && <p>Data Not Exist...</p>}
      {/* <ul>
        {data.map(product=>(
            <li key={product.id}>
                <strong>{product.name}</strong> ({product.price}원, {product.category}) - {product.inStock ? "O": "X"}
            </li>
        ))}
      </ul> */}
      <div className="ag-theme-alpine" style={{height:400, width:'100%'}}>
        <AgGridReact
            rowData={rowData}
            columnDefs={columnDefs}
            pagination={true}
            paginationPageSize={5}
            paginationPageSizeSelector={[5, 10, 20]}
            // theme="quartz"
            // domLayout="autoHeight"
            // modules={[ClientSideRowModelModule, PaginationModule]}
        />
      </div>
    </>
  )
}

export default Products
