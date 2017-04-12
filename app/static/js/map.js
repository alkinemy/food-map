var mapOptions = {
    center: new naver.maps.LatLng(37.5157873, 127.0991124),
    zoom: 12
};

var map = new naver.maps.Map('map', mapOptions);

var markerOptions = {
    position: new naver.maps.LatLng(37.5157873, 127.0991124),
    map: map
};

var marker = new naver.maps.Marker(markerOptions);
