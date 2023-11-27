import logo from './logo.svg';
import './App.css';

import './App.css';
//import searchBar from './common/components/searchBar';
import {React, useState, useEffect} from 'react';

import {BrowserRouter, Routes, Route} from "react-router-dom";

import Home from "./pages/home"
import AddPage from "./pages/add"
import ClaimPage from "./pages/claim"
import ViewPage from "./pages/view"

function App() {
  return(
    <div className = "App">
      <BrowserRouter>
        <Routes>
          <Route path ="" element={<Home/>}/>
          <Route path ="/addPage" element={<AddPage/>}/>
          <Route path ="/claimPage" element={<ClaimPage/>}/>
          <Route path ="/viewPage" element={<ViewPage/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
