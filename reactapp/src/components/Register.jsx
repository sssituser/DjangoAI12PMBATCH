import React,{useState} from "react";
import axios from 'axios'
import {Link, useNavigate} from 'react-router-dom'

export default function Register(){
    let navigate=useNavigate();
    let[employee,setEmployee]=useState({
        ename:"",
        esal : "",
    })

    function updateInput(event){
        setEmployee({
            ...employee,
            [event.target.name]:event.target.value
        })
    }

    function save(event){
        event.preventDefault()
        axios.post("http://localhost:9000/employees/",employee)
        .then(()=>{
            alert("Record Added...")
            navigate("/emplist")
        })
        .catch((error)=>{
            alert(error)
        })
    }

    return(
        <React.Fragment>
            <div className="container">
                <div className="row d-flex justify-content-center mt-5">
                    <div className="col-md-4">
                            <div className="card mt-5">
                                <div className="card-header bg-info text-white text-center">
                                    <p className="h3">Register Here</p>
                                </div>
                                <div className="card-body">
                                    <form action="" onSubmit={save}>
                                        <div className="form-group">
                                            <input type="text" name="ename" value={employee.ename} onChange={updateInput} className="form-control" placeholder="EmployeeName"/>
                                        </div>
                                         <div className="form-group">
                                            <input type="text" name="esal" value={employee.esal} onChange={updateInput} className="form-control" placeholder="EmployeeSalary"/>
                                        </div>
                                        <button className="btn btn-sm btn-outline-light-blue ">Register</button>
                                        <Link to="/emplist" className=" btn btn-sm btn-outline-deep-orange float-right">Back</Link>
                                    </form>
                                </div>
                            </div>
                    </div>
                </div>
            </div>
        </React.Fragment>
    )
}

