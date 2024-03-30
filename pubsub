gcloud beta services identity create \
    --service "secretmanager.googleapis.com" \
    --project "PROJECT_ID"

# This is from the output of the command above
export SM_SERVICE_ACCOUNT="service-...."

# Create a pubsub topic in your prject
gcloud pubsub topics create "projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_NAME"

# Make sure you have switched to the correct project first
gcloud pubsub topics add-iam-policy-binding PUBSUB_TOPIC_NAME \
    --member "serviceAccount:${SM_SERVICE_ACCOUNT}" \
    --role "roles/pubsub.publisher"
