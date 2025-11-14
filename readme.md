This project follows a complete machine learning pipeline that includes model building, backend integration, optimization, and deployment.
The model building phase is carried out using TensorFlow, where a Convolutional Neural Network (CNN) is trained with techniques such as data augmentation and the use of TensorFlow datasets to improve model generalization and performance.
The backend server is implemented using TensorFlow Serving and FastAPI, which together allow efficient model deployment and provide RESTful APIs for prediction requests.
During the model optimization stage, techniques such as quantization are applied to reduce model size and improve inference speed. The optimized model is then converted using TensorFlow Lite for lightweight and efficient execution, especially on edge or mobile devices.
Finally, the frontend and deployment phase involves developing user interfaces with React JS and React Native, enabling both web and mobile access to the model’s predictions. The complete solution is then deployed on Google Cloud Platform (GCP) for scalability and accessibility.


1. install all the requirements in requirements.txt
2. run train/training_model.ipynb => a h5 model will be savec in models file
3. run api/main.py => test your api with postman 
4. in the terminal , execute this commands: 
                    cd frontend 
                    npm install --from-lock-json
                    npm audit fix 
                    # you have to change env.exemple to env, than 
                    export NODE_OPTIONS=--openssl-legacy-provider 
                    npm run start

Deploying the TF Model (.h5) on GCP
Create a GCP account.
Create a Project on GCP (Keep note of the project id).
Create a GCP bucket.
Upload the tf .h5 model generate in the bucket in the path models/potato-model.h5.
Install Google Cloud SDK (Setup instructions).
Authenticate with Google Cloud SDK.
gcloud auth login
Run the deployment script.
cd gcp
gcloud functions deploy predict \
  --gen2 \                 
  --region=europe-west1 \
  --runtime=python313 \
  --entry-point=predict \
  --trigger-http \
  --allow-unauthenticated \
  --memory=2048MB \
  --timeout=540s \
  --project=potatos-classification-object