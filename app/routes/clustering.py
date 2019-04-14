from app.factory.text_clustering import start_clustering
from app import app, request, jsonify


@app.route("/cluster", methods=["POST"])
def cluster():
    documents = request.json["documents"]
    return jsonify(documents)
