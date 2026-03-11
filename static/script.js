function appendMessage(text, sender) {
    const chatbox = document.getElementById('chatbox');
    const msg = document.createElement('div');
    msg.className = sender;
    msg.textContent = text;
    chatbox.appendChild(msg);
    chatbox.scrollTop = chatbox.scrollHeight;
}

async function sendMessage() {
    const input = document.getElementById('message');
    const message = input.value.trim();
    if (!message) return;
    appendMessage("Sen: " + message, "user");
    input.value = "";

    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message })
        });

        if (!res.ok) {
            throw new Error("HTTP error " + res.status);
        }

        const data = await res.json();
        appendMessage("ÇınarGPT: " + data.response, "bot");
    } catch (err) {
        appendMessage("Hata: Yanıt alınamadı. " + err.message, "bot");
        console.error(err);
    }
}