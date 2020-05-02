from app import create_app,db
from flask_script import Manager, Server
from app.models import User

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(test)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )

if __name__ == '__main__':
    manager.run()