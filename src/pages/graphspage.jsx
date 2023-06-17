import Graphs from "../components/graphs.jsx";
const GraphsPage = () => {
  return (
    <div className="mt-24">
      <a className="text-4xl text-white text-center">Основные показатели Датасета обучения модели</a>
      <Graphs />
    </div>
  );
};
export default GraphsPage;
