# <div align="center">Refs</div>
A small and simple way to search folders for files using regular expressions.

For more information, click [here](HowTo.md)
## Features
* Recursively scans files inside a folder
* Uses regular expressions to search filenames
* Displays every file while scanning
* Displays all matching files
* Saves scanned file paths to an output file
* Custom output file path
* Custom target folder
* Displays scan time
* Displays the number of matches found
* Handles invalid regular expressions
* Handles keyboard interrupts
* No external Python dependencies
## Usage
Run:
```text
python Refs.py --folder "C:\Users\Desktop\test"
```
Refs will ask for a regular expression:
```text
Enter a valid regular expression pattern:
```
For example:
```text
^.*\.py$
```
Refs will recursively scan the selected folder and display every file it encounters.

Matching files will be displayed as:
```text
Match: C:\Users\Desktop\test\example.py
```
Non-matching files will be displayed as:
```text
Scanning: C:\Users\Desktop\test\example.txt
```
## Arguments
### `--folder`
Specifies the folder to scan.

Example:
```text
python Refs.py --folder "C:\Users\Desktop\test"
```
### `--output`
Specifies the folder where output file containing scanned file paths will be saved.

Example:
```text
python Refs.py --folder "C:\Users\Desktop\test" --output "C:\Users\Desktop\"
```
By default, the output file is:

```text
output.txt
```
in the current working directory.
### `--help`
Displays the Refs help message.
## Examples
Search for Python files:

```text
python Refs.py --folder "C:\" --output "C:\Users\Desktop"
```
Then enter:
```text
^.*\.py$
```
Search for every file:
```text
.*
```
## Requirements
* Python 3.x
* No external Python dependencies
## Downloads
Only the Python script is available.

— All Rights Reserved [Request Timeout](https://github.com/RequestTimeout)

[LICENSE](LICENSE.md)
