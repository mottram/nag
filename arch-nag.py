#!/usr/bin/env python2

import sys, os, fileinput

home = os.getenv("HOME")
filename = home + "/.nag"
test = open(filename, "a")
test.close()
size = os.path.getsize(filename)
number_of_lines = len(open(filename).readlines())

def helper():
    table = {"a": "Add an item to your list", "c": "Clear your list", "d [n]": "Remove item [n] from your list", "ls": "Show the contents of your list", "s": "Search your list"}
    for command, explanation in table.items():
        print "{0:10}  {1:10}".format(command, explanation)

def error():
    print "There's nothing to do!\nUse 'nag a' to add a new item to your list."

def add():
    new_item = raw_input("> ")
    with open(filename, "a") as f:
        f.write(new_item + "\n")

def list():
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

def searcher():
    search_term = raw_input("> ")
    line_num = 0
    f = open(filename)
    for line in f.readlines():
        line_num += 1
        if search_term in line:
            print line_num, line,
            f.close()
            break
    else:
        print search_term, "not found.",

try:
    if sys.argv[1] == "ls":
        list()
    elif sys.argv[1] == "help":
        helper()
    elif sys.argv[1] == "c":
        clear()
    elif sys.argv[1] == "a":
        add()
    elif sys.argv[1] == "d":
        delete()
    elif sys.argv[1] == "s":
        searcher()
    else:
        print "Oops! It looks like you mistyped a command:"
        helper()
except IndexError:
    first_line()
