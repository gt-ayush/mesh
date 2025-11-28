// Connect to WebSocket server
let socket = new WebSocket("ws://127.0.0.1:8000/ws/chat/");

socket.onopen = () => {
    console.log("Connected to WebSocket!");
};

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    displayMessage(data.message, false);
};

socket.onclose = () => {
    console.log("Disconnected from WebSocket.");
};

// Send message
function sendMessage() {
    const input = document.getElementById("messageInput");
    const msg = input.value.trim();

    if (msg === "") return;

    socket.send(JSON.stringify({ message: msg }));
    displayMessage(msg, true);

    input.value = "";
}

// Show message in chat window
function displayMessage(msg, isSelf) {
    const box = document.getElementById("chat-box");

    const div = document.createElement("div");
    div.classList.add("message");
    if (isSelf) div.classList.add("self");

    div.textContent = msg;
    box.appendChild(div);

    box.scrollTop = box.scrollHeight; // Auto-scroll
}
