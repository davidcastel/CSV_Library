# CSV_Library
Python library for course project.

## Release Notes :

### Version 0.1 and What to expect?

The CSV library will a program that uses various tools and utilaizes the power of the terminal. The use of the terminal is very important to be able to get the program running. 

The CSV library works by typing on the file in the condition :
``` if __name__ == "__main__" ```
And change the _filename_ (*test.csv*) to the name of the CSV file. At the current moment, the program only accepts files from the current directory. You can then change the second parameter within ```CSVLibrary()``` which is your _seperator_ (*|*) to the correct seperator that coresponds to your data file.

The second command in the condition, the following parameters for this command is as following: *Command*, *X coordinate*, *Y coordinate*, *New Element*, *Row Value*, *Column Value*
and these are the type for each parameter:
- String: *Command*, *New Element*
- Integer: *X Coorindate*, *Y Coordinate*, *Row Value*, *Column Value*

The command must be one of the following:
- create
- edit
- see
  
**create**: Just creates the table according to the data file
**edit**: Displays the table with the new element that the user wants to change. To be able edit, the following parameters needs to be filled in:*X coordinate*, *Y coordinate*, *New Element*
**see**: Displays the table of only row/columns that the user wants to see of. To be able to see, the following parameters needs to be filled in: *Row Value*, *Column Value*

### Instructions
Before starting, make sure that you have the latest version of python and pip.
- Download the source file
- Open the terminal and go the directory where the source file is located at
- Type the following commands to properly use the CSV library
```
pip install plotly
pip install PySimpleGUI
pip install numpy
pip install matplotlib
```
- Once the following programs have been installed, run the following command: ``` python main.py ``` (or python3 main.py, depending on how your machine runs files on the terminal. )

