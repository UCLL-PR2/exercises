---
layout: page
---

# Setting up Using GitHub Classroom

> This explanation assumes you have already cloned the exercises and want to keep the solutions you already made.
> If you want to start over fresh, follow the instructions on [this page](github-classroom-fresh.md) instead.

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

As mentioned at the top of this page, we assume that you already have downloaded the exercises on your machine.
Open a terminal (e.g., Git Bash) in the directory where you stored these exercises.
Let's first perform a quick sanity check.

```bash
$ git remote -v
origin  https://github.com/UCLL-PR2/exercises.git (fetch)
origin  https://github.com/UCLL-PR2/exercises.git (push)
```

If you get an error message, you are in the wrong directory.
Maybe ask a lecturer for help.

If `git remote -v` worked and showed you similar output, we can proceed.
Enter the following commands (please simply copy paste them, you don't want to make a mistake here):

```bash
$ git remote add upstream https://github.com/UCLL-PR2/exercises.git

# Replace URL by the URL you were given earlier
$ git remote set-url origin URL
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
$ git push
```

After the push is finished, refresh your repository's webpage in the browser.
It should now contain all the exercises.

From now on, you should make sure to always push your solutions to GitHub.
Instructions for how to do this can be found [here](../workflow.md).
