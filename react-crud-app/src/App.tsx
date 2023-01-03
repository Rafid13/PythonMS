import './App.css';
import Products from './admin/products';
import Main from './main/main';
import { BrowserRouter, Route, Router, Routes } from 'react-router-dom';
import ProductsCreate from './admin/productsCreate';
import ProductsEdit from './admin/productsEdit';

function App() {
  return (
    <div className="App">            
            <BrowserRouter>
              <Routes>
                <Route path='/' element={<Main />} />
                <Route path='/admin/products' element={< Products />} />   
                <Route path='/admin/products/create'  element={< ProductsCreate />}/>
                <Route path='/admin/products/:id/edit'  element={< ProductsEdit />}/>             
              </Routes>
            </BrowserRouter>
    </div>
  );
}

export default App;

