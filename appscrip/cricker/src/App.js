import './App.css';
import Cricker from './components/cricker';
import GetCricketer from './components/getCricketer';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Cricker/>
        <GetCricketer/>
      </header>
    </div>
  );
}

export default App;
