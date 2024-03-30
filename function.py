# https://codelabs.developers.google.com/codelabs/secret-manager-python#10

from google.cloud import secretmanager
def access_secret_version(secret_id, PROJECT_ID, version_id="latest"):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{PROJECT_ID}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(request={"name": name})

    # Return the decoded payload.
    return response.payload.data.decode('UTF-8')
    
import hashlib

def secret_hash(secret_value): 
  # return the sha224 hash of the secret value
  return hashlib.sha224(bytes(secret_value, "utf-8")).hexdigest()

gcp = secret_hash(access_secret_version("my-secret", "new-417205"))
print(gcp)
secretPrint = access_secret_version("my-secret", "new-417205")
print(secretPrint)