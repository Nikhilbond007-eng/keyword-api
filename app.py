from flask import Flask, request, jsonify
from google.ads.googleads.client import GoogleAdsClient

app = Flask(__name__)

client = GoogleAdsClient.load_from_storage("google-ads.yaml")

@app.route("/keywords")
def get_keywords():
    keyword = request.args.get("keyword")

    customer_id ="916-455-2447"

    ga_service = client.get_service("GoogleAdsService")

    query = f"""
        SELECT
          campaign.id
        FROM campaign
        LIMIT 1
    """

    response = ga_service.search(customer_id=customer_id, query=query)

    return jsonify({
        "status": "API working ✅",
        "keyword": keyword
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
