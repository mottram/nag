### Installation
1. Save the script as `nag` somewhere in your path (eg `~/bin`)
2. `chmod a+x ~/bin/nag`

### Usage

Run `nag` on its own to see the oldest item on your todo list. Use nag with these arguments to manage your list:

* a - add an item to your list
* c - clear your list
* d [n] - remove item [n] from your list
* ls - show the contents of your list

### Bugs

Um, it probably only works on an up-to-date installation of Arch Linux with `$XDG_CONFIG_HOME` set to `~/.config` at the moment. I'll fix that shortly!

### Why?

I know the world doesn't need yet another CLI todo list thingy, but I just finished _[Learning Python the Hard Way](http://learnpythonthehardway.org/index)_ and wanted to try to make something.
