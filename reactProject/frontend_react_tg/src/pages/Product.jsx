import React, { useEffect, useMemo } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { AgGridReact } from 'ag-grid-react'
import { ModuleRegistry } from 'ag-grid-community'
import { AllCommunityModule } from 'ag-grid-community'
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import { productAction } from '../redux/productSlice';

ModuleRegistry.registerModules([AllCommunityModule])

const Product = () => {
  const dispatch = useDispatch();
  const {data, error, status} = useSelector(state=>state.product)
  useEffect(()=>{
    dispatch(productAction())
  }, [dispatch])

  const columnDefs = useMemo(()=> [
    {headerName: "제품코드", field: '제품코드', flex: 1, sortable: true},
    {headerName: "제품명", field: '제품명', flex: 1},
    {headerName: "색상", field: '색상', flex: 1},
    {
      headerName: "원가", 
      field: '원가', 
      flex: 1, 
      type: "numericColumn",
      valueFormatter: (params) => `${params.value?.toLocaleString()}원`
    },
     {
      headerName: "단가", 
      field: '단가', 
      flex: 1, 
      type: "numericColumn",
      valueFormatter: (params) => `${params.value?.toLocaleString()}원`
    },
    {headerName: "제품분류코드", field: '제품분류코드', flex: 1},
  ], []);

  if(status==="loading"){
    return <div>loading.....</div>
  }
  if(error){
    return <div>제품 데이터가 없습니다. </div>
  }

  return (
    <div className='ag-theme-alpine custom-ag-grid' style={{height: 400, width:"100%"}}>
      <AgGridReact
        rowData = {data} //json : [{}, {}, {}, .....]
        columnDefs={columnDefs}
        animateRows={true}
        pagination={true}
        paginationPageSize={5}
        domLayout='autoheight'
      />
    </div>
  )
}

export default Product;