import React, { useState, useEffect } from "react";
import ChessBoard from "../components/ChessBoard";
import Button from "../components/Button";
import io from "socket.io-client";
import { INIT_GAME, PATH, WS_URL } from "../components/Messages";

export default function App({ sdf }) {
  const [showChessboard, setShowChessboard] = useState(false); // State to toggle between button and chessboard

  var socket = null;

  useEffect(() => {
    if (!socket) {
      socket = io(WS_URL, { path: PATH });
      console.log("socket created", socket);
    }
  }, []);

  const handleClick = () => {
    setShowChessboard(true); // Show the chessboard when button is clicked
    //Connect to the backend
    socket.emit("handle_message", { type: INIT_GAME });
  };

  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      {showChessboard ? (
        <div className="w-[50%] h-[50%] shadow-lg rounded">
          <ChessBoard socket={socket} />
        </div>
      ) : (
        <Button handleClick={handleClick} />
      )}
    </div>
  );
}
