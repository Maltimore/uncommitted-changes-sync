# uncommitted-changes-sync

## Use case
You are working on a code repository that can only be run, tested, compiled or debugged on a server. You would however like to work locally, and not on a mounted filesystem either, in order to be able to do things like full-text search. So you have the repository locally and remotely and need a way to quickly sync the two. Of course you could work locally, then commit, push and then pull on the server. The problem with that is that you need to commit things that you're just testing out or debugging, so it would mess up your commit history. That's where uncommitted-changes-sync comes in! It gives you a way to sync your uncommited changes with a remote filesystem.

## Usage
In the local repository, place a file called uncommitted-changes-sync-config that contains the local path to the remote repository that is mounted in your filesystem. Then place the file sync.py in that repository, ignore it with .gitigmore and run sync.py in order to sync.
