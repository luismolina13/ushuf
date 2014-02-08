function queueVideo(videoID) {	
	nextVideo = videoID;	
	currentVideo = nextVideo;
}

function videoLiked() {	
	// alert("videoLiked");
	loadXMLDoc("POST", "/like", true, queueVideo, "videoID="+currentVideo);
}

function videoUnLiked() {	
	loadXMLDoc("POST", "/unlike", true, showMssg, "videoID="+currentVideo);
}