# DHCP Log Checker

### Table of Contents
**[Description](#description)**<br>
**[Requirements](#requirements)**<br>
**[Tested Machine](#tested-on)**<br>
**[Execution Method](#sample-execution)**<br>
**[Scripts Overview](#overview)**<br>
**[Git Branching](#git-branching-strategy)**<br>
**[Bug Fix Request](#bug-fix-request)**<br>
**[Feature Request](#feature-request)**<br>
**[Authors](#authors)**<br>
**[Conclusion](#conclusion)**<br>

## Description
The repository is about the Python programming language. The basic and advanced programming with python has been written and tested successfully. From the basic data types to object oriented programming. All the basics of python have been covered in this repository.

## Requirements
- Operating System :  Windows-10
- Python :   Version 3.9

## Tested On
Windows-11 with Python version 3.9.13

## Sample Execution
Go to the Source/Exercise directory and run below command :

```python
python <Script>.py
```
## Scripts Overview

| Exercises   |      Description     | 
|----------| :---------------|
| Exercises_01 | To Understand assignment, operators, and variables interactions   | 
| Exercises_02 | To practice working on comments and docstrings while writing scripts   | 
| Exercises_03 | To work with Python's data structures |
| Exercises_04 | To begin writing Python codes to real life scenarios | 
| Exercises_05 | To understand use of functions for code reuse | 
| Exercises_06 | Modules, and packages in Python| 
| Exercises_07 | Handle errors in Python |
| Exercises_08 | Scalability and code reuse via Object-Oriented (OO) coding | 
| Exercises_09 | Unit testing using python | 
| Exercises_10 | Python standard libraries structure  |
| Exercises_11 | Managing network utilities using Python  | 
| Exercises_12 | Python project structure  |

## Git Branching

The branching strategy was used in the GitHub platform was to avoid unnecessary issues in the productinon branch. This will provide only stable codes to the production branch. The braches created below are to make the codes stable in the production.

- Main: contains only stable codes for the production.
- Test:  For testing and bugfixes in before pushing to production.
- Feature: Branch is used to add new features to the test and production.
- Bug Fix: Branch is used to fix the bugs in the stable code.

To the main branch the commits are done using pull requests. This will prevent accidental commits to the production stable codes. The pull request is associated with a code reviewer to check the codes and push it to the main branch.

## Bug Fix Request

Reported bugs can be found at [Bug Fix](https://github.com/rijo-robert-atu/Python/blob/989717801b3f12f3fd5def35ea06137751ba30ce/Documentation/Bug-fix.png)  

If developers encounter a bug with one of the Python programs, please follow the below steps:
- A "Bug" issue is created for the identified bug as shown below.

![image](https://github.com/rijo-robert-atu/Python/blob/989717801b3f12f3fd5def35ea06137751ba30ce/Documentation/Bug-fix.png)

- Clone the Python repo to local machine.


```
git clone https://github.com/krishnenduATU/Python.git
``` 

- A new branch is created from the "test" branch, named "bug_fix_#<bug_fix_number>"
  
  ![image](https://user-images.githubusercontent.com/119352610/209512959-1c818968-b75a-4623-8da4-0d8ba7fb0074.png)

- A developer will work on the bug and fix the issue, then commit the changes. Make sure to add the bug fix number to the commit message, for example, "BugFix #4 : Corrected Pie value "
- Now merge the newly created bug fix branch into the "test" branch. Delete the bugfix branch once it has been merged.
- Checkout to "dev" branch and merge the changes made in the "test" branch so that all the branch are in same state..
- Push the changes on local "dev" and "test" branches to remote repo 
- In the end, the changes from "dev" branch is pulled to "main" branch and issue is closed in GitHub.
 
## Feature Request

Feature requests can be found at [Features](https://github.com/rijo-robert-atu/Python/blob/c1458a959f2c2a9eea0ea451f1203dcd97adae21/Documentation/Pull%20request%20for%20feature%20branch.png)

To create a new feature in the Python programs, developer should follow below steps :

- A "Enhancement" issue is created as shown below.

![image](https://github.com/rijo-robert-atu/Python/blob/c1458a959f2c2a9eea0ea451f1203dcd97adae21/Documentation/Pull%20request%20for%20feature%20branch.png)

- Clone the Python repo to the local machine.
```
git clone https://github.com/krishnenduATU/Python.git
``` 

- A new branch is created from "dev" branch, named "Feature_#<issue number>" as shown below.  

  ![image](https://user-images.githubusercontent.com/119352610/209512959-1c818968-b75a-4623-8da4-0d8ba7fb0074.png)
  
- Developer will work on the new feature. Then commits the changes. Make sure to add issue number to the commit message, for example "Feature #8 : Created UDP server and client scripts" to track the changes.
- Now, checkout to "dev" branch and merge the newly created feature branch. Delete the feature branch.
- Checkout to "test" branch and merge the changes made in "dev" branch so that all the branch are in same state.
- Push the changes on local "dev" and "test" branches to remote repo.
- In the end, the changes from "dev" branch is pulled to "main" branch and the feature request is closed in GitHub.

## Authors

This Python repository was developed as a part of Infrastructure as Code module's assignment by Krishnendu VP.  

## Conclusion

This Python repository covered the fundamental concepts of Python and offered a doable strategy for improving programming skills. In accordance with the provided exercises and research on the same, learners should be able to build and organise Python projects for network or server administration, log analysis, and the automation of routine tasks.




## Functionalities
| Script | Description |
| ----------- | ----------- |
| project.bat | Batch file to create project structure |
| main.py | DHCP log checker |
| csv_creator.py | To convert the final list of values to csv file |
| filter.py | Parse the dhcp log file |
| read_log.py | Reading the dhcp log file |
| unique_values.py | To clear out the duplicate values |
| vendor.py | Get the vendor names from mac address |

## Authors
DHCP Log Checker tool was developed as a part of Infrastructure as Code module's assignment by Rijo Robert.