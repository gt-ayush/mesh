const socket = new WebSocket("ws://127.0.0.1:8000/ws/chat/");

socket.onopen = () => console.log("WebSocket connected!");
socket.onclose = () => console.log("WebSocket disconnected.");

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    addMessage(data.message, false);
};

function sendMessage() {
    const input = document.getElementById("messageInput");
    const msg = input.value.trim();
    if (!msg) return;

    socket.send(JSON.stringify({ message: msg }));
    addMessage(msg, true);

    input.value = "";
}

function addMessage(text, self) {
    const box = document.getElementById("chat-box");

    const div = document.createElement("div");
    div.className = "msg " + (self ? "self" : "other");
    div.textContent = text;

    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}
