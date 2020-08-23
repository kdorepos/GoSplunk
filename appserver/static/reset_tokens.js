require([
        'jquery',
	'splunkjs/mvc',
	'splunkjs/mvc/simplexml/ready!'
    ], function ($, mvc) {
    var tokens = mvc.Components.get("default");
    $('#reset_button').on("click", function(e){
	tokens.set("form.category", "None");
	tokens.set("form.title", "None");
	tokens.set("form.GoSplunk_Query", "None");
    });
});
