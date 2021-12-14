$(document).ready(function() {
    console.log("Yee");
    $("#buttons").click(function() {
        let formData = $('#counterValue').text();
        console.log(formData);
        $.ajax({
            url: "/Increment", // fix this to your liking
            type: "POST",
            data: { 'new_data': formData },
        });
    });
});