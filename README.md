# Demo exercise


## Steps to do in Vcode
1. Clone to your computer (vcode remember)
1. from vcode => Make a branch - call it -  branch-no-conflict
1. Make a small change by putting your name at the top of the python file and commenting it out.
1. commit the change
1. publish this branch

## Steps to do in Github
1. Go to github check that you see your branch and your last commit

How to ‘merge’ this branch into your main branch? **Do not do it yet.**


## Steps to create a conflict

Simulate two users working on the same repository in different branches but changing the same file

1. Create another branch, call it branch-with-conflict
1. Comment out the the function that calculates the length and comment out the final print statement to displays the length 
1. Commit it , **but  do not push** 
1. Switch to the **branch-no-conflict** and uncomment the function that  but calculate the count of features differently (e.g use for loop with a counter)
1. Commit and push the changes to github
1. “merge “ it with main (it is called a pull request) 
1. Switch back to branch-with-conflict and publish it
1. Try to “Merge” this branch as well. What happens

Why did this conflict happened? 

## Steps to solve the conlict
1. notice that in both branches something similar has been attempted, you could just ignore one branch.
1. Resolve in vcode the conflicht by merging the changes of both branches

## How to prevent conflicts
1. Ideally do not work on the same files in two different branches 


