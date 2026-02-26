from flask import Flask, request, jsonify
import os
from google.ads.googleads.client import GoogleAdsClient

# ----------------------------
# Create Flask App
# ----------------------------
app = Flask(__name__)

# ----------------------------
# Load Google Ads credentials
# (from Render Environment Variables)
# ----------------------------
config = {
    "developer_token": os.environ.get("DEVELOPER_TOKEN"),
    "client_id": os.environ.get("CLIENT_ID"),
    "client_secret": os.environ.get("CLIENT_SECRET"),
    "refresh_token": os.environ.get("REFRESH_TOKEN"),
    "use_proto_plus": True,
}

# Initialize Google Ads Client
client = GoogleAdsClient.load_from_dict(config)

# ----------------------------
# API Route
# ----------------------------
@app.route("/keywords")
def get_keywords():
    try:
        keyword = request.args.get("keyword")

        # Your Google Ads Customer ID (NO DASHES)
        customer_id = "9164552447"

        ga_service = client.get_service("GoogleAdsService")

        query = """
            SELECT campaign.id
            FROM campaign
            LIMIT 1
        """

        response = ga_service.search(
            customer_id=customer_id,
            query=query
        )

        return jsonify({
            "status": "API working ✅",
            "keyword": keyword
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# ----------------------------
# Run Server (Render uses this)
# ----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
