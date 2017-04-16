function openSideSlide() {
    $("#restaurantDetail").css("width", "30%");

    $('#giveGoodFeedback').tooltip();
    $('#giveBadFeedback').tooltip();
}

function closeSideSlide() {
    if (selectedMarker !== null) {
        selectedMarker.setIcon(null);
        selectedMarker.setShadow(null);
    }

    $("#restaurantDetail").hide();
    $("#restaurantDetail").animate({'width': '0' }, function() {
        $("#restaurantDetail").show();
    });
}