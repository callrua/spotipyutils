from src.cli import pass_environment

import click


@click.command("setlist_to_playlist", short_help="Turns a setlist.fm setlist into a Spotify playlist.")
@click.option("--setlist", type=str, help="URL of the setlist to turn into a playlist")
@click.option("--id", type=str, help="ID of User who will own the playlist")
@pass_environment
def cmd(ctx, setlist, id):
    """" Turns a setlist.fm setlist into a Spotify playlist. """
    ctx.id = id
    ctx.setlist_to_playlist(setlist)
