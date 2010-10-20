#!/usr/bin/env python

# TODO: sort usage table alphabetically - can't sort a dict?
#       make search find after first instance
#       take args for -a, -d and -s on command line instead of with raw_input
#       do the check if ~/.nag exists bit properly
#            look for XDG_CONFIG_HOME and put nag dir in there, otherwise default to ~/.nag?

import sys, os, fileinput, getopt

home = os.getenv("HOME")
filename = home + "/.nag"
test = open(filename, "a")
test.close()
size = os.path.getsize(filename)
number_of_lines = len(open(filename).readlines())

def usage():
    print "usage: nag [-acdls] "
    table = {"-a": "add an item to your list", "-c": "clear your list", "-d [n]": "remove item [n] from your list", "-l": "show the contents of your list", "-s": "search your list"}
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

def main(argv):
    if len(sys.argv) == 1:
        first_line()
    else:
        try:
            opts, args = getopt.getopt(sys.argv[1:], "acd:hls", ["add", "clear", "delete=", "list", "search"])
        except getopt.GetoptError, err:
            print str(err) 
            usage()
            sys.exit(2)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()    
            elif opt in ("-l", "--list"):
                list()
            elif opt in ("-a", "--add"):
                add()
            elif opt in ("-c", "--clear"):
                clear()
            elif opt in ("-s", "--search"):
                searcher()
            elif opt in ("-d", "--delete"):
                delete()
            else:
                usage()

if __name__ == "__main__":
    main(sys.argv[1:])
