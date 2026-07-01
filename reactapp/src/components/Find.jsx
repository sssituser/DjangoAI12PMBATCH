import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

export default function Find(){
    let {id} = useParams()
    
    let[employee,setEmployee]=useState({});

    function getEmployeeById(){
        axios.get(`http://localhost:9000/employees/${id}`)
        .then((res)=>{
            setEmployee(res.data)
        })
        .catch((e)=>{alert(e)})
    }
    useEffect(()=>{
        getEmployeeById()

    },[])

    return(
        <React.Fragment>
               
                <div className="container mt-5">
                    <div className="row d-flex justify-content-center">
                        <div className="col-md-5">
                            <div className="card mt-5">
                                <div className="card-header bg-primary text-white text-center">
                                        <p className="h1">Employee Info</p>
                                </div>
                                <div className="card-body">
                                    <p className="h2">Employee ID : {employee.id}</p>
                                    <p className="h2">Employee Name : {employee.ename}</p>
                                    <p className="h2">Employee Salary : {employee.esal}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

        </React.Fragment>
    )
}