(function ($) {
    $(function () {

        $('.button-collapse').sideNav();

    });

    $(function () {

        $('select').material_select();

    });

    $('#favorite').click(function () {
        var fc = $('#favorite_count');
        if ($(this).text() === 'star') {

            $(this).html('star_border');
            fc.html((parseInt(fc.text()) - 1).toString())
        }
        else {
            $(this).html('star');
            fc.html((parseInt(fc.text()) + 1).toString())
        }
    });

    $('#stock_dec').click(function () {
        var count = $('#stock_count');
        if (count.val() > 0) {
            count.val((parseInt(count.val()) - 1).toString());
        }
    });

    $('#stock_inc').click(function () {
        var count = $('#stock_count');
        count.val((parseInt(count.val()) + 1).toString());
    });

})
(jQuery);

