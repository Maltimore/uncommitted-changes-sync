# uncommitted-changes-sync

## Use case
You are working on a git code repository that you want to run/debug on a server/cluster. You would however like to work locally (for instance because you don't have root access on the server and therefore can't install all the cool helper tools that you **need**), and not on a mounted filesystem either (because it's too slow). So you have the repository locally and remotely and need a way to quickly sync the two. Of course you could work locally, then commit, push and then pull on the server. The problem with that is that you need to commit things that you're just testing out, so it would mess up your commit history. That's where uncommitted-changes-sync comes in! It gives you a way to sync your uncommited changes with a remote filesystem.

## CAUTION
This will **DELETE** all untracked files and folders in your remote repository every time it syncs (unless they are in your .gitignore).

## Usage
This **only works on Linux**.
Clone this repository and enter it. You have to make the three files ```sync```, ```git_upd``` and ```inotdo``` executable. You can do this using

```
chmod u+x sync
chmod u+x git_upd
chmod u+x inotdo
```

Create a file ```config``` within this folder. It should have one line per repository that you want to sync (syncing one local repository with multiple remots is also possible). In each line, you should have first the path to the local repository, then the ssh-name of the remote host, and then the remote path to the repository. Like so:

```
/home/maltimore/myrepo mycluster /home/remote_user/myrepo
```

Then within this repository, run 

```./sync```.

You can stop all syncers by hitting Ctrl-c.

## Gotchas
- You cannot use $HOME in your remote path
- Changes in git submodules are not synced (yet. Working on it!)

