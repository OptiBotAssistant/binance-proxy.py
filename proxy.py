from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/binance")
def proxy_binance():
    symbol = request.args.get("symbol", "BTCUSDT")
    interval = request.args.get("interval", "5m")
    limit = request.args.get("limit", "5")

    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "Binance Proxy is running"
