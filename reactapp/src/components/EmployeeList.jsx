import React,{useEffect, useState} from "react";
import { Link } from "react-router-dom";
import axios from "axios";

export default function EmployeeList(){
    let[employees,setEmployees]=useState([])
    function getEmployees(){
        axios.get("http://localhost:9000/employees/")
        .then((res)=>{
            setEmployees(res.data)
        })
        .catch((error)=>{
            alert(error)
        })
    }
    useEffect(()=>{
        getEmployees()
    },[])
    function del(id){
        axios.delete(`http://localhost:9000/employees/${id}`)
        .then(()=>{
            alert("Record deleted")
            getEmployees()
        })
        .catch((e)=>{
            alert(e)
        })
    }

    return(
        <React.Fragment>
            <div className="container">
                <section>
                    <div className="row mt-3">
                        <div className="col">
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam ducimus, quos quod veritatis assumenda voluptates animi eius dolor vero. Dolorem reiciendis explicabo modi amet doloribus dignissimos illum delectus, optio alias. Optio distinctio, totam commodi illum laboriosam qui excepturi assumenda accusantium sapiente reprehenderit harum animi magni, molestiae consectetur odit voluptates perspiciatis dolore. Modi iusto nemo delectus voluptatem libero odit, vero saepe!
                        </div>
                    </div>
                    <div className="row mt-3">
                        <div className="col-md-8">
                            <Link to={"/register"} className="btn btn-sm btn-outline-deep-purple">Create</Link>
                        </div>
                        <div className="col-md-4">

                        </div>
                    </div>
                </section>
                {
                    employees.length>0 ?  
                    <table className="mt-5 table table-bordered  table-striped table-hover text-center">
                        <thead className="bg-primary text-white">
                            <tr>
                                <th>Employee Id</th>
                                <th>Employee Name</th>
                                <th>Employee Salary</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                employees.map((emp)=>{
                                    return(
                                        <tr>
                                                <td>{emp.id}</td>
                                                <td>{emp.ename}</td>
                                                <td>{emp.esal}</td>
                                                <td>
                                    <Link to={`/find/${emp.id}`}>
                            <i className=" text-success fa fa-eye-slash fa-2x mr-2"></i>
                                    </Link>      

                                    <Link to={`/edit/${emp.id}`}>
                            <i className=" text-primary fa fa-pencil-square fa-2x mr-2"></i>
                                    </Link>    
                                                    
                                        <i className=" text-danger fa fa-trash-alt fa-2x" onClick={()=>del(emp.id)} ></i>
                                                </td>
                                        </tr>
                                    )
                                })
                            }
                        </tbody>

                    </table>
                    :
                    <p className="h1 text-danger text-center">Recors Not Found</p>
                }
            </div>
        </React.Fragment>
    )

}
