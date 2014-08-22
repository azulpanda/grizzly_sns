$(document).ready(function(){
	var time=5;

	$.ajax({
		url:'/newsfeed',
		type:'POST',
		data:{'start':0, 'end':5},
		success:function(response){
			$('.posts_here').append(response);
		}
	});


	$(window).scroll(function() {
		if($(window).scrollTop() + $(window).height() == $(document).height()) {
			if($('.no_more').length == 0){
				$.ajax({
					url:'/newsfeed',
					type:'POST',
					data:{'start':time, 'end':time+5},
					success:function(response){
						$('.posts_here').append(response);
					}
				});
				time = time+5;
			}
		}
	});
});
