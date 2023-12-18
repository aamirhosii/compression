import { useState } from 'react'


import './App.css'

function App() {

  const [file, setFile] = useState()

  const onSubmit = () => {
    console.log()
    console.log("Ran submit")
  }

  return (
    <>
    <h1>Hello</h1>
      <form onSubmit={onSubmit}>
      <input type="file" required />
      <button>Submit</button>
    </form>
    </>
  )
}

export default App
