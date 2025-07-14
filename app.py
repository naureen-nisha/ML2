from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    hours = int(request.form['hours'])
    difficulty = int(request.form['difficulty'])

    # Simple dummy logic for now
    if hours >= 5 and difficulty <= 5:
        plan = "🧠 Focus on completing 2 major topics today."
    elif hours < 3:
        plan = "⏳ Try to review summary notes or watch quick videos."
    else:
        plan = "📈 Mix one hard and two easy topics to stay consistent."

    return render_template("result.html", plan=plan, study_hours=hours)  # ✅ Fixed this line

if __name__ == '__main__':
    app.run(debug=True)
