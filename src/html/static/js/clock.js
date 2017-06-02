var tday=new Array("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday");
var tmonth=new Array("January","February","March","April","May","June","July","August","September","October","November","December");	


function startClock() {
	
	function createClock() {
		var d=new Date();
		var nday=d.getDay(),nmonth=d.getMonth(),ndate=d.getDate(),nyear=d.getFullYear();
		var nhour=d.getHours(),nmin=d.getMinutes();nsec=d.getSeconds();
		if(nmin<=9) nmin="0"+nmin;
		if(nsec<=9) nsec="0"+nsec;
		//
		var date=""+tday[nday]+", "+ndate+" "+tmonth[nmonth]+" "+nyear+"";
		document.getElementById("date").innerHTML = date;
		//
		document.getElementById("hour").innerHTML = nhour;
		document.getElementById("minute").innerHTML = nmin;
		document.getElementById("second").innerHTML = nsec;
		//
	}


	createClock();
	setInterval(createClock, 1000); //1sec

}


function startClock_dem() {

	function createClock_dem() {
		var d=new Date();
		var nday=d.getDay();
		var nhour=d.getHours();
		//
		if (nhour<12) {
		    sTime = "morning";
		} else if (nhour<18) {
		    sTime = "afternoon"
		} else {
		    sTime = "night"
		}

		//
		var sDatetime = "Now it's ".concat(tday[nday], " ", sTime);
		//
		document.getElementById("date_dem").innerHTML = sDatetime;
		//
	}

	createClock_dem();
	setInterval(createClock_dem, 300000); //5mins

}