import React from 'react'
import { Layout, Menu } from 'antd'
import {
  EnvironmentOutlined,
  GiftOutlined,
  ShoppingOutlined,
  TagsOutlined,
  AppstoreOutlined,
  CalendarOutlined,
  ShareAltOutlined,
  BarChartOutlined,
 } from "@ant-design/icons"
import { Link, useLocation } from 'react-router-dom';

 const {Sider} = Layout;

 const items = [
  {
    key: '/region',
    icon: <EnvironmentOutlined/>,
    label: <Link to ="/region">지역</Link>
  }, 
  {
    key: '/promotion',
    icon: <GiftOutlined/>,
    label: <Link to ="/promotion">프로모션</Link>
  }, 
  {
    key: '/product',
    icon: <ShoppingOutlined/>,
    label: <Link to ="/product">제품</Link>
  }, 
  {
    key: '/category',
    icon: <TagsOutlined/>,
    label: <Link to ="/category">분류</Link>
  }, 
  {
    key: '/subcategory',
    icon: <AppstoreOutlined/>,
    label: <Link to ="/subcategory">제품분류</Link>
  }, 
  {
    key: '/date',
    icon: <CalendarOutlined/>,
    label: <Link to ="/date">날짜</Link>
  },
   {
    key: '/channel',
    icon: <ShareAltOutlined/>,
    label: <Link to ="/channel">채널</Link>
  },
  {
    key: '/sale',
    icon: <BarChartOutlined/>,
    label: <Link to ="/sale">판매</Link>
  },

 ]

const SideBar = () => {
  const loaction = useLocation();
  return (
    <Sider width={200} className='site-layout-background'>
      <Menu
        mode="inline"
        selectedKeys={[loaction.pathname]}
        style={{height: "100%", borderRight: 0}}
        items = {items}
      />
    </Sider>
  )
}

export default SideBar