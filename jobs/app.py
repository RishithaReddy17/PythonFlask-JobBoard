from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')


# @app.route('/')
# def index():
#     return "Hello, World!"

# if __name__ == '__main__':
#     app.run(debug=True)