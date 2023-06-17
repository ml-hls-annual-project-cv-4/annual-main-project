import { useState } from "react";
import reactLogo from "./assets/react.svg";
import Dataset from "./pages/dataset";
import Navbar from "./components/Navbar";
import { BrowserRouter } from "react-router-dom";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Layout from "./components/Layout";
import GraphsPage from "./pages/graphspage";
import PredictionPage from "./pages/predictionpage";
function App() {
  return (
    <div className="App">
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Layout />}>
              <Route index element={<Dataset />} />
            </Route>
            <Route path="/dataset" element={<Layout />}>
              <Route index element={<GraphsPage />} />
            </Route>
            <Route path="/prediction" element={<Layout />}>
              <Route index element={<PredictionPage />} />
            </Route>
          </Routes>
        </BrowserRouter>
      </div>
  );
}

export default App;
