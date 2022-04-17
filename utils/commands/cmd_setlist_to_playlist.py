from utils.cli import pass_environment

import click

@click.command("setlist_to_playlist", short_help="Turns a setlist.fm setlist into a Spotify playlist.")
@click.option("--setlist", type=str, help="URL of the setlist to turn into a playlist")
@pass_environment
def cli(ctx, setlist):
    """" Turns a setlist.fm setlist into a Spotify playlist. """
    ctx.setlist_to_playlist(setlist)
