///https://www.youtube.com/watch?v=nF9riePnm80

$(function(){
	$('button').click(function(){
		var email = $('#corp_email').val();
		var surveyLink = $('#survey_id').val();
		var numOfResponses = $('#num_of_resp').val();
		var responseType = $('#resp_type').val();
		$.ajax({
			url: '/',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});