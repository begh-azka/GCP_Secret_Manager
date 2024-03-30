from google.cloud import secretmanager
client   = secretmanager.SecretManagerServiceClient()
name     = f"projects/new-417205/secrets/password/versions/latest"
response = client.access_secret_version(request={"name": name})
print(response)
