import { getImageUrl } from './utils.js'
import './AvatarCSS.css';

function Avatar({ person, size }) {
  return (
    <img
      className="avatar"
      src={getImageUrl(person)}
      alt={person.name}
      width={size}
      height={size}
    />
  );
}

function Card({ children }) {
  return (
    <div className="card">
      {children}
    </div>
  );
}

function App() {
  return (
    <Card>
      <Avatar
        size={100}
        person={{
          name: 'Hedy Lamarr',
        }}
      />
    </Card>
  );
}

export default App;