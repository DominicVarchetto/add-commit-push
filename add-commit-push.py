import os
import sys

print ("Loading...")
numOfArgs = len(sys.argv)
print ("Arguments Passed: ", numOfArgs)





print ("Add Commit Push")
print ("\nGit status")
os.system ("git status")
print ("\ngit add -A")
os.system ("git add -A")
print ('\ngit commit -m "Changed Files"')
os.system ('git commit -m "Changed Files"')
print ("\ngit push")
os.system ("git push")