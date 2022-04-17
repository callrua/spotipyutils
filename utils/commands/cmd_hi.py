from utils.cli import pass_environment

import click

@click.command("greet", short_help="Greet me")
@pass_environment
def cli(ctx):
    """" Simple greet """
    ctx.greet()
