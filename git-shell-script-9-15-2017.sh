# Test merge fuctionalility of git

cd /Users/wxs/Dropbox/Git-test
mkdir Test-merge
cd Test-merge


cd /Users/wxs/Dropbox/Git-test/Test-merge
# Start with clean slate
rm -rf .git
rm *.txt
ls -a

git init

# Make root file
echo $'1\n2\n3\n4\n5\n6\n7\n8\n9' > root.txt
cat root.txt

git add root.txt
git commit -m "Commit root file"

# Try pushing to Github
# First create repository "Test-merge" on Github using Web interface
# The git remote add command takes two arguments:
#   A remote name, for example, origin
#   A remote URL, for example, https://github.com/user/repo.git

git remote rm origin  # in case "origin" had been defined already
git remote add origin https://github.com/wstuetzle/Test-merge.git
git push -u origin master


# Make a modified version of root.txt
echo $'4\n5\n6\n7\n8\n9\n10\n11\n12' > root.txt
git add root.txt
git commit -m "Commit mod 1 of root file"

# Checkout the original version of root.txt
git log --oneline
# produces hash tag for each commit
git checkout 7873acb  # Will produce detached head
cat root.txt
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
#
# Make a new branch starting at the original version of root.txt
# and check it out
git checkout -b alternative

# Make an alternative modification of root.txt
echo $'0\n1\n2\n3\n4\n5\n6' > root.txt
cat root.txt
# 0
# 1
# 2
# 3
# 4
# 5
# 6

git add root.txt
git commit -m "Commit mod 2 of root file"

git branch

git checkout master
cat root.txt
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12

git checkout alternative
cat root.txt
# 0
# 1
# 2
# 3
# 4
# 5
# 6

# Now try a merge
git checkout master
git merge alternative --no-edit  # Can't do it
cat root.txt

# "Fix" the problem
echo $'0\n4\n5\n6\n' > root.txt
git add root.txt
git commit -m "Fixed conflict"

git checkout master
cat root.txt
# 0
# 4
# 5
# 6

git checkout alternative
cat root.txt
# 0
# 1
# 2
# 3
# 4
# 5
# 6
