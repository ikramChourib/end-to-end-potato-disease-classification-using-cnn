from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np
from flask import jsonify

model = None
class_names = ["Early Blight", "Late Blight", "Healthy"]
BUCKET_NAME = "potatos-codebasics-tf-models"

def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")

def predict(request):
    global model
    if model is None:
        download_blob(BUCKET_NAME, "models/version1_potatoes.h5", "/tmp/potatoes.h5")
        model = tf.keras.models.load_model("/tmp/potatoes.h5")

    if request.method != "POST":
        return jsonify({"error": "Please use POST"}), 405

    # Récupération de l'image depuis le formulaire ou le JSON
    if request.files:
        image = request.files["file"]
        image = Image.open(image).convert("RGB").resize((256, 256))
    else:
        return jsonify({"error": "No file uploaded"}), 400

    image = np.array(image) / 255.0
    img_array = tf.expand_dims(image, 0)
    predictions = model.predict(img_array)

    predicted_class = class_names[int(np.argmax(predictions[0]))]
    confidence = float(np.max(predictions[0]) * 100)  # ✅ conversion en float natif

    print("Predictions:", predictions)

    # ✅ jsonify gère les types Python natifs
    return jsonify({
        "class": predicted_class,
        "confidence": confidence
    })


#commande : gcloud functions deploy predict \
#  --gen2 \                 
#  --region=europe-west1 \
#  --runtime=python313 \
#  --entry-point=predict \
#  --trigger-http \
#  --allow-unauthenticated \
#  --memory=2048MB \
#  --timeout=540s \
#  --project=potatos-classification-object
