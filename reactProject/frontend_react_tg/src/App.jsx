import './App.css'
import { Route, Routes } from 'react-router-dom'
import * as Pages from "./pages"
import { Layout } from 'antd'
import HeaderBar from './components/HeaderBar';
import SideBar from './components/SideBar';

const {Header, Content} = Layout;

function App() {

  return (
    <Routes>
      <Route path="/login" element={<Pages.user_Login/>}/>
      <Route path="/register" element={<Pages.user_Register/>}/>
      <Route
        path='/*'
        element={
          <Layout style={{minHeight: '100vh'}}>
            <Header style={{padding:0, background: "#fff"}}>
              <HeaderBar/>
            </Header>
            <Layout>
              <SideBar/>
              <Content style={{
                margin: "24px 16px", 
                padding: 24, 
                background: "#fff", 
                flex: 1,
                overflow: 'auto',
                }}>
                <Routes>
                  <Route path="/region" element={<Pages.region/>}/>
                  <Route path="/promotion" element={<Pages.promotion/>}/>
                  <Route path="/product" element={<Pages.product/>}/>
                  <Route path="/category" element={<Pages.category/>}/>
                  <Route path="/subcategory" element={<Pages.subcategory/>}/>
                  <Route path="/date" element={<Pages.datePage/>}/>
                  <Route path="/channel" element={<Pages.channel/>}/>
                  <Route path="/sale" element={<Pages.sale/>}/>
                </Routes>
              </Content>
            </Layout>
          </Layout>
        }/>
    </Routes>
  )
}

export default App
