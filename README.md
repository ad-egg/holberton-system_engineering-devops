# holberton-system_engineering-devops
## 0x00-shell_basics
### 0-current_working_directory 
This is a script that prints the path name of the current working directory. 
### 1-listit
This script displays the contents of your current working directory. 
### 2-bring_me_home
This script changes the working directory to the user's home directory. 
### 3-listfiles
This script displays the current directory contents in long format. 
### 4-listmorefiles
This script displays in long format the contents of the current working directory, including hidden files. 
### 5-listfilesdigitonly
This script displays in long format the contents of the current working directory, including hidden files, with the user and group IDs displayed numerically. 
### 6-firstdirectory
This script creates a directory named `holberton` in the `/tmp/` directory. 
### 7-movethatfile
This script moves the file `betty` from `/tmp/` to `/tmp/holberton`. 
### 8-firstdelete
This script deletes the file `betty` that is in `/tmp/holberton`. 
### 9-firstdirdeletion
This script deletes the `holberton` directory that is located in the `/tmp` directory. 
### 10-back
This script changes the current working directory to the previous working directory. 
### 11-lists
This script lists all (including hidden) files in the current directory, the parent of the working directory, and the `/boot` directory in long format. 
### 12-file_type
This script prints the file type of `iamafile`. 
### 13-symbolic_link
This script creates a symbolic link `__ls__` that links to `/bin/ls`. 
### 14-copy_html
This script copies all the HTML files from the current working directory to the parent of the working directory but excludes files that already exist in the parent directory. 
### 15-lets_move
This script moves all files that begin with an uppercase letter to the directory `/tmp/u`. 
### 16-clean_emacs
This script deletes all the files in the current working directory that end with `~`. 
### 17-tree
This script, within the current working directory, creates the directory `welcome` which contains the directory `to` which contains the directory `holberton`. 
### 18-commas
This script lists all (including hidden) of the files and directories of the current directory, with each entry separated by a comma (`,`) and ends directory names with a slash (`/`). 
## 0x01-shell_permissions
### 0-iam_betty
This script changes your userID to `betty`.
### 1-who_am_i
This script prints your effective userid. 
### 2-groups
This script prints all the groups that the curent user is in.
### 3-new_owner
This script changes the file owner of `hello` to `betty`. 
### 4-empty
This script creates an empty file called `hello`.
### 5-execute
This script adds execute permission for the owner of the file named `hello`.
### 6-multiple_permissions
This script adds execute permission for the owner and group and read permission to other users to the file `hello`. 
### 7-everybody
This script adds execute permission to everyone for the file `hello`. 
### 8-James_Bond
This script sets the permissions of the file `hello` so that owner and group have no permission but other users have all the permissions. 
### 9-John_Doe
This script sets the permissions of the file `hello` to `-rwxr-x-wx`. 
### 10-mirror_permissions
This script sets the permissions of the file `hello` to those of the file `olleh`. 
### 11-directories_permissions
This script adds execute permission to all subdirectories of the current working directory for the owner, group, and other users. 
### 12-directory_permissions
This script creates a directory named `dir_holberton` with permissions 751. 
### 13-change_group
This script changes the group owner of file `hello` to `holberton`. 
### 14-change_owner_and_group
This script changes, in the current working directory, the owner to `betty` and the group to `holberton` for all of the files and directories. 
### 15-symbolic_link_permissions
This script changes the owner of the file `_hello` to `betty` and the group to `holberton`.
### 16-if_only
This script changes the owner of the file `hello` to `betty` if it is owned by user `guillaume`. 
