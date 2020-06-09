
let current_offset = 0;      // Start with the first channel

const limit = 10;            // Number of channels to load

document.addEventListener('DOMContentLoaded', () => {

	// Call the load function once the page has loaded
	load();

	// Get the search bar as an object
	let search = document.querySelector('.search-input');

	// Create a listener for when the user types into the search bar
	search.onkeyup = () => {

		// Check that there is content inside of the search bar
		if (search.value.length > 3) {
			searching(search.value);
		}
	};

	// if the user scrolls to the bottom of the page, load more channels
	window.onscroll = () => {

		// Call the load function when the user scrolls to the bottom of the screen
		if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
			load();
		}
	};

});

// Function that makes request ot get more channels
function load() {

	// Get the current offset for the request and then update the offset 
	offset = current_offset;
	current_offset += limit;
	// Create a request object that is pointed towards the /channels path
	const request = new XMLHttpRequest();
	request.open('POST', '/channels');

	// Run this code when the data comes back from the server
	request.onload = () => {
		const data = JSON.parse(request.responseText);  // Parse the incoming data
		data.forEach(add_channel);
	};

	// Create a new form and append our offset and limit values
	const data = new FormData();
	data.append('offset', offset);
	data.append('limit', limit);

	// send request
	request.send(data);
};

// Function that creates a new channel element and adds it to the existing channels on the home page
function add_channel(name) {

	// Create the outer div element
	const channel = document.createElement('div');
	channel.className = 'channel-item';  // Give this div the class channel-item

	// Create the child div to channel
	const inner_div = document.createElement('div');
	inner_div.className = 'border-btm';  // Giv this dic the class border-btm

	// Create both inner span elements to hold the channel title and number of followers
	const span1 = document.createElement('span');
	span1.className = 'channel-title';
	span1.innerHTML = name;  // Set the text for this span to the name returned by the server

	const span2 = document.createElement('span');
	span2.className = 'text-secondary spacer-lg';
	span2.innerHTML = 'Followers : 0';

	// configure all of the elements in order
	inner_div.append(span1);
	inner_div.append(span2);
	// Add the inner eleents to the outer most div element
	channel.append(inner_div);

	// Add the channel to the DOM
	document.querySelector('#channels').append(channel);
};

// Function sends request to the server so that
function searching(val) {

	// Create a request object pointed at the search route on the server
	const req = new XMLHttpRequest();
	req.open('POST', '/search');

	// Handle data once it returns from the server
	req.onload = () => {
		const data = JSON.parse(req.responseText);
	};

	// Package the search data that the user entered
	const data = new FormData();
	data.append('text', val);
	// Send the request
	req.send(data);
};



