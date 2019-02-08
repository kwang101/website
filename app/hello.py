from flask import Flask, render_template, send_from_directory, make_response

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

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/docs/resume')
def get_pdf(id=None):
    if id is not None:
        binary_pdf = get_binary_pdf_data_from_database(id=id)
        response = make_response(binary_pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = \
            'inline; filename=%s.pdf' % 'Resume'
        return response

@app.route('/resume')
def show_pdf(id=None):
    if id is not None:
        return render_template('doc.html', doc_id=id)

if __name__ == '__main__':
    app.run(debug=True)