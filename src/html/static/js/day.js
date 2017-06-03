function startDay() {


	function updateDay() {
		//
		httpGetAsync("/info/today", updateDayAsync)
		//
	}


    function updateDayAsync(dayinfoStr) {
		//
		// Parse string into JSON object
		try {
		    var dayinfoJson = JSON.parse(dayinfoStr);
		} catch(err) {
		    var dayinfoJson = false;
		}
		//
		// Update HTML
		try {
            if (dayinfoJson) {
                updatePage(dayinfoJson);
            } else {
                throw "null response";
            }
        } catch(err) {}
        //
        // Set time for next update
        var wait = 900000; //15min
        setTimeout(updateDay, wait);
        //
    }


    function updatePage(info) {
        //
        //carers
        carers = info.carers
        for (var x in carers) {
            //
            var c = carers[x];
            //
            var dtStart = new Date(c.start + "Z");
            var dtEnd = new Date(c.end + "Z");
            //
            var leftStart = getTimePercent(dtStart);
            var leftEnd = getTimePercent(dtEnd);
            var width = leftEnd - leftStart;
            //
            var divCarer = document.createElement("div");
            divCarer.className = "carer-block material-col-grey-300";
            divCarer.style.left = leftStart.toString().concat("%");
            divCarer.style.width = width.toString().concat("%");
            //
            var spanCarerName = document.createElement("span");
            spanCarerName.innerHTML = c.name;
            //
            divCarer.appendChild(spanCarerName);
            //
            document.getElementById("day-contents").appendChild(divCarer);
        }
        //
        return true
    }


    function updateNowBar() {
        //
        var now = new Date();
        var percentSeconds = getTimePercent(now);
        //
        var newStyle = percentSeconds.toString().concat("%");
        //
        document.getElementById("bar_now").style.left = newStyle;
        //
    }


    function createHourBars() {
        //
        for (var i=1;i < 23; i++) {
            if (i != 12) {
                //
                var percentSeconds = 100 * (i * 60 * 60)/(24 * 60 * 60);
                //
                var spanBar = document.createElement("span");
                spanBar.className = "bar bar_hour";
                spanBar.style.left = percentSeconds.toString().concat("%");
                document.getElementById("bars").appendChild(spanBar);
            }
        }
        //
    }


    function getTimePercent(dt) {
        //
        var secondsInADay = 24 * 60 * 60;
        //
        var hours = dt.getHours() * 60 * 60;
        var minutes = dt.getMinutes() * 60;
        var seconds = dt.getSeconds();
        var totalSeconds = hours + minutes + seconds;
        //
        var percentSeconds = 100 * totalSeconds/secondsInADay;
        //
        return percentSeconds;

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

    createHourBars();

    updateNowBar();
	setInterval(updateNowBar, 900000); //15min

	updateDay();

}