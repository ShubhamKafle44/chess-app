// GamePage.js
import React, { useState } from "react";
import Board from "../components/Board";
import useSocket from "../hooks/useSocket";
import { useEffect } from "react";
import { Chess } from "chess.js";
import { GAME_OVER, INIT_GAME } from "../components/Messages";
const Game = ({ gameId, color }) => {
  const socket = useSocket();
  // const [board, setBoard] = useState(Chess());
  const [fen, setfen] = useState(Chess());
  useEffect(() => {
    if (!socket) {
      return;
    }
    //Initialize  a game first:
    socket.emit("play", INIT_GAME);
    //send moves;
    socket.emit("message");
    socket.on("message", (event) => {
      const message = JSON.parse(event.data);
      console.log(message);
      switch (message.type) {
        case INIT_GAME:
          console.log("Game inititalized");
          break;
        case MOVE:
          console.log("Game inititalized");
          break;
        case GAME_OVER:
          console.log("Game inititalized");
          break;
      }
    });
  });
  return (
    <div className="">
      {GAME_OVER && <h2>{GAME_OVER}</h2>}
      <Board fen={fen} makeMove={makeMove} />
    </div>
  );
};

export default Game;
