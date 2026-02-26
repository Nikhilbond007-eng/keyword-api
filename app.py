from flask import Flask, request, jsonify
import os
from google.ads.googleads.client import GoogleAdsClient

# Create Flask app
app = Flask(__name__)

# Load credentials from Render environment variables
config = {
    "developer_token": os.environ.get("DEVELOPER_TOKEN"),
    "client_id": os.environ.get("CLIENT_ID"),
    "client_secret": os.environ.get("CLIENT_SECRET"),
    "refresh_token": os.environ.get("REFRESH_TOKEN"),
    "use_proto_plus": True,
}

client = GoogleAdsClient.load_from_dict(config)


@app.route("/keywords")
def get_keywords():
    keyword = request.args.get("keyword")

    customer_id = "9164552447"  # your ads customer id (no dashes if error later)

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
