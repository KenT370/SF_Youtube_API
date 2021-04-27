# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAZ-KiVyapZQi25rgdm9k3wM8EO01WQfvc"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id="UCKORm8sxh3cheBpqs0akkhg"
    )
    response = request.execute()
    
    
    print(response['items'][0]['statistics']['subscriberCount'])

if __name__ == "__main__":
    main()