from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    km = request.args.get("km", "")
    if km:
        mile = mile_from(km)
    else:
        mile = ""

    return (
        	"""<h2> Convert Kilometers to Miles! </h2>"""
		"""<br>"""
		"""<form action="" method="get">
                <input type="text" name="km">
                <input type="submit" value="Convert">
            </form>"""
        + "Miles: "
        + '<a id="mile">' +mile+ '</a>'

    )
 
@app.route("/<int:km>")
def mile_from(km):
    """Convert kms to Miles."""
    mile = float(km) * 0.621371
    mile = round(mile, 2) 
    return str(mile)

@app.route("/<string:script>")
def run(script):
    script=request.args.get("script", "")
    return (
	"""<h2> Run! 🕸 </h2>"""
	"""<form action="" method="get">
                <input type="text" name="script">
                <input type="submit" value="Run">
            </form>"""
    + '<a id="script">' + script + '</a>'
) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
     #app.run(host="0.0.0.0", port=8080, debug=False)
