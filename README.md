# uncommitted-changes-sync

## Use case
You are working on a git code repository that you want to run/debug on a server/cluster. You would however like to work locally (for instance because you don't have root access on the server and therefore can't install all the cool helper tools that you **need**), and not on a mounted filesystem either (because it's too slow). So you have the repository locally and remotely and need a way to quickly sync the two. Of course you could work locally, then commit, push and then pull on the server. The problem with that is that you need to commit things that you're just testing out, so it would mess up your commit history. That's where uncommitted-changes-sync comes in! It gives you a way to sync your uncommited changes with a remote filesystem.

## CAUTION
This will **DELETE** all untracked files and folders in your remote repository every time it syncs (unless they are in your .gitignore).


## Installation
This **only works on Linux**.
You need the program ```inotifywait``` installed locally. On ubuntu, it can be found in ```inotify-tools```.

```
sudo apt install inotify-tools
```

Then clone this repository somewhere on your local computer. That's it!

## Usage
Create a file ```config``` within this folder. It should have one line per repository that you want to sync (syncing one local repository with multiple remots is also possible). In each line, you should have first the path to the local repository, then the ssh-name of the remote host, and then the remote path to the repository. Like so:

```
/home/maltimore/myrepo mycluster /home/remote_user/myrepo
```

Lines starting with "#" or empty lines are ignored.

If you haven't done so already, you should add your ssh-key to the ssh-daemon with

```ssh-add```

Then within this repository, run 

```./sync config```

The first argument "config" just tells sync where to find the config, so if the config is in a different folder:

```./sync /path/to/config```

## Gotchas
- You cannot use $HOME in your remote path
- Changes in git submodules are not synced. However, you can sync each submodule individually by including them as extra repos in the ```config``` file
- Your local and remote repository should be on the same branch, and origin/head must point to the same commit. You can however make commits locally, as long as you don't push them. Once you push, you need to pull on the remote.
- If your diff is empty, the output from the server will be 'unrecognized input'. Nothing bad happens, but it can be confusing.
