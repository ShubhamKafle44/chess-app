import Game from "./Game";
import { useNavigate } from "react-router-dom";
export default function Home() {
  const navigate = useNavigate();
  function handleClick() {
    navigate("/game");
  }
  return (
    <div className="justify-center box-border items-center m-6 h-full ">
      <button
        onClick={() => {
          handleClick;
        }}
      >
        Play Game
      </button>
    </div>
  );
}
