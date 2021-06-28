import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("jCuh84s3vFjOFH9VUi58vIIr6",
    "VIbmaZCEf6GULkON2e3JvV5sm2DxgbSBKjj0hoq7Zb04VsRxZz")
auth.set_access_token("1322222341301006337-93nQLN4GHcrh9imHEUyuD3kcbSuFir",
    "fmb5NFdnob4ngZ7D6Cbr9oGFFIQwtct9gRnKHn3a4lbPo")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")