import os
import click

from src.internal.spotipy_utils import Spotify


CONTEXT_SETTINGS = dict(auto_envvar_prefix="SPOTIFY")


# Creates a Spotify class, that is passed around anything with @pass_environment
# ensure=True ensures this class is created
pass_environment = click.make_pass_decorator(Spotify, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))


class SpotifyCLI(click.MultiCommand):
    def list_commands(self, ctx):
        """ List commands in the CLI. """
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename in os.listdir(cmd_folder):
                if filename.endswith(".py") and filename.startswith("cmd_"):
                    rv.append(filename[4:-3])
        rv.sort()
        return rv


    def get_command(self, ctx, name):
        """ Add sub-commands to CLI. """
        try:
            mod = __import__(f"src.commands.cmd_{name}", None, None, ["cmd"])
        except ImportError:
            return
        return mod.cmd


@click.command(cls=SpotifyCLI, context_settings=CONTEXT_SETTINGS)
@pass_environment
def root_cli(ctx):
    pass
