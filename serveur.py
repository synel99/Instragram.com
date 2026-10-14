from flask import Flask, request, jsonify, send_from_directory

app = Flask(____)

@app.route("/")
def accueil():
    return send_from_directory(".", "index.html")

@app.route("/script.js")
def script():
    return send_from_directory(".", "script.js")

@app.route("/recevoir", methods=["POST"])
def recevoir():
    donnees = request.get_json() or {}
    message = donnees.get("message", "")
    print("DONNEES RECUES :", donnees)

    print("INFORMATION REÇUE :", message)

    with open("messages.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

    return jsonify({"message": "Message reçu !"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)