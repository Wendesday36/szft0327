function validateForm() {
	let x = document.validTeszt.knev.value;
	if (x === "") {
    	alert("A mező kitöltése kötelező!");
    	return false;
	}
return true;
}
