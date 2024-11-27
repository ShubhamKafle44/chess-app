import React, { useState, useEffect } from "react";
import { Chessboard } from "react-chessboard";
import { io } from "socket.io-client";
import { MOVE, PATH, WS_URL } from "./Messages";

export default function ChessBoard({ socket }) {
  const [boardState, setBoardState] = useState("start"); // Initial board position in FEN format

  useEffect(() => {
    // Listen for board updates from the backend
    socket.on("updateBoard", (newBoard) => {
      setBoardState(newBoard); // Update board state with FEN string
    });
  }, []);

  const handleMove = (sourceSquare, targetSquare) => {
    // Create a move object
    const move = {
      from: sourceSquare,
      to: targetSquare,
      promotion: "q", // Default promotion to queen
    };

    // Send the move to the backend
    socket.emit("handle_message", { type: MOVE, payload: move });

    return true; // Allow the move to appear immediately; backend will correct if invalid
  };

  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <Chessboard
        position={boardState}
        onPieceDrop={handleMove} // Trigger move handling on piece drop
      />
    </div>
  );
}
