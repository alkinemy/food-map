$(document).ready(function() {
    $('#restaurantDetailContent').on('click', '#giveGoodFeedback', function(event) {
        event.preventDefault();

        $.ajax({
            method: 'POST',
            url: '/restaurants/' + $(this).data('restaurant-id') + '/feedback/good'
        }).done(function(response) {
            $("#goodFeedbackCount").html(response.good);
            toastr.success('추천하였습니다!', '감사합니다!', {"positionClass": "toast-bottom-center"});
        }).fail(function() {
            toastr.error('개발자에게 연락주세요 흑흑', '실패했습니다!', {"positionClass": "toast-bottom-center"});
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
            toastr.error('개발자에게 연락주세요 흑흑', '실패했습니다!', {"positionClass": "toast-bottom-center"});
        });
    });


    $('#restaurantDetailContent').on('submit', '#commentRegisterForm', function(event) {
        event.preventDefault();

        var csrfToken = $(this).find('input[name="csrf_token"]').val();
        var data = toJsonWithoutCsrfToken($(this).serializeArray());
        console.log(typeof data)
        $.ajax({
            beforeSend: function(xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrfToken);
                }
            },
            method: 'POST',
            contentType: 'application/json',
            url: $(this).attr('action'),
            data: JSON.stringify(data)
        }).done(function(commentView) {
            $('#restaurantCommentList').empty();
            $('#restaurantCommentList').append(commentView);
            $('#commentRegisterForm textarea').val('');
            toastr.success('댓글이 입력되었습니다!', '감사합니다!', {"positionClass": "toast-bottom-center"});
        }).fail(function(message) {
            toastr.error(message, '실패했습니다!', {"positionClass": "toast-bottom-center"})
        });
    });

    function toJsonWithoutCsrfToken(data) {
        var result = {}
        data.forEach(function(element) {
            if (element.name !== 'csrf_token') {
                result[element.name] = element.value;
            }
        });
        return result;
    }

});
