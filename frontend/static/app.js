// frontend/static/app.js

let socket = null;
const ws_url = (location.protocol === 'https:' ? 'wss://' : 'ws://') + location.host + "/ws/chat/";

function appendMessage(text) {
    const chatBox = document.getElementById("chat-box");
    const p = document.createElement("p");
    p.textContent = "🟦 " + text;
    chatBox.appendChild(p);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function setupWebSocket() {
    socket = new WebSocket(ws_url);

    socket.onopen = function() {
        console.log("WebSocket connected");
    };

    socket.onmessage = function(event) {
        try {
            const data = JSON.parse(event.data);
            if (data.type === "chat") {
                appendMessage(data.message);
            } else if (data.type === "history") {
                // history.messages is an array
                const hist = data.messages || [];
                document.getElementById("chat-box").innerHTML = "";
                hist.forEach(m => appendMessage(m));
            }
        } catch (e) {
            console.error("Invalid message", e);
        }
    };

    socket.onclose = function() {
        console.log("WebSocket closed, retrying in 2s...");
        setTimeout(setupWebSocket, 2000);
    };

    socket.onerror = function(err) {
        console.error("WebSocket error", err);
        socket.close();
    };
}

// Call this on page load
setupWebSocket();

async function sendMessage() {
    const input = document.getElementById("msgInput");
    const msg = input.value.trim();
    if (!msg) return;

    // Use websocket if connected
    if (socket && socket.readyState === WebSocket.OPEN) {
        socket.send(JSON.stringify({type: "chat", message: msg}));
    } else {
        // Fallback to HTTP endpoint
        await fetch(`/send/?msg=${encodeURIComponent(msg)}`);
    }
    input.value = "";
}
