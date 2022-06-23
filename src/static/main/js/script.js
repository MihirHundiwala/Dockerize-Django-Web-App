let hvar = document.getElementById('gameison_heading');
let text = hvar.innerHTML;
let chars=text.split("");
hvar.innerHTML="";

for(let i=0;i<chars.length;i++)
{
	hvar.innerHTML+="<span>" + chars[i] + "</span>";
}
let timer=setInterval(onTick1,50);
let char=0;

function onTick1(){
	let span= hvar.getElementsByTagName('span')[char];
	span.className='fade';
	char++;
	if (char === chars.length){
		clearInterval(timer);
		char=0;
		timer=setInterval(onTick2,50);
		return;
	}
}

function onTick2(){
	let span= hvar.getElementsByTagName('span')[char];
	span.className='';
	char++;
	if (char === chars.length){
		clearInterval(timer);
		char=0;
		timer=setInterval(onTick1,50);
		return;
	}
}


function leavepage(){
	let answer = confirm('Are you sure you want to leave this website?');
	if(answer){
		return true;
	}
	else{
		return false;
	}
}