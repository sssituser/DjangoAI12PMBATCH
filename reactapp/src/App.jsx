import React from "react";
import Home from "./components/Home";
import Register from "./components/Register";
import Login from "./components/Login";
import About from "./components/About";
import Contact from "./components/Contact";
import { Routes,Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import EmployeeList from "./components/EmployeeList";
import Edit from "./components/Edit";
import Find from "./components/Find";

export default function App(){
  return(
    <React.Fragment>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/register" element={<Register/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/about" element={<About/>}/>
        <Route path="/contact" element={<Contact/>}/>
        <Route path="/emplist" element={<EmployeeList/>}/>
        <Route path="/edit/:id" element={<Edit/>} />
        <Route path="/find/:id" element={<Find/>}/>
      </Routes>  
    </React.Fragment>
  )
}
