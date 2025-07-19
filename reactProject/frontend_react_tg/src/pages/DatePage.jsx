import React, { useEffect, useMemo } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { AgGridReact } from 'ag-grid-react'
import { ModuleRegistry } from 'ag-grid-community'
import { AllCommunityModule } from 'ag-grid-community'
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import { datePageAction } from '../redux/datePageSlice';

ModuleRegistry.registerModules([AllCommunityModule])

const DatePage = () => {
  const dispatch = useDispatch();
  const {data, error, status} = useSelector(state=>state.datePage)
  useEffect(()=>{
    dispatch(datePageAction())
  }, [dispatch])

  const columnDefs = useMemo(()=> [
    {headerName: "날짜코드", field: '날짜코드', flex: 1, sortable: true},
    {headerName: "날짜", field: '날짜', flex: 1},
    {headerName: "년도", field: '년도', flex: 1},
    {headerName: "분기", field: '분기', flex: 1},
    {headerName: "월(No)", field: '월(No)', flex: 1},
    {headerName: "월(영문)", field: '월(영문)', flex: 1},

  ], []);

  if(status==="loading"){
    return <div>loading.....</div>
  }
  if(error){
    return <div>데이트 데이터가 없습니다. </div>
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

export default DatePage;