# Project-Cloner
A small Python script that helps developers at Kippa create new versions of any codebase automatically

## Usage

- To use the script to clone a project folder simply provide it with the (relative) path of the folder you want
  cloned and the name you wish the destination folder to have. Here's an example:
```
py cloner.py ../<project-folder-name> <new-project-folder-name>
```

- If you do not provide the script with a second argument naming the destination folder, it will use 
  "v2" as the default folder name. Here's an example
 ```
 py cloner.py ../<project-folder-name>
 ```
 
 - As seen above, it's easier to parse the relative path of the project you wish to clone rather that 
  the absolute path
  
 - The script will throw an error and stop running if you pass a folder name that already exists with the working
   directory as a second argument. It will create the folder and fill it up automatically
 
