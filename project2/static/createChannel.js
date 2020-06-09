document.addEventListener('DOMContentLoaded', () => {

	// Grab the tetbox for channel name
	cn = document.querySelector('.cn');
	btn = document.querySelector('#chan-btn');

	// Disable the button by default
	btn.disabled = true;
	btn.className = "disabled-chan-btn";

	// Create a listener for when the user types
	cn.onkeyup = () => {
		if(cn.value.length > 0) {
			btn.disabled = false;
			btn.className = "create-btn";
		} else {
			btn.disabled = true;
			btn.className = "disabled-chan-btn";
		}
	};
});