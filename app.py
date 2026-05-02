from flask import Flask, render_template, request, redirect, url_for
from forms import TestForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.secret_key = 'your-very-secret-key'
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def form_view():
    form = TestForm()
    
    if form.validate_on_submit():
        file_data = form.file.data
        filename = secure_filename(file_data.filename)
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file_data.save(file_path)
        
        submitted_info = {
            "Name": form.name.data,
            "Email": form.email.data,
            "Age": form.age.data,
            "Gender": dict(form.gender.choices).get(form.gender.data),
            "Mode of Travel": dict(form.modeTravel.choices).get(form.modeTravel.data),
            "Date of Birth": form.date.data.strftime('%Y-%m-%d'),
            "File Saved As": filename
        }
        
        return render_template('success.html', data=submitted_info)
    
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)