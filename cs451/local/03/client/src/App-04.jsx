import './AvatarCSS.css';
const person = {
    name: 'Gregorio Y. Zara',
    theme: {
        backgroundColor: 'black',
        color: 'pink'
    }
};
  
function TodoList() {
    return (
        <div style={person.theme}>
            <h1>{person.name}'s Todos</h1>
            <img
                className="avatar"
                src="./gregorio_zara.png"
                alt="Gregorio Y. Zara"
            />
            <ul>
                <li>Improve the video phone</li>
                <li>Prepare aeronautics lectures</li>
                <li>Work on the alchol-fuelled engine</li>
            </ul>
        </div>
    );
}

function App ()
{
    return (
        <section>
            <h1>Todo list</h1>
            <TodoList />
        </section>
    );
}

export default App;