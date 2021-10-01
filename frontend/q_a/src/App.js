import logo from './logo.svg';
import './App.css';
import {Nav, Footer, About, Contact, Home, Answer} from "./components/Routes"
import { Route,Switch } from 'react-router-dom'

function App() {
  return (
    <div className="App">
      <Nav />
      <Switch>
        <Route path='/' exact component={() => <Home />} />
        <Route path='/about' exact component={() => <About />} />
        <Route path='/contact' exact component={() => <Contact />} />
      </Switch>
      <Footer />
    </div>
  );
}

export default App;