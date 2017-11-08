from git import Repo
import os
import shutil

with open("uncommited-file-sync-config", "r") as f:
    mountdir = f.read()
    mountdir = mountdir[:-1]  # remove the '\n' at the end of this file

repo = Repo(os.getcwd())

for diff in repo.head.commit.diff(None):
    changed_file = diff.a_path
    destination_path = os.path.join(mountdir, diff.a_path)
    print("Copying " + changed_file + " to " + destination_path)
    if not os.path.exists(os.path.dirname(destination_path)):
        os.makedirs(os.path.dirname(destination_path))
    shutil.copyfile(changed_file, destination_path)
