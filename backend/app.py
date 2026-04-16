from flask import Flask, request, jsonify

app = Flask(__name__)

tickets = []

def classify_issue(text):
    text = text.lower()
    if "vpn" in text:
        return "VPN Issue"
    elif "outlook" in text:
        return "Email Issue"
    elif "printer" in text:
        return "Printer Issue"
    elif "password" in text:
        return "Account Lock"
    return "General Issue"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    issue = classify_issue(user_input)

    ticket = {
        "id": len(tickets) + 1,
        "issue": issue,
        "status": "Open"
    }
    tickets.append(ticket)

    return jsonify({
        "response": f"{issue} detected. Ticket #{ticket['id']} created."
    })

@app.route("/tickets", methods=["GET"])
def get_tickets():
    return jsonify(tickets)

if __name__ == "__main__":
    app.run(debug=True)
