//----------Password Reset----------//


// get the user_email from the hideen input from the form
let current_user_email = $("#current_user").val();

// get the user's security question from the database
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



//----------Task View Customization----------//



//check database to see what customization options the user set
function api_get_settings(success_function) {

    $.ajax({
        url: '/api/settings', type: "GET",
        success: success_function
    });
}

api_get_settings(function(result){
    let type = "";
    let shown = 0;

    for(const setting of result.settings) {
        type = setting.upcoming_type
        shown = setting.upcoming_shown
    }

    console.log("type: " + type + " shown: " + shown)
})


//display the customization options that the user has set on the settings page

//when the user clicks the submit button on task view customzation div:
//put the values selected into the databse
//now go to task view and display tasks according to those values