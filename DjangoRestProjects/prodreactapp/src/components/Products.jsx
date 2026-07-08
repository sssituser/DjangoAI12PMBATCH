import React, { useEffect, useState } from "react";
import axios from 'axios'
import {Link} from 'react-router-dom'

export default function Products(){
    
  let[products,setProducts]=useState([]);

  useEffect(()=>{
    axios.get("http://localhost:7000/products/")
    .then((res)=>{
      setProducts(res.data)
    })
    .catch()
  },[])

  return(
    <React.Fragment>
    
      <div className="container mt-5">
        <Link to='/add' className="btn btn-primary btn-sm">Create</Link>
       
        {
          products.length>0 ?
          <table className="table table-bordered table-striped table-hover text-center">
            <thead className="bg-primary text-white">
              <tr>
                <th>Product Id</th>
                <th>Product Name</th>
                <th>Product Price</th>
              </tr>
            </thead>
            {
              products.map((pro)=>{
                return(
                  <tr>
                    <td>{pro.ProductId}</td>
                    <td>{pro.ProductName}</td>
                    <td>{pro.Price}</td>
                  </tr>
                )
              })
            }
          </table>
          :
          <p className="h1 text-center text-danger">Products not found</p>
        }
      </div>
    </React.Fragment>
  );
}