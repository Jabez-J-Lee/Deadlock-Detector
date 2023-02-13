# Introduction
- Lab from the Operating Systems course demonstrating understanding of deadlocks and how to detect them.

## Index

- [About](#about)
- [Usage](#usage)
  - [Installation](#installation)
  - [Pre-Requisites](#pre-requisites)
  - [Build and Run](#Build-and-Run)

## About
Apply Banker's Algorithm to Deadlock Detection via input file, which is specified by the user on program start. 
The program will then run the algorithm and display a message stating either that there is a deadlock or that there is not. 
If there is a deadlock, the processes that are involved in the deadlock will be listed. 
The user will then be given a chance to run another set of data

## Usage
Create a data set that follows the following sample data:
```
5         (Number of Processes)
3         (Number of Resource Types)
0 0 0     (Available unallocaated instance of each resource)
0 1 0     (Allocation Matrix) - N lines of M numbers
2 0 0     
3 0 3 
2 1 1 
0 0 2 
0 0 0     (Request Matrix) - N lines of M numbers
2 0 2 
0 0 1 
1 0 0 
0 0 2
```

### Installation
All Code developed and tested on Linux using Visual Studio Code (VSCode) in Python

### Pre-Requisites
Using the NumPy library, which must therefore be installed. To install NumPy visit their website [here](https://numpy.org/install)

### Build and Run
- Once installed you can run the program by typing:
```
python main.py
```
- When prompted for a file, enter your custom data set or the given text files (input.txt, input2.txt, or input3.txt):
```
input.txt
```
