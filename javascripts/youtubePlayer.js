var currentVideo = "vdRr97u41Rg";
var nextVideo = "";

// Update a particular HTML element with a new value
function updateHTML(elmId, value) {
  document.getElementById(elmId).innerHTML = value;
}

// Play video and set a timer to determine if they liked 
// this video or not. 
function playVideo() {
  if(ytplayer) {    
    ytplayer.playVideo();
    halfVideoDuration = (ytplayer.getDuration() * 1000) / 2;
    // alert(halfVideoDuration);
    setTimeout(function() {videoLiked();},halfVideoDuration);
  }
}

// EVENT TRIGGERS
function onPlayerStateChange(playerState) {
  switch(playerState) {
    case 0: // ENDED    
      ytplayer.loadVideoById(nextVideo);      
      playVideo();    
      break;
    case 1: // PLAYING      
      break;
    case 2: // PAUSED
      break;
    case 3: // BUFFERING
      break;    
    case 5: // CUED       
      break;
  }    
}

// This function is called when an error is thrown by the player
function onPlayerError(errorCode) {
  alert("An error occured of type:" + errorCode);
}

// This function is automatically called by the player once it loads
function onYouTubePlayerReady(playerId) {
  ytplayer = document.getElementById("ytPlayer");
  playVideo();
  ytplayer.addEventListener("onError", "onPlayerError");
  ytPlayer.addEventListener("onStateChange", "onPlayerStateChange");  
}

// The "main method" of this sample. Called when someone clicks "Run".
function loadPlayer() {
  // The video to load
  var videoID = currentVideo;
  // Lets Flash from another domain call JavaScript
  var params = { allowScriptAccess: "always" };
  // The element id of the Flash embed
  var atts = { id: "ytPlayer" };
  // All of the magic handled by SWFObject (http://code.google.com/p/swfobject/)
  swfobject.embedSWF("http://www.youtube.com/v/" + videoID + 
                     "?version=3&enablejsapi=1&playerapiid=player1", 
                     "videoDiv", "480", "295", "9", null, null, params, atts);
}
function _run() {
  loadPlayer();
}
google.setOnLoadCallback(_run);