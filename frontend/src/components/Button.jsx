export default function Button({ handleClick }) {
  return (
    <button
      onClick={handleClick}
      className="px-4 py-2 bg-blue-500 text-white rounded shadow hover:bg-blue-600"
    >
      Play Game
    </button>
  );
}
