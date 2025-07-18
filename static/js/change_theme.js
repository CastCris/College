console.log(document.cookie);
function get_cookie(cookie_name){
	cookie_all=document.cookie.replace(/;/g,'').split(' ');
	//console.log(cookie_all);
	for(var i=0;i<cookie_all.length;++i){
		splited_i=cookie_all[i].split('=');
		let var_name=splited_i[0];
		let var_cont=splited_i[1];
		if(var_cont===undefined||!var_cont.length)
			continue;
		if(var_name==cookie_name){
			console.log(var_name+' '+var_cont);
			return var_cont
		}
	}
	return null
}
function change_theme(){
	const root=document.documentElement;
	const button=document.getElementById("light_night");
	//
	let light=get_cookie("light");
	if(light===undefined)
		light=0;
	light=Number(light);
	light=!light
	//
	if(light)
		light=1
	else
		light=0
	//
	// console.log(light);
	var text_color="";
	var back_color="";
	var text_button="";
	if(light){  // Light theme
		text_color="black";
		back_color="white";
		text_button="night";
	}else{ // Dark theme
		text_color="white";
		back_color="black";
		text_button="light";
	}
	//
	root.style.setProperty("--text-color",text_color);
	root.style.setProperty("--back-color",back_color);
	//
	button.textContent=text_button;
	//
	//console.log(light);
	//console.log(!light);
	document.cookie="light="+light;
}
