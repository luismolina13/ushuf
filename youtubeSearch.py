#!/usr/bin/python

from apiclient.discovery import build

# Set DEVELOPER_KEY to the "API key" value from the "Access" tab of the
# Google APIs Console http://code.google.com/apis/console#access
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyBY58aP8fFT9U_G3Q-zQaC3t9B49ZzOHVc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
  developerKey=DEVELOPER_KEY)

def log(str):
  print "@@@@@@@@"

def get_next_video(videoId, liked):
  nextId = ""
  log("Looking for the next video to play based user preferences")
  if (liked == True) :
    nextId = getNext(videoId)
  else :
    searchNew()

  return nextId

def getNext(videoId):  
  log("Looking for next video")  
  return youtube_search(videoId)

def searchNew():
  log("Searching for a new video")

def youtube_search(videoId):

  search_response = youtube.search().list(
    q=videoId,
    part="id,snippet",
    maxResults=5,
    type="video"
  ).execute()

  search_query = ""

  # There is only going to be one item in this search
  for search_result in search_response.get("items", []):
    search_query += search_result["snippet"]["title"]
    log(search_query)

  search_response = youtube.search().list(
    q=search_query,
    part="id,snippet",
    maxResults=10,
    type="video",
    safeSearch="strict"
  ).execute()  

  videos = []

  nextVideo = ""

  # There is only going to be one item in this search
  for search_result in search_response.get("items", []):
    if(search_result["snippet"]["title"] != search_query):        
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))    
      if(nextVideo == ""):
        nextVideo = search_result["id"]["videoId"]

  # print "Videos:\n", "\n".join(videos), "\n"

  log(nextVideo)

  return nextVideo



