import { BrowserRouter, Routes, Route } from "react-router-dom";

import MainLayout from "./layouts/MainLayout";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import ExploreCases from "./pages/ExploreCases";
import CaseDetails from "./pages/CaseDetails";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<MainLayout />}>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/cases" element={<ExploreCases />} />
          <Route path="/cases/:caseId" element={<CaseDetails />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}