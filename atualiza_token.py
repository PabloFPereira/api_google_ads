from google_auth_oauthlib.flow import InstalledAppFlow

flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/adwords']
)

creds = flow.run_local_server(port=0)

print('Refresh token:', creds.refresh_token)
