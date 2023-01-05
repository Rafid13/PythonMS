from main import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# migrate = Migrate(app, db)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
# manager.add_command('main-app-db.default.svc.cluster.local/main', MigrateCommand)


if __name__ == '__main__':
    manager.run()