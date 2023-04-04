from flask import Flask, render_template , request, redirect
from models import db

from common import constants 
from logic import TodoLogic

app = Flask(__name__)
#/// is a relative path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.app_context().push()
db.init_app(app)
db.create_all()


@app.route('/',methods=[constants.POST,constants.GET])
def index():
    logic = TodoLogic(db)
    if request.method == constants.POST:
        task_content = request.form['content']
        try:
            logic.create(task_content)
            return redirect('/')
        except:
            return 'There was an issue on creating the element'
    else:
        tasks = logic.get_all()
        return render_template('index.html',tasks=tasks)
    
@app.route('/delete/<int:id>')
def delete_tasks(id):
    logic = TodoLogic(db)
    try:
        logic.delete(id)
        return redirect('/')
    except:
        return 'There was an issue on deleting the element'
    

@app.route('/update/<int:id>',methods=[constants.POST,constants.GET] )
def update(id):
    logic = TodoLogic(db)
    if request.method == constants.POST:
        task_content = request.form['content']
        try:
            logic.update(id,task_content)
            return redirect('/')
        except:
            return 'There was an issue on updating the element'
    else:
        try:
            task = logic.get_one(id)
            return render_template('update.html', task=task)
        except:
            return 'There was an issue on retrieving the element'
       
    

if __name__== '__main__':
    app.run(debug=True)