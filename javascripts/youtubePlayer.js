var currentVideo = "rcatzGEG3ro";

// Update a particular HTML element with a new value
function updateHTML(elmId, value) {
  document.getElementById(elmId).innerHTML = value;
}

// Loads the selected video into the player.
function loadVideo() {
  var selectBox = document.getElementById("videoSelection");
  var videoID = selectBox.options[selectBox.selectedIndex].value
  
  if(ytplayer) {
    ytplayer.loadVideoById(videoID);
  }
}

// EVENT TRIGGERS
function onPlayerStateChange(playerState) {
  if(playerState == 0) {
    alert("VideoEnded");
  }
  if(playerState == 5) {
    alert("VideoReadytoPlay");
  }
}

// This function is called when an error is thrown by the player
function onPlayerError(errorCode) {
  alert("An error occured of type:" + errorCode);
}

// This function is automatically called by the player once it loads
function onYouTubePlayerReady(playerId) {
  ytplayer = document.getElementById("ytPlayer");
  ytplayer.playVideo();
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