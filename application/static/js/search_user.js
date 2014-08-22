function start_follow(id) {
	$.ajax({
		url:'/start_follow/'+id,
		type:'POST'
	});
}

$(document).ready(function(){
	var go_search = $.ajax();
	$('#user_input').keyup(function(){
		if(go_search){
			go_search.abort();
		}
		$('.search_output').empty();
		var username = $('#user_input').val();
		if(username!=""){
			go_search = $.ajax({
				url:'/search_user',
				type:'POST',
				data:{'username':username},
				success:function(response){
					var user_list = $.parseJSON(response);
					for(var i=0; i<user_list.length; i++){
						$('.search_output').append('<div class="btn listed" onclick="start_follow('+user_list[i]['user_id']+')">'+user_list[i]['username']+'('+user_list[i]['email']+')'+'</div>');
					}
				}
			});
		}
	});
});