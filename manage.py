from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role,Comment



@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role, Comment = Comment)


if __name__ == '__main__':
    manager.run()