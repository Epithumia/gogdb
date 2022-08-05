import os


def configure_app(app):
    app.config["JINJA_LSTRIP_BLOCKS"] = False
    app.config["JINJA_TRIM_BLOCKS"] = False

    app.config.from_envvar("GOGDB_CONFIG")

    app.jinja_env.lstrip_blocks = app.config["JINJA_LSTRIP_BLOCKS"]
    app.jinja_env.trim_blocks = app.config["JINJA_TRIM_BLOCKS"]
