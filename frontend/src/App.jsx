import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home"; // Assuming you have a Home component
import Game from "./pages/Game"; // Assuming you have a Game component
import Signup from "./components/Signup";
const App = () => {
  return (
    <BrowserRouter>
      {" "}
      {/* No basename here */}
      <Routes>
        {/* The root path for the home page */}
        <Route path="/" element={<Signup />} />
        {/* The route for the game page */}
        {/* <Route path="/game" element={<Game />} /> */}
      </Routes>
    </BrowserRouter>
  );
};

export default App;
