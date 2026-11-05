File handling in python 

File handling 
creating, opening, reading, writing and closing


- Store data can be also in files 
- Access external files like .txt, .csv, .json etc. 
- Process larges files 
- Automate tasks like reading configs or reports 


x = 42 -> RAM (Random access memory) 

1. File paths: Absolute vs Relative 
a Path is the address string specifying the location of file or folder in the operation 


open(filename, mode)

`r` -> Read 
`w` -> write (Start 0 byte)
`a` -> append 
`x` -> Exclusive create (if file exits it throw error)
`r+` -> read + write ()

Text Mode vs binary mode (Image, pdfs, audio and compiled bytecode):
r -> rb 
w -> wb
