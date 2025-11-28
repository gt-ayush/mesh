function sendMessage() {
    const msg = document.getElementById("msgInput").value;
    if (!msg) return;

    fetch(`/send/?msg=${encodeURIComponent(msg)}`)
    .then(res => res.json())
    .then(() => {
        document.getElementById("msgInput").value = "";
        loadMessages();
    });
}

function loadMessages() {
    fetch(`/receive/`)
    .then(res => res.json())
    .then(data => {
        let box = document.getElementById("messages");
        box.innerHTML = "";

        data.messages.forEach(m => {
            let p = document.createElement("p");
            p.textContent = "• " + m;
            box.appendChild(p);
        });
    });
}

// Auto-refresh messages every 2 seconds
setInterval(loadMessages, 2000);

window.onload = loadMessages;
