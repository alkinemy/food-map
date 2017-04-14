$('#restaurantDetailContent').on('click', '#giveGoodFeedback', function(event) {
    event.preventDefault();

    $.ajax({
        method: 'POST',
        url: '/restaurants/' + $(this).data('restaurant-id') + '/feedback/good'
    }).done(function(count) {
        $("#goodFeedbackCount").html(count);
        //TODO toast 보여주기
    }).fail(function() {
        //TODO toast 보여주기
    });
});

$('#restaurantDetailContent').on('click', '#giveBadFeedback', function(event) {
    event.preventDefault();

    $.ajax({
        method: 'POST',
        url: '/restaurants/' + $(this).data('restaurant-id') + '/feedback/bad'
    }).done(function(count) {
        $("#badFeedbackCount").html(count);
        //TODO toast 보여주기
    }).fail(function() {
        //TODO toast 보여주기
    });
});
