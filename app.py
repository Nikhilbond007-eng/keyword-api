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


@app.route("/")
def home():
    return "Keyword API Running ✅"


@app.route("/keywords")
def get_keywords():
    try:
        keyword = request.args.get("keyword")

        customer_id = "9164552447"  # NO DASHES

        keyword_plan_idea_service = client.get_service(
            "KeywordPlanIdeaService"
        )

        request_data = {
            "customer_id": customer_id,
            "keyword_seed": {
                "keywords": [keyword]
            },
            "geo_target_constants": [
                "geoTargetConstants/2840"  # USA
            ],
            "language": "languageConstants/1000",
        }

        response = keyword_plan_idea_service.generate_keyword_ideas(
            request=request_data
        )

        results = []

        for idea in response.results[:20]:
            results.append({
                "keyword": idea.text,
                "avg_monthly_searches":
                    idea.keyword_idea_metrics.avg_monthly_searches
            })

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
