---
layout: page
---

# Setting up Using GitHub Classroom

> This explanation assumes you haven't downloaded the exercises yet and simply want to start fresh.
> If, however, you have cloned the exercises in the past and solved some exercises, you might want to follow [these instructions](github-classroom.md) instead.

On Toledo, under "First Steps", you'll find a link to the GitHub Classroom Assignment.
Click on it.
You will be led to a page inviting you to "Accept this assignment".
Press the button to accept it.

You are then shown a page informing you that your repository is being prepared.
Refresh the page every few seconds until a new page appears telling you you're ready to go.
A URL should be shown: it should look something like https://github.com/UCLL-P2-2223/p2-exercises-youraccountname.
You will need this URL, so don't lose it.

> If you happen to lose the URL, simply visit the GitHub Classroom link on Toledo again.
> You'll be brought straight to the page showing the URL.

On your machine, create a directory where you would like to store the exercises.

> Do _not_ place this directory under OneDrive/DropBox/Google Drive/...
> We will be working with GitHub, which is a better alternative for storing code in the cloud.
> Storing a Git repository on OneDrive/... could corrupt it.

Open a terminal in this directory and enter the following command:

```bash
# Replace URL by the URL you were given earlier
$ git clone URL exercises
```

This should create a directory named `exercises` and download the course material into that directory.
Next, enter the following commands:

```bash
$ cd exercises
$ git remote add upstream https://github.com/UCLL-PR2/exercises.git
$ git pull upstream main
```

Let's check if everything worked:

```bash
$ git remote -v
origin    https://github.com/UCLL-P2-2223/p2-exercises-youraccountname (fetch)
origin    https://github.com/UCLL-P2-2223/p2-exercises-youraccountname (push)
upstream  https://github.com/UCLL-PR2/exercises.git (fetch)
upstream  https://github.com/UCLL-PR2/exercises.git (push)
```

Here, `origin` refers to your very own repository, which you have write access to.
`upstream` refers to our repository, for which you only have readonly access.

Visit your remote repository's webpage.
You can do this by using a browser and going to your repository URL.
GitHub should claim it's empty.
Let's fill it up by sending your locally stored data to GitHub:

```bash
$ git push -u origin master
```

After the push is finished, refresh your repository's webpage in the browser.
It should now contain all the exercises.

From now on, you should make sure to always push your solutions to GitHub.
Instructions for how to do this can be found [here](../workflow.md).
