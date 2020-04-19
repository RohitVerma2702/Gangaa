$(document).ready(function () {

	var map;

	function initialize() {

		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(showPosition);
		} else {
			x.innerHTML = "Geolocation is not supported by this browser.";
		}

		function showPosition(position) {
			lati = position.coords.latitude;
			longi = position.coords.longitude;

			document.getElementById("lat").value = lati;
			document.getElementById("long").value = longi;

			var myLatlng = new google.maps.LatLng(lati, longi);

			var myOptions = {
				zoom: 20,
				center: myLatlng,
				mapTypeId: google.maps.MapTypeId.ROADMAP
			};
			map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

			var marker = new google.maps.Marker({
				draggable: true,
				position: myLatlng,
				map: map,
				title: "Your location"
			});

			google.maps.event.addListener(marker, 'dragend', function (event) {
				document.getElementById("lat").value = event.latLng.lat();
				document.getElementById("long").value = event.latLng.lng();
				infoWindow.open(map, marker);
			});
		}
	}
	google.maps.event.addDomListener(window, "load", initialize());

});