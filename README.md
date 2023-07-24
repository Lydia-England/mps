# mps

---

A command-line utility that calculates the "A" matrix and the "E" matrix from a given transition matrix. 

---

## Prerequisites

- Python interpreter
- terminaltables Python package
- mps.py file

---

## Usage

Basic usage:
```bash
python mps.py [options...]
```

---

## Required Options
- `-n N` sets the dimensions of the matrix to NxN where N is some integer. For example, to run the program with an expected T matrix dimension of 2x2, run:
  ```bash
  python mps.py -n 2
  ```

---

## Optional flags
- `-h` or `--help` displays the help menu.
- `-q` or `--quiet` limits unnecesary outputs. *(default off)*
- `--no-sleep` no delay times between commands. Delay times exist as the default for ease of human-readability. *(default off)*
- `--normalize off` do NOT normalize matrix rows and columns such that each of their sums equal 1.
- `--normalize check` check with the user during runtime before normalizing any matrix rows or columns. *(default normalization setting)*
- `--normalize all` automatically normalize matrix rows and columns such that each of their sums equal 1.
- `-d N` or `--decimal_places N` sets the number of decimal places displayed in the output to N places. *(default is 6)* 
- `-o` or `--output` will output a .csv file containing the 'E' matrix. *(default off)*
- `--write_matrix FILENAME` sets the filename to write the matrix to. *(default is E-matrix-YYYY-mm-DD-HH-MM-SS.csv)*

---

## Examples

### Input a 4x4 T matrix; save to default file name.
```bash
python mps.py -n 4 -o
```

### Input a 2x2 T matrix; do NOT normalize; save to file called 'matrixFile.csv'.
```bash
python mps.py -n 2 --normalize off -o --write_matrix matrixFile.csv 
```

### Input a 5x5 T matrix; automatically normalize; output up to 3 decimal places; do not save.
```bash
python mps.py -n 2 --normalize all -d 3 
```

---

## Cheat Sheet for Terminal
- `pwd`: print working directory 
- `cd`: change directory 
- `cd ..`: change directory up one level 
- `ls`: list files in current directory 
- `ls -l`: list files in current directory (long format; more details) 
- `cat [file]`: display contents of [file] on terminal screen 
- `open [file]`: open [file] with default software
- `mkdir [dirname]`: make new directory called [dirname]
- `touch [filename]`: make new file called [filename]
- `rm [filename]`: remove file called [filename]
- `vim [file]`: open [file] in vim editor
- `nano [file]`: open [file] in nano editor
 


