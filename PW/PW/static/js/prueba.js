var i = 0;
$(document).on("ready", main);

function cambiarSlider(){
	i++;
	if(i == $("#section4_2 img").size()){
		i = 0;
	}
	$("#section4_2 img").hide();
	$("#section4_2 img").eq(i).fadeIn("medium");
}




function main(){
	var control = setInterval(cambiarSlider, 3000);
}

