function openSideSlide() {
    $("")
    document.getElementById("restaurantDetail").style.width = "30%";
//    document.getElementById("map").style.width = "70%";
}

function closeSideSlide() {
    $("#restaurantDetail").css("width, 0");
    document.getElementById("restaurantDetail").style.width = "0";
//    document.getElementById("map").style.width= "100%";
}