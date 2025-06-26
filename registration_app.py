from flask import Flask, render_template_string, request

app = Flask(__name__)

form_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Short Term Training Program Registration</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; }
        .container { background: #fff; padding: 30px; margin: 50px auto; width: 400px; border-radius: 8px; box-shadow: 0 2px 8px #ccc; }
        label { display: block; margin-top: 15px; }
        input[type=text], input[type=number] { width: 100%; padding: 8px; margin-top: 5px; border-radius: 4px; border: 1px solid #ccc; }
        .btn { margin-top: 20px; width: 100%; padding: 10px; background: #007bff; color: #fff; border: none; border-radius: 4px; cursor: pointer; }
        .info { background: #e7f3fe; padding: 15px; border-radius: 4px; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Attendee Registration</h2>
        <form method="post">
            <label>Name:</label>
            <input type="text" name="name" required>
            <label>Age:</label>
            <input type="number" name="age" min="1" max="120" required>
            <label>Organization:</label>
            <input type="text" name="organization" required>
            <label>Expertise:</label>
            <input type="text" name="expertise" required>
            <hr style="margin: 25px 0;">
            <h3>Speaker Session Details</h3>
            <label>Name of Speaker:</label>
            <input type="text" name="speaker_name" required>
            <label>Title of the Session:</label>
            <input type="text" name="session_title" required>
            <button class="btn" type="submit">Submit</button>
        </form>
        {% if info %}
        <div class="info">
            <strong>Attendee Information:</strong><br>
            Name: {{ info.name }}<br>
            Age: {{ info.age }}<br>
            Organization: {{ info.organization }}<br>
            Expertise: {{ info.expertise }}<br><br>
            <strong>Speaker Session Details:</strong><br>
            Name of Speaker: {{ info.speaker_name }}<br>
            Title of the Session: {{ info.session_title }}
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def register():
    info = None
    if request.method == 'POST':
        info = {
            'name': request.form['name'],
            'age': request.form['age'],
            'organization': request.form['organization'],
            'expertise': request.form['expertise'],
            'speaker_name': request.form['speaker_name'],
            'session_title': request.form['session_title']
        }
    return render_template_string(form_html, info=info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
