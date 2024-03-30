import functions_framework

@functions_framework.http
def getSecretValue(request):
    
   request_json = request.get_json(silent=True)
   from google.cloud import secretmanager
   client   = secretmanager.SecretManagerServiceClient()
   name     = f"projects/new-417205/secrets/password/versions/latest"
   response = client.access_secret_version(request={"name": name})
   payload  = response.payload.data.decode("UTF-8")
   print(payload)

   return payload
