from flask import Flask, jsonify

app = Flask(__name__)
accounts = {}
next_id = 1

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Banking API"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/accounts", methods=["POST"])
def create_account():
    global next_id
    accounts[next_id] = {"id": next_id, "balance": 0}
    acc = accounts[next_id]
    next_id += 1
    return jsonify(acc), 201


@app.route("/accounts/<int:acc_id>/balance")
def get_balance(acc_id):
    acc = accounts.get(acc_id)
    if not acc:
        return jsonify({"error": "Account not found"}), 404
    return jsonify({"balance": acc["balance"]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)