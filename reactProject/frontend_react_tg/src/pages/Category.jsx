import React, { useEffect, useMemo } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { AgGridReact } from 'ag-grid-react'
import { ModuleRegistry } from 'ag-grid-community'
import { AllCommunityModule } from 'ag-grid-community'
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import { categoryAction } from '../redux/categorySlice';

ModuleRegistry.registerModules([AllCommunityModule])

const Category = () => {
  const dispatch = useDispatch();
  const {data, error, status} = useSelector(state=>state.category)
  useEffect(()=>{
    dispatch(categoryAction())
  }, [dispatch])

  const columnDefs = useMemo(()=> [
    {headerName: "분류코드", field: '분류코드', flex: 1, sortable: true},
    {headerName: "분류명", field: '분류명', flex: 1},
   
  ], []);

  if(status==="loading"){
    return <div>loading.....</div>
  }
  if(error){
    return <div>분류 데이터가 없습니다. </div>
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

export default Category;