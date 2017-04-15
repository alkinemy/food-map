$('#restaurantDetailContent').on('click', '#giveGoodFeedback', function(event) {
    event.preventDefault();

    $.ajax({
        method: 'POST',
        url: '/restaurants/' + $(this).data('restaurant-id') + '/feedback/good'
    }).done(function(response) {
        $("#goodFeedbackCount").html(response.good);
        toastr.success('추천하였습니다!', '감사합니다!', {"positionClass": "toast-bottom-center"});
    }).fail(function() {
        toastr.error('개발자에게 연락주세요 흑흑', '실패했습니다!', {"positionClass": "toast-bottom-center"})
    });
});

$('#restaurantDetailContent').on('click', '#giveBadFeedback', function(event) {
    event.preventDefault();

    $.ajax({
        method: 'POST',
        url: '/restaurants/' + $(this).data('restaurant-id') + '/feedback/bad'
    }).done(function(response) {
        $("#badFeedbackCount").html(response.bad);
        toastr.warning('비추천하였습니다!', '감사합니다!', {"positionClass": "toast-bottom-center"});
    }).fail(function() {
        toastr.error('개발자에게 연락주세요 흑흑', '실패했습니다!', {"positionClass": "toast-bottom-center"})
    });
});
