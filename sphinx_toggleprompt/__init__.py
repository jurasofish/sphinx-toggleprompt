from sphinx.util import logging
from pathlib import Path


__version__ = "0.0.5"
logger = logging.getLogger(__name__)


def scb_static_path(app):
    static_path = str((Path(__file__).parent / '_static').absolute())
    app.config.html_static_path.append(static_path)


def add_to_context(app, config):
    # Update the global context
    config.html_context.update({'toggleprompt_offset_right': config.toggleprompt_offset_right})


def setup(app):
    logger.verbose('Adding toggle buttons to code blocks...')
    # Add our static path
    app.connect('builder-inited', scb_static_path)

    # configuration for this tool
    app.add_config_value("toggleprompt_offset_right", 0, "html")

    # Add configuration value to the template
    app.connect("config-inited", add_to_context)

    # Add relevant code to headers
    app.add_js_file("toggleprompt.js")
    return {"version": __version__,
            "parallel_read_safe": True,
            "parallel_write_safe": True}
