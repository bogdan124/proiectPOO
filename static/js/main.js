


	var mymap = L.map('mapid').setView([51.505, -0.09], 13);





	L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1,
		    accessToken: 'sk.eyJ1IjoiYm9nZGFuYmliIiwiYSI6ImNraWVlZjRmZjEwenMyenBvODlkdjVlbmIifQ.zz05kpCXAlAVpxF9JQ0igQ'

	}).addTo(mymap);

	L.marker([51.5, -0.09]).addTo(mymap);



 $.ajax({
     type :"POST",
     url: "/profileData",
     cache: false,
     contentType: "application/json",
     success: function(result) {
        console.log(result);

        L.Routing.control({
          waypoints: [
            L.latLng(result[0][2], result[0][3]),
            L.latLng(57.6792, 11.949)
          ],
            routeWhileDragging: true,
            geocoder: L.Control.Geocoder.nominatim()
        }).addTo(mymap);
            $(".pulse-card-profile").html(result[0][1]);
            $(".altitude-card-profile").html(result[0][6]);
            $(".speed-card-profile").html(result[0][5]);
            $(".speed-card-profile").html(result[0][5]);
            $(".lon-card-profile").html(result[0][2]);
            $(".lat-card-profile").html(result[0][3]);
            $(".date-card-profile").html(result[0][7]);
            $(".satellites-card-profile").html(result[0][4]);
     }
    });

     $.ajax({
     type :"POST",
     url: "/predictdib",
     cache: false,
     contentType: "application/json",
     success: function(result) {
         $(".diabet-user").html(result);
         }
      });

 setInterval(function(){
 $.ajax({
     type :"POST",
     url: "/profileData",
     cache: false,
     contentType: "application/json",
     success: function(result) {
            $(".pulse-card-profile").html(result[0][1]);
            $(".altitude-card-profile").html(result[0][6]);
            $(".speed-card-profile").html(result[0][5]);
            $(".speed-card-profile").html(result[0][5]);
            $(".lon-card-profile").html(result[0][2]);
            $(".lat-card-profile").html(result[0][3]);
            $(".date-card-profile").html(result[0][7]);
            $(".satellites-card-profile").html(result[0][4]);
     }
      });

    }, 3000);

