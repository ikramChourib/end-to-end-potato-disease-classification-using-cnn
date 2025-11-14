PROJECT_ID="potatos-classification-object"
PROJECT_NUMBER="755556308120"

CLOUDBUILD_SA="$PROJECT_ID@cloudbuild.gserviceaccount.com"
FUNCTIONS_SA="service-$PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$CLOUDBUILD_SA" \
  --role="roles/cloudfunctions.developer"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$CLOUDBUILD_SA" \
  --role="roles/iam.serviceAccountUser"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$FUNCTIONS_SA" \
  --role="roles/run.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$FUNCTIONS_SA" \
  --role="roles/storage.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$FUNCTIONS_SA" \
  --role="roles/logging.logWriter"
