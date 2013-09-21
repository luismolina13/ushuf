function showMssg(txt) {
	alert(txt);
}

function videoLiked() {	
	loadXMLDoc("POST", "/like", true, showMssg, "videoID="+currentVideo);
}

function videoUnLiked() {
	loadXMLDoc("POST", "/unlike", true, showMssg, "videoID="+currentVideo);
}