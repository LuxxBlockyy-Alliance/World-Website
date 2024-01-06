from flask import Flask, render_template

app = Flask(__name__, template_folder='website')


@app.route('/')
def hello():
    return render_template('index.html')


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='172.17.0.3')
