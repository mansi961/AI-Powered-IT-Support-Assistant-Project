async function sendMessage() {
  const input = document.getElementById("userInput").value;

  const res = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message: input})
  });

  const data = await res.json();

  document.getElementById("chatBox").innerHTML += `
    <p><b>You:</b> ${input}</p>
    <p><b>Bot:</b> ${data.response}</p>
  `;
}
