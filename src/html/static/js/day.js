function startDay() {


	function updateDay() {
		//
		httpGetAsync("/info/today", updateDayAsync)
		//
	}


    function updateDayAsync(dayStr) {
		//
		// Parse string into JSON object
		try {
		    var dayJson = JSON.parse(dayStr);
		} catch(err) {
		    var dayJson = false;
		}
		//
		// Get label and update HTML
		var label = ""
		//
		try {
            if (dayJson) {
                label = dayJson.carer.label;
                if (!label) {throw "error in response"}
            } else {
                throw "null response";
            }
        } catch(err) {
            label = "I'm sorry, I don't know who your next carer will be. I'll try to find out again in a little while.";
        }
        //
        updatePage(dayJson);
        //
        // Set time for next update
        var wait = 60000; //1min
        setTimeout(updateDay, wait);
        //
    }


    function updatePage(info) {
        //
    }


    function updateNowBar() {
        //
        var secondsInADay = 24 * 60 * 60;
        //
        var now = new Date();
        var hours = now.getHours() * 60 * 60;
        var minutes = now.getMinutes() * 60;
        var seconds = now.getSeconds();
        var totalSeconds = hours + minutes + seconds;
        //
        var percentSeconds = 100 * totalSeconds/secondsInADay;
        //
        var newStyle = percentSeconds.toString().concat("%");
        //
        document.getElementById("now_bar").style.left = newStyle;
        //
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

    updateNowBar();
	setInterval(updateNowBar, 900000); //15min

//	updateDay();

}