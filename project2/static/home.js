// Launch this when the page has finished loading
document.addEventListener('DOMContentLoaded', () => {

	// Connect to the websocket being used
	var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port)

	// When a new channel has been created run this block
	socket.on('new channel', () => {
		// Add the new channel to the top of the home page
	})
})