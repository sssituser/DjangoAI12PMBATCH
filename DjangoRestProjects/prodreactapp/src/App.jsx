
import React from 'react'
import {Routes,Route} from 'react-router-dom'
import Products from './components/Products'
import AddProduct from './components/AddProduct'

export default function App() {
  return (
   <React.Fragment>
        <Routes>
          <Route path='/' element={<Products/>}/>
          <Route path='/add' element={<AddProduct/>}/>
        </Routes>
   </React.Fragment>
  )
}
