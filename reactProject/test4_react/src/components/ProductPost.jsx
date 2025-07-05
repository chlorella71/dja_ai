import React, {useState} from 'react'
import {useDispatch} from 'react-redux'
import {fetchPostProducts} from '../redux/reducerSlices/productPostSlice'
import { fetchProducts} from '../redux/reducerSlices/productSlice'
// import Modal from './Modal'
import {Modal, Input, InputNumber, Checkbox, Button, Form} from 'antd'

// example = {
//       "id": "A1",
//       "name": "Laptop",
//       "price": 1200,
//       "category": "Electronics",
//       "inStock": true
//     }

const ProductPost = () => {
    // const [product, setProduct] =useState({
    //     name: '',
    //     price: 0,
    //     category: '',
    //     inStock: false,
    // })

    const [modalOpen, setModalOpen] = useState(false)
    const [modalMessage, setModalMessage] = useState('')

    const dispatch = useDispatch();

    const [form] = Form.useForm();

    // const handleChange= (e)=>{
    //     const {name, value, type, checked } = e.target
    //     setProduct(prev => ({
    //         ...prev,
    //         [name] : type === 'checkbox' ? checked: value
    //     }))
    // }

    const handleSubmit = async (product) => {
        try {
            await dispatch(fetchPostProducts(product)).unwrap()
            dispatch(fetchProducts())
            form.resetFields()
            setModalMessage('상품등록성공!')
            setModalOpen(true)
        } catch (error) {
            console.error('에러: ', error)
            setModalMessage('등록 실패!...')
            setModalOpen(true)
        }
    }

  return (
    <>
        <div><h2>ProductPost</h2></div>
        <Form
            form={form}
            layout="vertical"
            onFinish={handleSubmit}
            style={{maxWidth: 400}}
        >
            <Form.Item
                label="품명"
                name="name"
                rules={[{required: true, message: '품명을 입력하세요'}]}
            >
                <Input placeholde="품명" />
            </Form.Item>
            <Form.Item
                label="가격"
                name="price"
                rules={[{required: true, message: '가격을 입력하세요'}]}
            >
                <InputNumber placeholde="가격" style={{width:'100%'}}/>
            </Form.Item>
            <Form.Item
                label="카테고리"
                name="category"
                rules={[{required: true, message: '카테고리를 입력하세요'}]}
            >
                <Input placeholde="카테고리" />
            </Form.Item>
            <Form.Item
                name="inStock"
                valuePropName="checked"
            >
                <Checkbox>재고 있음</Checkbox>
            </Form.Item>
            <Form.Item>
                <Button type="primary" htmlType="submit">
                    등록
                </Button>
            </Form.Item>
        </Form>
        {/* <form onSubmit={handleSubmit}>
            <input type="text" name="name" placeholder='품명' value={product.name} onChange={handleChange} />
            <input type="number" name="price" placeholder='가격' value={product.price} onChange={handleChange} />
            <input type="text" name="category" placeholder='품목' value={product.category} onChange={handleChange} />
            <input type="checkbox" name="inStock" placeholder='재고' value={product.inStock} onChange={handleChange} />
            <button type="submit">등록</button>
        </form> */}
        {/* <div>{modal && <Modal message={modal} />}</div> */}
        <Modal
            open={modalOpen}
            onOk={()=>setModalOpen(false)}
            onCancel={()=>setModalOpen(false)}
            okText='확인'
            cancelButtonProps={{style: {display: 'none'}}}
        ><p>{modalMessage}</p></Modal>
    </>
  )
}

export default ProductPost
