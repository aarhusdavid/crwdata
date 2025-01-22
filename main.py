import os
from flask_migrate import Migrate
from flask_minify import Minify
from decouple import config
from api_generator.commands import gen_api
from apps import create_app, db

DEBUG = config('DEBUG', default=False, cast=bool)
get_config_mode = 'Debug' if DEBUG else 'Production'
app = create_app(get_config_mode)

Migrate(app, db)

if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)

for command in [gen_api]:
    app.cli.add_command(command)

if __name__ == "__main__":
    app.run()