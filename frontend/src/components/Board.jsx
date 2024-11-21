// Board.js
import React from "react";
import { Chessboard } from "react-chessboard";

const Board = ({ fen, makeMove }) => {
  const onDrop = (source, target) => {
    const move = { from: source, to: target, promotion: "q" };
    makeMove(move);
  };

  return <Chessboard position={fen} onPieceDrop={onDrop} />;
};

export default Board;
