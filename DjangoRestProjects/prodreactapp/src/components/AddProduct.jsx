import axios from 'axios';
import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom';

export default function AddProduct() {
 let navi = useNavigate();
    let[product,setProduct]=useState({
        "ProductId":"",
        "ProductName" :"",
        "Price":""
    });
    function submit(event){ 
        event.preventDefault()
        axios.post('http://localhost:7000/products/',product)
        .then(()=>{
            alert("Product Added..")
            navi("/")
        })
        .catch((er)=>{
            alert(er)
        })
    }
    function updateInput(event){
        setProduct({
            ...product,
            [event.target.name]:event.target.value
        })
    }
    return (
    <div className="container mt-5">
        <div className="row d-flext justify-content-center">
            <div className="col-md-5">
                <div className="card mt-5">
                    <div className="card-header text-center bg-primary text-white">
                        <p className="h3">Add Product</p>
                    </div>
                    <div className="card-body">
                        <form action="" onSubmit={submit}>
                                <div className="form-group">
                                    <input  onChange={updateInput} type="number" name="ProductId" value={product.ProductId} className='form-control' placeholder='Product ID'/>
                                </div>
                                <div className="form-group">
                                    <input onChange={updateInput} type="text" name="ProductName" value={product.ProductName} className='form-control' placeholder='Product Name'/>
                                </div>
                                <div className="form-group">
                                    <input onChange={updateInput} type="number" name="Price" value={product.Price} className='form-control' placeholder='Product Price'/>
                                </div>

                                <button className='btn btn-sm btn-primary'>Create</button>
                                <Link to='/' className='btn btn-sm btn-warning float-right'>Back</Link>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
  )
}
