from flask_script import Manager
from migrate_demo import app
from flask_migrate import Migrate, MigrateCommand
from exts import db
from models import Article
