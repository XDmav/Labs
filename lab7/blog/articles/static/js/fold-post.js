var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i<foldBtns.length; i++){
	foldBtns[i].addEventListener("click", function(e) {
        if (e.target.parentElement.className == "one-post folded"){
            e.target.innerHTML = "Свернуть";
            e.target.parentElement.className = "one-post";
        }
        else{
            e.target.innerHTML = "Развернуть";
            e.target.parentElement.className = "one-post folded";
        }
    });
}