from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role,Comment,Pitch,Upvote,Downvote
from flask_migrate import Migrate,MigrateCommand

app = create_app('development')

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)
manager.add_command('run',Server(use_debugger=True))

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role, Comment = Comment, Pitch = Pitch, Upvote = Upvote, Downvote = Downvote)


if __name__ == '__main__':
    manager.run()