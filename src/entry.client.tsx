import React from 'react'
import ReactDOM from 'react-dom/client'
import { StartClient } from '@tanstack/start/client'
import { router } from './router'

const element = document.getElementById('app')

if (!element) {
  throw new Error('Root element not found')
}

const root = ReactDOM.createRoot(element)

root.render(
  <React.StrictMode>
    <StartClient router={router} />
  </React.StrictMode>,
)
