from application import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager
app = create_app()

app.app_context().push()

manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    manager.run()


