from flask import Flask, render_template, request, jsonify
import os
from utils.traits import traits
from utils.softsets import classification
from utils.resnet50 import predict_class

app = Flask(__name__)

# Define the path to the uploads folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the "uploads" folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    return render_template("index.html", traits=traits)


@app.route("/find_dog_breed", methods=["POST"])
def find_dog_breed():
    # Get the uploaded image
    image = request.files["image"]

    # Get the list of selected traits
    sample = {}
    print(request.form)
    for trait, value in zip(traits, request.form.getlist('slide_traits')):
        sample[trait] = float(value)
    print(sample)
    # sample = {
    #     'Sensitive': 0.6,
    #     'Introvert': 0,
    #     'Family-oriented': 1,
    #     'Protective': 0.4,
    #     'Friendly': 1,
    #     'Extravert': 0.8,
    #     'Quick learner': 0,
    #     'Intelligent': 0.5,
    #     'Communicative': 0.6,
    #     'Curious': 0.2,
    #     'Energetic': 1,
    #     'Emotional': 0.5,
    #     'Sport freak': 0.1,
    #     'Playfull': 0.9
    # }
    # Save the uploaded image to the "uploads" folder
    if image:
        path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(path)

    # Process the image and traits here
    softsets_result = classification(sample)
    resnet50_result = predict_class(path)
    print(softsets_result, resnet50_result)
    combined_result = {}
    for breed in softsets_result.keys():
        combined_result[breed] = (softsets_result[breed] + 1.5*resnet50_result[breed])/2.5

    max_key = max(combined_result, key=lambda k: combined_result[k])
    # Replace the hardcoded result with your actual logic
    result = {"dog_breed": max_key}
    print(result)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


