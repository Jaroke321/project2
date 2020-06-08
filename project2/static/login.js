document.addEventListener('DOMContentLoaded', () => {

	// Grab all of the objects from the form
	let submit = document.querySelector('#submit');
	let un = document.querySelector('.un');
	let pass = document.querySelector('.pass');
	// By defautl set the submit button to be disabled
	submit.disabled = true;
	submit.className = "disabled-btn";

	// Set a listener for when the user is typing in their username
	un.onkeyup = () => {
		// Check that the user has also typed in a password
		if((pass.value.length > 0) && (un.value.length > 0)) {
			// Enable the button
			submit.disabled = false;
			submit.className = "submit";
		} else {
			submit.disabled = true;
			submit.className = "disabled-btn";
		}
	};

	// Set a listener for when the user is typing in their password
	pass.onkeyup = () => {
		// Check that the user has also typed in a password
		if((un.value.length > 0) && (pass.value.length > 0)) {
			// Enable the button
			submit.disabled = false;
			submit.className = "submit";
		} else {
			submit.disabled = true;
			submit.className = "disabled-btn";
		}
	};

});

