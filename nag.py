#!/usr/bin/env python2

import sys, os, fileinput
config = os.getenv("XDG_CONFIG_HOME")

if not os.path.exists(config + "/nag"):
    os.makedirs(config + "/nag")
    filename = config + "/nag/list.txt"
else:
    filename = config + "/nag/list.txt"

txt = open(filename, "a")
size = os.path.getsize(filename)
number_of_lines = len(open(filename).readlines())

def helper():
    print """
 ls   \tshow the contents of your list
 a    \tadd an item to your list
 n    \tshow the next item on your list
 c    \tclear your list
 d [n]\tremove item [n] from your list
    """
    return("")

def error():
    print "There's nothing to do!\nUse 'nag a' to add a new item to your list."

def add():
    new_item = raw_input("> ")
    with open(filename, "a") as f:
        f.write(new_item + "\n")

def ls():
    if size == 0:
        error()
    else:
        for line in fileinput.input(filename):
            print fileinput.lineno(), line,
        print "---\nYou have", number_of_lines, "items in", filename

def clear():
    print "Are you sure you want to clear your nag list? (y or n)"
    answer = raw_input("> ")
    if answer == "y":
        with open(filename, "w") as f:
            f.truncate()
            f.close()
            print "List cleared!",
    else:
        exit()

def first_line():
    if size == 0:
        error()
    else:
        with open(filename) as f:
            print "Next item: " + f.readline(),

def delete():
    line_to_delete = int(sys.argv[2])
    if line_to_delete > number_of_lines:
        print "Item", line_to_delete, "doesn't exist!", "You only have ", number_of_lines, "item(s)."
    else:
        lines = file(filename, "r+").readlines()
        del lines[line_to_delete -1]
        open(filename, 'w').writelines(lines)
        print "Item", line_to_delete , "deleted!"

try:
    if sys.argv[1] == "ls":
        ls()
    elif sys.argv[1] == "help":
        helper()
    elif sys.argv[1] == "c":
        clear()
    elif sys.argv[1] == "a":
        add()
    elif sys.argv[1] == "d":
        delete()
    else:
        print "Oops! It looks like you mistyped a command:"
        helper()
except IndexError:
    first_line()
