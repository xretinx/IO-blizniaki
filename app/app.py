from flask import Flask, render_template, request, jsonify
import os
from utils.traits import traits

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
    selected_traits = request.form.getlist("selected_traits")
    print(selected_traits)

    # Save the uploaded image to the "uploads" folder
    if image:
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))

    # Process the image and traits here
    # Replace the hardcoded result with your actual logic
    result = {"dog_breed": "Golden Retriever"}

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)


