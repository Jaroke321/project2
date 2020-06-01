from project2 import app

@app.route("/")
def index():
	"""Main page"""

	return "Hello, World"