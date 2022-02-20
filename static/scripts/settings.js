
// get the user_email from the session
let current_user_email = $("#current_user").val();

jQuery.when(jQuery.getJSON("/get_security_question?user_email=" + current_user_email)).done(function(data) {

    // checking for NA because NA is returned as the question if the user is not found
    if (data.question == "NA") {
        $("#current_question").val("No security question set");
        $("#current_answer").hide();
        return;

    } else {
        $("#current_question").val(data.question);
    }
});