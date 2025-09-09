function TodoList() {
    return (
      <>
        <h1>Hedy Lamarr's Todos</h1>
        <img
            src="./hedy_lamarr.png"
            alt="Hedy Lamarr"
            class="photo"
        />
        <ul>
            <li>Invent new traffic lights</li>
            <li>Rehearse a movie scene</li>
            <li>Improve spectrum technology</li>
        </ul>
      </>
    );
  }
  
  function App() {
    return (
      <section>
        <h1>Todo List</h1>
        <TodoList />
      </section>
    );
  }
  
  export default App;
  