# HW0 - Pt.2 Report
### Hope Zobinou
### DATA 440, Fall 2023
### 9/12/2023

# Q1

*Create a directory (name it whatever you wish, e.g., data440. Change the permissions on this directory 
 so that you are the only user who can read, write, or execute (view the contents) the directory (see "Protection and Permission"). 
 Take a screenshot of (or copy/paste) the command and its output into your report.*

## Answer

The example figures below show the directory that can only be accessed by me.

![hw0_q1_p1](https://github.com/HopeZobinou/data440/assets/81893993/9deb84dc-d35a-4926-bd4c-82e77fca460e)

![hw0_q1_p2](https://github.com/HopeZobinou/data440/assets/81893993/a38a0365-f1fe-4a64-b605-461a2c218181)

## Discussion

In the first image, I stored the directory path into a variable so it can be easier when I want to assign things.
Next, I used the New-Item and ItemType commands to set the directory variable as a directory type (reference 1).

In the second image, I used Get-Acl and Set-Acl to get the security info of the directory and set the edited info to the 
directory-path variable(reference 2).


# Q2

In the directory that you just created, use a simple text editor (e.g., the nano editor) to create a file named test.txt 
(nano test.txt) with the following contents:

```text
CS 800
CS 432
CS 725
MATH 212
MATH 32
```

For each of the commands below, do the following:

* Execute the command
* Take a screenshot of (or copy/paste) the command and its output into your report
* Write a sentence that describes what the command did

Commands:

1. `wc -l test.txt`
2. `echo "CS 800" >> test.txt; cat test.txt`
3. `grep CS test.txt`
4. `grep -c CS test.txt`
5. `sort test.txt`
6. `sort -k2 test.txt`
7. `sort -k2 -n test.txt`
8. `sort test.txt | uniq -c`

## Answer (command 1)
input:
```text
hopez@LAPTOP-VD25VJKM MINGW64 ~/documents/cookie
$ wc -l test.txt
```
output:
```text
5 test.txt
```

## Discussion
The above command counts the number of lines used in the text file.

## Answer (command 2)
input:
```text
hopez@LAPTOP-VD25VJKM MINGW64 ~/documents/cookie
$ echo "CS 800" >> test.txt; cat test.txt
```

output:
```text
CS 800
CS 432
CS 725
MATH 212
MATH 32
CS 800
```

## Discussion

The command added CS 800 to the bottom of the text.

## Answer (command 3)

input:
```text
hopez@LAPTOP-VD25VJKM MINGW64 ~/documents/cookie
$ grep CS test.txt
```
output:
```text
CS 800
CS 432
CS 725
CS 800
```

## Discussion
The grep command removed the lines that didn't contain their parameter (CS).

## Answer (command 4)
input:
```text
hopez@LAPTOP-VD25VJKM MINGW64 ~/documents/cookie
$ grep -c CS test.txt
```
output:
```text
4
```
## Discussion
The above command counts the number of lines that contain CS.

## Answer (command 5)
input:
```text
hopez@LAPTOP-VD25VJKM MINGW64 ~/documents/cookie
$ sort test.txt
```
output:
```text
CS 432
CS 725
CS 800
CS 800
MATH 212
MATH 32
```

## Discussion
The above command sorts the lines in alphabetical order.

## Answer (command 6)
input:
```text
hopez@LAPTOP-VD25VJKM MINGW64 ~/documents/cookie
$ sort -k2 test.txt
```
output:
```text
MATH 212
MATH 32
CS 432
CS 725
CS 800
CS 800
```
## Discussion
This command sorts the lines from Z-A.

## Answer (command 7)
input:
```text
hopez@LAPTOP-VD25VJKM MINGW64 ~/documents/cookie
$ sort -k2 -n test.txt
```
output:
```text
MATH 32
MATH 212
CS 432
CS 725
CS 800
CS 800
```

## Discussion
This command sorts the lines from Z-A and in ascending order with the numbers.

## Answer (command 8)
input:
```text
hopez@LAPTOP-VD25VJKM MINGW64 ~/documents/cookie
$ sort test.txt | uniq -c
```
output:
```text
      1 CS 432
      1 CS 725
      1 CS 800
      1 CS 800
      1 MATH 212
      1 MATH 32
```

## Discussion
The above command sorts the lines and counts the unique lines.


# References

* Reference 1, Powershell Create Directory If Not Exist: A Detailed Guide < https://blog.enterprisedna.co/powershell-create-directory-if-not-exist/#:~:text=1.-,Using%20%2DItemType%20Parameter,%2DItemType%20to%20%E2%80%9CDirectory%E2%80%9D.&text=The%20output%20confirms%20that%20the,in%20the%20specified%20folder%20path.>
* Reference 2, How to Use PowerShell to Manage Folder Permissions <https://petri.com/how-to-use-powershell-to-manage-folder-permissions/>
