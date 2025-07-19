import React, { useEffect, useMemo } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { AgGridReact } from 'ag-grid-react'
import { ModuleRegistry } from 'ag-grid-community'
import { AllCommunityModule } from 'ag-grid-community'
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import { regionAction } from '../redux/regionSlice';

ModuleRegistry.registerModules([AllCommunityModule])

const Region = () => {
  const dispatch = useDispatch();
  const {data, error, status} = useSelector(state=>state.region)
  useEffect(()=>{
    dispatch(regionAction())
  }, [dispatch])
  const columnDefs = useMemo(()=> [
    {headerName: "지역코드", field: '지역코드', flex: 1, sortable: true},
    {headerName: "시도", field: '시도', flex: 1, sortable: true},
     {headerName: "구군시", field: '구군시', flex: 1, sortable: true},
      {headerName: "지역", field: '지역', flex: 1, sortable: true},
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

export default Region;