import React, { useEffect, useMemo } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { AgGridReact } from 'ag-grid-react'
import { ModuleRegistry } from 'ag-grid-community'
import { AllCommunityModule } from 'ag-grid-community'
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import { promotionAction } from '../redux/promotionSlice';

ModuleRegistry.registerModules([AllCommunityModule])

const Promotion = () => {
  const dispatch = useDispatch();
  const {data, error, status} = useSelector(state=>state.promotion)
  useEffect(()=>{
    dispatch(promotionAction())
  }, [dispatch])
  const columnDefs = useMemo(()=> [
    {headerName: "프로모션코드", field: '프로모션코드', flex: 1, sortable: true},
    {headerName: "프로모션", field: '프로모션', flex: 1, sortable: true},
    {
      headerName: "할인율", 
      field: '할인율', 
      flex: 1,
      valueFormatter: (params) => `${(params.value*100).toFixed(0)}%`,
      // cellStyle: {textAlign: 'right'}
    },
  ], []);

  if(status==="loading"){
    return <div>loading.....</div>
  }
  if(error){
    return <div>프로모션 데이터가 없습니다. </div>
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

export default Promotion