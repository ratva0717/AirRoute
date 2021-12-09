$(function() {
    $("try").click(function() {
        let formData = $('.counterValue').text;
        $.ajax({
            url: "/Increment", // fix this to your liking
            type: "POST",
            data: { 'new_data': formData },
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});