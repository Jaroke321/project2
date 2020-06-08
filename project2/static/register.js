document.addEventListener('DOMContentLoaded', () => {

	// Grab all of the objects that are apart of the form
	un = document.querySelector('.un');
	pass = document.querySelector('#pass');
	c_pass = document.querySelector('#cPass');
	submit = document.querySelector('#submit')

	// Start by disabling the submit button
	submit.disabled = true;
	submit.className = "disabled-btn";

	// Set a listener for when the user is typing in the username field
	un.onkeyup = () => {
		if ((un.value.length > 0) && (pass.value.length > 0) && (c_pass.value === pass.value)) {
			submit.disabled = false;
			submit.className = "submit";
		} else {
			submit.disabled = true;
			submit.className = "disabled-btn";
		}
	};

	// Set a listener for when the user is typing in the pass field
	pass.onkeyup = () => {
		if ((un.value.length > 0) && (pass.value.length > 0) && (c_pass.value === pass.value)) {
			submit.disabled = false;
			submit.className = "submit";
		} else {
			submit.disabled = true;
			submit.className = "disabled-btn";
		}
	};

	// Set a listener for when the user is typing in the second pass field
	c_pass.onkeyup = () => {
		if ((un.value.length > 0) && (pass.value.length > 0) && (c_pass.value === pass.value)) {
			submit.disabled = false;
			submit.className = "submit";
		} else {
			submit.disabled = true;
			submit.className = "disabled-btn";
		}
	};
});