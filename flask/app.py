from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timezone

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    time = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    def formatted_time(self):
        return self.time.strftime('%Y-%m-%d %H:%M:%S')
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
@app.route("/",methods=['GET','POST'])
def HelloWorld():
    if request.method =='POST':
        todo_title=request.form['title']
        todo_desc=request.form['description']
        data=Todo(title=todo_title,description=todo_desc)
        db.session.add(data)
        db.session.commit()
    allTodo=Todo.query.all()
    
    return render_template('index.html',allTodo=allTodo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return redirect("/")
    else:
        return "TO DO not found"

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.description = request.form['description']
        db.session.commit()
        return redirect("/")
    
    return render_template('update.html', todo=todo)


if __name__ == "__main__":
    app.run(debug=True)
