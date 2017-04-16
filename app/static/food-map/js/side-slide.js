function openSideSlide() {
    $("#restaurantDetail").css("width", "30%");

    $('#giveGoodFeedback').tooltip();
    $('#giveBadFeedback').tooltip();
}

function closeSideSlide() {
    $("#restaurantDetail").hide();
    $("#restaurantDetail").animate({'width': '0' }, function() {
        $("#restaurantDetail").show();
    });
}