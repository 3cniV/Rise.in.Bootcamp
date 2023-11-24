from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    """Return a friendly HTTP Greeting."""
    print("I am inside Hello World.")
    return 'Hello World.!'


@app.route('/echo/<name>')
def echo(name) :
    """echo <name>"""

    return f"Hello {name}"

if __name__ == '__name__':
    app.run(host='127.0.0.1', port=8080, debug=True)

