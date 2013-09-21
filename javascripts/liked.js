
function loadXMLDoc(method,url,async,onCallBack,postData) {
	var xmlhttp;
	if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
		xmlhttp=new XMLHttpRequest();
	}
	else {// code for IE6, IE5
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
			onCallBack(xmlhttp.responseText);			
		}
	}
	xmlhttp.open(method,url,async);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send(postData);
}

function showMssg(txt) {
	alert(txt);
}

function videoLiked() {	
	loadXMLDoc("POST", "/like", true, showMssg, "videoID="+currentVideo);
}

function videoUnLiked() {
	loadXMLDoc("POST", "/unlike", true, showMssg, "videoID="+currentVideo);
}