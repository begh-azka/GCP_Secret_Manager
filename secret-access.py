from google.cloud import secretmanager
client   = secretmanager.SecretManagerServiceClient()
name     = f"projects/new-417205/secrets/my-secret/versions/latest"
response = client.access_secret_version(request={"name": name})
payload  = response.payload.data.decode("UTF-8")
print(payload)




# secretmanager.versions.access - to default google app engine service account - for cloudfunction
