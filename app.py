from flask import Flask, request, jsonify # type: ignore
import Image_To_JSON as img2json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Up and running!</p>"

@app.route("/image_to_json", methods=["POST"])
def image_to_json_endpoint():
    data = request.json
    if not data or "image_url" not in data or "json_format" not in data:
        return jsonify({"error": "Invalid input, 'image_url' and 'json_format' are required."}), 400
    
    image_url = data["image_url"]
    json_format = data["json_format"]

    if "settings" not in data:
        settings = img2json.Settings()
    else:
        settings = img2json.Settings(**data["settings"])
    
    try:
        myImageToJSON = img2json.Image_To_JSON(settings)
        result = myImageToJSON.image_to_json(image_url, json_format, myImageToJSON.model)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
   
    
@app.route("/generate_json_format", methods=["POST"])
def generate_json_format_endpoint():
    data = request.json
    if not data or "image_url" not in data:
        return jsonify({"error": "Invalid input, 'image_url' is required."}), 400
    
    image_url = data["image_url"]
    if "settings" not in data:
        settings = img2json.Settings()
    else:
        settings = img2json.Settings(**data["settings"])
    try:
        myImageToJSON = img2json.Image_To_JSON(settings)
        result = myImageToJSON.generate_JSON_format(image_url)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
