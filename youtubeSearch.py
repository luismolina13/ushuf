#!/usr/bin/python

from apiclient.discovery import build
from optparse import OptionParser

import re
import difflib
import json
import urllib

# Set DEVELOPER_KEY to the "API key" value from the "Access" tab of the
# Google APIs Console http://code.google.com/apis/console#access
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyBY58aP8fFT9U_G3Q-zQaC3t9B49ZzOHVc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
FREEBASE_SEARCH_URL = "https://www.googleapis.com/freebase/v1/search?%s"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
  developerKey=DEVELOPER_KEY)

def log(str):
  print "@@@@@@@@", str

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

def get_topic_id(search_query):
  freebase_params = dict(query="Amazing goals", key=DEVELOPER_KEY)
  freebase_url = FREEBASE_SEARCH_URL % urllib.urlencode(freebase_params)
  freebase_response = json.loads(urllib.urlopen(freebase_url).read())

  if len(freebase_response["result"]) == 0:
    log("No matching terms were found in Freebase.")

  mids = []
  index = 1
  print "The following topics were found:"
  for result in freebase_response["result"]:
    mids.append(result["mid"])
    print "  %2d. %s (%s)" % (index, result.get("name", "Unknown"),
      result.get("notable", {}).get("name", "Unknown"))
    index += 1

  mid = None
  while mid is None:
    index = raw_input("Enter a topic number to find related YouTube %ss: " %
      "video")
    try:
      mid = mids[int(index) - 1]
    except ValueError:
      pass
  return mid

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
    # log(search_query)

  log(search_query)
  get_topic_id(search_query)

  search_response = youtube.search().list(
    q=search_query,
    part="id,snippet",
    maxResults=10,
    type="video",
    safeSearch="strict"
  ).execute()  

  videos = []

  nextVideo = ""
  nextTitle = ""

  # There is only going to be one item in this search
  for search_result in search_response.get("items", []):
    if(search_result["snippet"]["title"] != search_query):        
      # videos.append("%s (%s)" % (search_result["snippet"]["title"],
      #                            search_result["id"]["videoId"]))    
      if(nextVideo == ""):
        nextVideo = search_result["id"]["videoId"]
        nextTitle = search_result["snippet"]["title"]

  s1w = re.findall('\w+', search_query.lower())
  s2w = re.findall('\w+', nextTitle.lower())

  common_ratio = difflib.SequenceMatcher(None, s1w, s2w).ratio()
  ratio = '%.1f%% of words common.' % (100*common_ratio)
  log(ratio)

  # print "Videos:\n", "\n".join(videos), "\n"

  # log(nextTitle)

  return nextVideo



