# <div align="center">Refs</div>
## How to download and use Refs
### Installation (Python 3.X required)
First download `Refs.py` from /RequestTimeout/Refs/src/Refs.py

Then place the Python file somewhere accessible, for example:
```text
C:\Refs\Refs.py
```
Then when you want to bulk search for files, open a terminal and run:
```bash
python "C:\Refs\Refs.py" --folder "C:\Users\Desktop\test"
```
Refs will ask you to enter a regular expression pattern.
### Using Refs
After starting Refs, enter a regular expression when prompted:
```text
Enter a valid regular expression pattern:
```
For example, to find Python files:
```text
^.*\.py$
```
Refs will recursively scan the specified folder.

Every file being scanned will be displayed in the terminal.

When a file matches the regular expression, Refs will display:
```text
Match: C:\path\to\file.py
```
### Output
Refs saves the paths of all scanned files to the output file.

By default, this is:
```text
output.txt
```
In the current working directory.

You can specify a different output folder path using `--output`(`output.txt` will be generated in this folder):
```bash
python Refs.py --folder "C:\Users\Desktop\test" --output "C:\Users\Desktop\"
```
### Showing Matches
After scanning is complete, Refs will display the number of matches found and the amount of time the scan took.

Refs will then ask:
```text
Do you want to print every matches found? [Y/N]
```
Enter `Y` to display every match.

Enter `N` to exit without displaying the matches again.

If `Y` is selected, Refs waits five seconds before displaying the matches for more readability.

This is especially useful when a large number of files were found.
### Examples
Find all `.py` files:
```text
Regex:
^.*\.py$
```
Find all `.txt` files:
```text
Regex:
^.*\.txt$
```
Match every file:
```text
Regex:
.*
```
> **Warning:** Using `.*` on a large folder can produce very large amounts of terminal output and a large output file.
### Requirements
* Python 3.x
* No external Python dependencies
