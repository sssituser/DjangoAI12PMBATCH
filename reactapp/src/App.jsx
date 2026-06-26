import React from "react";
import Home from "./components/Home";
import Register from "./components/Register";
import Login from "./components/Login";
import About from "./components/About";
import Contact from "./components/Contact";
import { Routes,Route } from "react-router-dom";
import Navbar from "./components/Navbar";
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
      </Routes>  
    </React.Fragment>
  )
}
