import { io } from "socket.io-client";
import { INIT_GAME } from "../components/Messages";
const WS_URL = "http://localhost:5173";
const socket = io.connect(WS_URL);

const useSocket = (message) => {
  socket.emit("message", (message) => {
    console.log("Received message");
  });
};

export default useSocket;
