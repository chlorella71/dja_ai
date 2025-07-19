import React, { useEffect, useMemo, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { AgGridReact } from 'ag-grid-react'
import { ModuleRegistry } from 'ag-grid-community'
import { AllCommunityModule } from 'ag-grid-community'
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import { salesAction } from '../redux/salesSlice';
import SaleModal from '../modals/SaleModal'
import { Button } from 'antd'

ModuleRegistry.registerModules([AllCommunityModule])

const Sales = () => {

  const [isModalOpen, setIsModalOpen] = useState(false)
  const dispatch = useDispatch();
  const {data, error, status} = useSelector(state=>state.sales)
  useEffect(()=>{
    dispatch(salesAction())
  }, [dispatch])
  const columnDefs = useMemo(()=> [
      {headerName: "날짜", field: '날짜', flex: 1, sortable: true},
      {headerName: "제품코드", field: '제품코드', flex: 1},
     {headerName: "고객코드", field: '고객코드', flex: 1},
     {headerName: "프로모션코드", field: '프로모션코드', flex: 1},
     {headerName: "채널코드", field: '채널코드', flex: 1},
     {
        headerName: "수량", 
        field: 'Quantity', 
        flex: 1,
        type: "numericColumn",
        valueFormatter: (params) => `${Number(params.value)?.toLocaleString()}개`,
        // cellStyle: {textAlign: 'right'}
    },
    {
      headerName: "단가", 
      field: 'UnitPrice', 
      flex: 1,
      type: "numericColumn",
      valueFormatter: (params) => `${Number(params.value)?.toLocaleString()}원`,
      // cellStyle: {textAlign: 'right'}
    },
    {headerName: "지역", field: '지역', flex: 1},
      
  ], []);

  if(status==="loading"){
    return <div>loading.....</div>
  }
  if(error){
    return <div>판매 데이터가 없습니다. </div>
  }

  return (
    <>
      <div style={{ display: 'flex', justifyContent: 'flex-end', paddingBottom: "10px" }}>
          <Button type="primary" onClick={() => setIsModalOpen(true)}>판매 등록</Button>
      </div>
        <SaleModal open={isModalOpen} onCancel={() => setIsModalOpen(false)} />
    
      <div className='ag-theme-alpine custom-ag-grid' style={{height: 450, width:"100%"}}>
      <AgGridReact
        rowData = {data} //json : [{}, {}, {}, .....]
        columnDefs={columnDefs}
        animateRows={true}
        pagination={true}
        paginationPageSize={15}
        domLayout='autoheight'
      />
    </div>
    
    
    </>
    
  )
}

export default Sales;