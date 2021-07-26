# git and github notes


> A local branch is a branch that only you (the local user) can see. It exists only on your local machine
> the remote branch is the code that exist in a web server like github .

~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~

### createing a new repo in github 

* first create a new folder in you device and go into it
```
    mkdir folderName
    cd folderName
```

* run 
```
git init
```

* write your code inside this folder , lets say we created index.html
```
index.html

<div>hello world</div>

```

* upload your changes to local branch
```
git add .
git commit -m "first commit"
```

* to publish your changes into github repo you have to create a repo in github first from +new button

* then run this command in termminal inside your folder
```
git remote add origin https://github.com/omer-os/my-notes.git # this is the repo link
```

* then add your branch as main production branch in github

```
git push -u origin master
```

* run these commands whenever you make change in you code to publish it to github repo
```
git add .
git commit -m "commit massege bla bla bla"
git push
```
~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~

### createing a new branch

* to create a new branch beside your main producion branch run ... 
```
git checkout -b test-branch
```

* to show in which branch you are now
```
git branch
```

* to switch between branches
```
git checkout the-name-of-branch
```

* to merge changes between branches switch to branch were you want to mege changes and run 
```
git merge the-name-of-test-branch-that-you-want-to-get-changes-from
```

### what if your frind made changes into main branch in remote repo in github ?

* you have to get changes from github into your local branch first , how ? just run
```
git pull
```

* then publish your new changes by
```
git add .
git commit -m "last commits"
git push
```


~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~
