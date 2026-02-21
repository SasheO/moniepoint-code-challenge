from flask import Flask, jsonify, request
from connect_to_database import *

app = Flask(__name__)

@app.route("/analytics/top-merchant", methods=["GET"])
def get_top_merchant():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM top_merchant;")
        response = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/analytics/monthly-active-merchants", methods=["GET"])
def get_monthly_active_merchants():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM  monthly_active_merchants;")
        response = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/analytics/product-adoption", methods=["GET"])
def get_monthly_active_merchants():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM  product_adoption;")
        response = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/aanalytics/kyc-funnel", methods=["GET"])
def get_monthly_active_merchants():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM  kyc_funnel;")
        response = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/aanalytics/failure-rates", methods=["GET"])
def get_monthly_active_merchants():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM  failure_rates;")
        response = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
    # app.run(host="127.0.0.1", port=8080, debug=True)
