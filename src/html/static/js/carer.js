function startCarer() {


	function updateCarer() {
		//
		httpGetAsync("/carers/now-or-next", updateCarerAsync)
		//
	}


    function updateCarerAsync(carerStr) {
		//
		// Parse string into JSON object
		try {
		    var carerJson = JSON.parse(carerStr);
		} catch(err) {
		    var carerJson = false;
		}
		//
		// Get label and update HTML
		var label = ""
		//
		try {
            if (carerJson) {
                label = carerJson.carer.label
                if (!label) {throw "error in response"}
            } else {
                throw "null response"
            }
        } catch(err) {
            label = "I'm sorry, I don't know who your next carer will be. I'll try to find out again in a little while."
        }
        //
        updateLabel(label)
        //
        // Set time for next update
        var wait = 10000 //10sec
        //
        try {
            if (carerJson) {
                //
                var dtStart = new Date(carerJson.carer.start + "Z");
                var dtEnd = new Date(carerJson.carer.end + "Z");
                //
                var dtNow = new Date();
                //
                if (dtStart < dtNow) {
                    wait = dtNow - dtEnd
                } else if (dtStart > dtNow) {
                    wait = dtStart - dtNow
                } else {
                    throw "error in response"
                }
                //
            } else {
                throw "null response"
            }
        } catch(err) {
            wait = 300000  //5mins
        }
        //
        setTimeout(updateCarer, wait)
        //
    }


    function updateLabel(label) {
        document.getElementById("msg-carer").innerHTML = label;
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


	updateCarer();

}