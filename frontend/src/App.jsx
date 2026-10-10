import React from 'react'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import Register from './pages/Register'
import ExploreCases from './pages/ExploreCases'
import CaseDetails from './pages/CaseDetails'

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home/>
  },
  {
    path:'/login',
    element:<Login/>,
  },
  {
    path:'/register',
    element:<Register/>,
  },
  {
    path:'/cases',
    element:<ExploreCases/>,
  },
  {
    path: '/cases/:caseId',
    element: <CaseDetails/>,
  },
]);


const App = () => {
  return (
    <RouterProvider router={router}/>
  )
}

export default App