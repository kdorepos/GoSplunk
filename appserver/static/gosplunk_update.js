require([
    'jquery',
    'splunkjs/mvc',
    'splunkjs/mvc/simplexml/ready!'
], function ($, mvc) {
var tokens = mvc.Components.get("default");
$('#update_button').on("click", function (e){
    var ok = confirm("Confirm Update: Internet Access is REQUIRED");
    if ( ok==true){
        tokens.set("form.tokUpdate", "| gosplunkupdate");
    } else {
        alert("Update Cancelled");
        tokens.set("form.tokUpdate","| makeresults");
    }
    });
});