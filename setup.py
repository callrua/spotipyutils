from setuptools import setup

setup(
    name="spotipy-utils",
    version="1.0",
    packages=["utils", "utils.commands"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        spotipy-utils=utils.cli:cli
    """
)
