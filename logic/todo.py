
from models.todo import Todo

class TodoLogic:

    def __init__(self , db) -> None:
        self.db = db

    def create(self, content):
        new_task =  Todo(content=content)
        try:
            self.db.session.add(new_task)
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise e
    def get_all(self):
        tasks = Todo.query.order_by(Todo.date_created).all()
        return tasks
    def get_one(self,id):
        task = Todo.query.get_or_404(id)
        return task
    def delete(self, id):
        try:
            task_to_delete = Todo.query.get_or_404(id)
            self.db.session.delete(task_to_delete)
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise e
    def update(self, id, content):
        try:
            task_to_update = Todo.query.get_or_404(id)
            task_to_update.content = content
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise e


