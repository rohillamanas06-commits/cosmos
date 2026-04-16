import React from 'react'
import ReactDOM from 'react-dom/client'
import { RouterProvider } from '@tanstack/react-router'
import { router } from './router'

const element = document.getElementById('app')

if (!element) {
  throw new Error('Root element not found')
}

const root = ReactDOM.createRoot(element)

root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)

