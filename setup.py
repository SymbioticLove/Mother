from distutils.core import setup
import py2exe

setup(
    options={'py2exe': {'bundle_files': 1}},
    windows=[{'script': 'mother.py'}],  # Replace 'your_game.py' with your game's main script
    zipfile=None,
    py_modules=['mother'],  # Replace 'your_game' with the name of your game script, excluding the '.py' extension
)