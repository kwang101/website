from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/posts')
def posts():
	return render_template('posts.html')

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)