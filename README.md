### Installation

1. Save the script as `nag` somewhere in your path (eg `~/bin`)
2. `chmod a+x ~/bin/nag`

Or clone this repo and symlink 'nag.py' to somewhere in your path.

If you're on Arch Linux, use 'arch-nag.py'.

NB: You probably shouldn't use this script: I don't know what I'm doing (see below).

### Usage

Run `nag` on its own to see the oldest item on your todo list. Use nag with these arguments to manage your list:
    
    -a, --add               add an item to your list
    -c, --clear             clear your list
    -d [n], --delete [n]    remove item [n] from your list
    -l, --list              show the contents of your list

### Why?

I know the world doesn't need yet another CLI todo list thingy, but I just finished _[Learning Python the Hard Way](http://learnpythonthehardway.org/index)_ and wanted to try to make something.
