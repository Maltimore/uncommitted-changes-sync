# uncommitted-changes-sync

## Use case
You are working on a git code repository that you want to run on a server. However, you would like to work on the files locally. Reasons for this could be that
- you don't have root access on the server and therefore can't install the helper tools that you need
- a mounted remote filesystem can be too slow

So you have the repository locally and remotely and need a way to quickly sync the two. Of course you could work locally, then commit, push and then pull on the server, but it is inconvenient. In particular, you don't want to create a commit yet, because you're still debugging. That's where `uncommitted-changes-sync` comes in! It gives you a way to sync your uncommited changes directly to a remote filesystem.

## CAUTION
This will **DELETE** all untracked files and folders in your remote repository every time it syncs (unless they are in your .gitignore).

## Installation
This only works on Linux.
You need the program ```inotifywait``` installed locally. On debian/ubuntu, it can be found in the package ```inotify-tools```:
```
sudo apt install inotify-tools
```
Then download this repository to your local computer.

## How it works
The main functionality can be found in `git_upd`.
Every time a local change to a file in one of the tracked repositories is detected, the following happens:
- Locally, create a git diff between the current state of the repository and the branch to compare with (typically origin/master)
- Send the diff via `ssh` to the server
- On the server, perform a `git reset --hard` to the comparison branch
- On the server, apply the diff

## Usage
Create a config file and place it somewhere on your computer (on unix, the recommended path would be something like `~/.config/uncommitted_changes_sync`, but anywhere is fine). It should have one line per repository that you want to sync. In each line, you put first the path to the local repository, then the comparison branch, then the ssh-name of the remote host, and then the remote path to the repository, all separated by spaces. Example:

```
/home/local_username/myrepo origin/main mycluster /home/remote_username/myrepo
```

Lines starting with "#" or empty lines are ignored.

If you haven't done so already, you should add your ssh-key to the ssh-daemon with

```ssh-add```

Then, run the sync command (adjust the paths):

```~/repos/uncommitted_changes_sync/sync ~/.config/uncommitted_changes_sync```

## Gotchas
- You cannot use $HOME in your remote path
- Assuming your comparison branch is `origin/master`, then you need to make sure that `origin/master` points to the same commit locally and remotely. Note that you can make commits locally, even to `master`, as long as you don't push the commits to `origin/master` without pulling on the remote
- Changes in git submodules are not synced. However, you can sync each submodule individually by including them as extra repos in the ```config``` file
- If your diff is empty, the output from the server will be `unrecognized input`. Nothing bad happens, but it can be confusing.

## Run in the background with systemd
To run this in the background with `systemd` as a `user` unit (i.e. not requiring root permissions):
- Place the provided file `systemd_unit.service` into `~/.config/systemd/user/` and give it a more reasonable name like `uncommitted-changes-sync.service`. In the file, adapt the path as required.
- Run `systemctl --user restart uncommitted-changes-sync.service`

If you did not run `ssh-add` since booting, you have to run it first before then (re-)starting the `systemd` unit.
