import logo from './logo.svg';
import './App.css';
import Counter from './Counter'

function MyButton() {
    return (
        <button>
        I'm a button
        </button>
    );
}
  
function App() {
    return (
      <div>
        <h1>Welcome to my app</h1>
        <MyButton />
      </div>
    );
}

export default App;
