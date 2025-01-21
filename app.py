from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import json

app = Flask(__name__)

CORS(app)

with open("q-vercel-python.json", "r") as file:
    marks_data = json.load(file)


@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")

    result = {"marks": []}

    for name in names:
        matching_entry = next(
            (item for item in marks_data if item["name"] == name), None
        )
        if matching_entry:
            result["marks"].append(matching_entry["marks"])
        else:
            result["marks"].append(None)
    return jsonify(result)


if __name__ == "_main_":
    app.run(debug=True)
