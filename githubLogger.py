import sys, os, subprocess, datetime

print('LOGGER')

tracker_File_Path = "./tracker.txt"
contribution_date = str(datetime.datetime.today()).split()[0]

with open(tracker_File_Path, 'a') as the_tracker_file:
    the_tracker_file.write(contribution_date)
    the_tracker_file.write('Created a private contribution on a bitbucket repository.')
    the_tracker_file.write("\n")
    the_tracker_file.write("\n")

subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Test commit made with python and hook"])
subprocess.call(["git", "push", "origin", "master"])