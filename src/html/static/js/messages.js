function startMessages() {


	function updateMessages() {
		//
		httpGetAsync("/messages/current", updateMessagesAsync);
		//
	}


    function updateMessagesAsync(msgStr) {
		//
		// Parse string into JSON object
		try {
		    var msgJson = JSON.parse(msgStr);
		} catch(err) {
		    var msgJson = false;
		}
		//
		// Get label and update HTML
		var divMsgs = document.createElement("div");
		//
		try {
            if (msgJson) {
                divMsgs = createMsgDiv(msgJson.messages)
            } else {
                throw "null response";
            }
        } catch(err) {
            var divMsgs = document.createElement("div");
            divMsgs.innerHTML = "I'm sorry, messages are unavailable at the moment. I will try to retireve them again shortly.";
        }
        //
        updateDiv(divMsgs);
        //
        setTimeout(updateMessages, 300000); //5mins
        //
    }


    function createMsgDiv(messages) {
        //
        var divMsgs = document.createElement("div");
        //
        for (var x in messages) {
            //
            var divM = document.createElement("div");
            divM.id = "msg_" + x.toString();
            divM.className = "msg";
            divM.innerHTML = messages[x];
            //
            divMsgs.appendChild(divM);
            //
        }
        //
        return divMsgs;
        //
    }


    function updateDiv(divMsgs) {
        document.getElementById("messages").innerHTML = ""
        document.getElementById("messages").appendChild(divMsgs);
    }


    function httpGetAsync(url, callback) {
        try {
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                    callback(xmlHttp.responseText);
            }
            xmlHttp.open("get", url, true);
            xmlHttp.send(null);
        } catch(err) {
            callback(false);
        }
    }


	updateMessages();

}