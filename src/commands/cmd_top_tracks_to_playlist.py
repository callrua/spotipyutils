from src.cli import pass_environment

import click


@click.command("top_tracks_playlist", short_help="Turns a setlist.fm setlist into a Spotify playlist.")
@click.option("--id", type=str, help="ID of User who will own the playlist")
@pass_environment
def cmd(ctx, id):
    """" Creates 3 time ranged (long, medium, short term) playlists from users top tracks. """
    ctx.id = id
    ctx.top_tracks_to_playlist()
