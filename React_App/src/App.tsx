import ListGroup from "./components/ListGroup/index";

function App() {
  const items = ["Lahore", "Karachi", "Dubai"];
  return (
    <div>
      <ListGroup heading="Cities" items={items} onSelectItem={() => {}} />
    </div>
  );
}

export default App;
