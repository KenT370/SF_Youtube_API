#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:15:42 2021

@author: kenneth.torres
"""

import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

def pickle_file_name(
        api_name = 'youtube',
        api_version = 'v3'):
    return f'token_{api_name}_{api_version}.pickle'

def load_credentials(
        api_name = 'youtubeAnalytics',
        api_version = 'v2'):
    pickle_file = pickle_file_name(
        api_name, api_version)

    if not os.path.exists(pickle_file):
        return None

    with open(pickle_file, 'rb') as token:
        return pickle.load(token)

def save_credentials(
        cred, api_name = 'youtubeAnalytics',
        api_version = 'v2'):
    pickle_file = pickle_file_name(
        api_name, api_version)

    with open(pickle_file, 'wb') as token:
        pickle.dump(cred, token)
        
        

def execute_api_request(client_library_function, **kwargs):
  response = client_library_function(
    **kwargs
  ).execute()
  print(response)


def create_service(
        client_secret_file, scopes,
        api_name = 'youtubeAnalytics',
        api_version = 'v2'):
    print(client_secret_file, scopes,
        api_name, api_version,
        sep = ', ')

    cred = load_credentials(api_name, api_version)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                    client_secret_file, scopes)
            cred = flow.run_console()

    save_credentials(cred, api_name, api_version)

    try:
        service = build(api_name, api_version, credentials = cred)
        print(api_name, 'service created successfully')
        return service
    except Exception as e:
        print(api_name, 'service creation failed:', e)
        return None

def main():
    youtube = create_service("client_secret.json",
        ['https://www.googleapis.com/auth/yt-analytics.readonly'])
    if not youtube: return

    youtubeAnalytics = create_service( "client_secret.json",
        ['https://www.googleapis.com/auth/yt-analytics.readonly'])
    execute_api_request(
      youtubeAnalytics.reports().query,
      ids='channel==MINE',
      startDate='2020-01-01',
      endDate='2021-12-31',
      metrics='estimatedMinutesWatched,views,likes,subscribersGained',
      dimensions='day',
      sort='day'
  )
    
    #response = request.execute()

    #print(response)

# -*- coding: utf-8 -*-


if __name__ == '__main__':
    main()
 

  
  
  