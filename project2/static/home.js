
let current_offset = 0;      // Start with the first channel

const limit = 10;    // Number of channels to load

document.addEventListener('DOMContentLoaded', load);

// if the user scrolls to the bottom of the page, load more channels
window.onscroll = () => {

	if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
		load();
	}
};

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

function add_channel(name) {

	const channel = document.createElement('div');
	channel.className = 'channel-item';

	const inner_div = document.createElement('div');
	inner_div.className = 'border-btm';

	const span1 = document.createElement('span');
	span1.className = 'channel-title';
	span1.innerHTML = name;

	const span2 = document.createElement('span');
	span2.className = 'text-secondary spacer-lg';
	span2.innerHTML = 'Followers : 0';

	inner_div.append(span1);
	inner_div.append(span2);
	channel.append(inner_div);

	// Add the channel to the DOM
	document.querySelector('#channels').append(channel);
}




