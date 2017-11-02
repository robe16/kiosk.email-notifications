window.onload=function() {
    startClock_dem();
    startCarer();
    startMessages();
    startDay();

    setTimeout(function () {
            if (newState == -1) {
                location.reload(true);
            }
        }, 1800000); //30 minutes

}