const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
function OnSignin(){
	var form_data = new FormData();
	form_data.append("csrfmiddlewaretoken", csrftoken);
	form_data.append("username", $("#username").val())
	form_data.append("password",  $("#password").val())
	$.ajax({
		type: "POST",
		// What kind of addres our server expectin for (gonna handle sended data)
		url: "/login/verify/",
		// Data to send on server
		// I need pass to server parent name because I need to hide one of field (ManyToMany django DB relation)
		data: form_data,
		// If we use FormData you have to specify them
		processData: false,
		contentType: false,
		// For activating feature of django csrf-tokent protection
		headers: {'X-CSRFToken': csrftoken},
		mode: 'same-origin', // Do not send CSRF token to another domain.
		success: function(result) {
			$("#common-error").removeClass('error success')	
			$("#common-error").addClass('success')	
			$("#common-error").text(result.common)	
			// Redirect to login page
			setTimeout(function(){
				window.location.href = '/'
			},3000)
		},
		error: function(jqXHR, textStatus, errorThrown){
			$("#common-error").removeClass('error success')	
			$("#common-error").addClass('error')	
			$("#common-error").text(jqXHR.responseJSON.common)	
		}
	});
}

$(document).ready( function(){
	$("#signin").on('click',OnSignin)
})
