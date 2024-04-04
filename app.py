
from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Настройка подключения к базе данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Определение модели данных
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)

# Создание таблицы в базе данных (если ещё не создана)
@app.before_first_request
def create_tables():
    db.create_all()

# Обработчик для формы обратной связи
@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    if name and email and phone and message:  # Проверка, что все поля заполнены
        feedback = Feedback(name=name, email=email, phone=phone, message=message)
        db.session.add(feedback)
        db.session.commit()
        return redirect('/index.html')  # Перенаправление на index.html после успешного добавления
    else:
        return "Ошибка при отправке заявки. Попробуйте еще раз."

if __name__ == '__main__':
    app.run(debug=True)
