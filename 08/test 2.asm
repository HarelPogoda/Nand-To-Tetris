//lets reset all the segments now
//THAT = *(frame-1); restores THAT for the caller
@6
A=M-1
D=M
@THAT
M=D

//THIS = *(frame-2); restores THIS for the caller
@6
D=M
@2
A=D-A
D=M
@THIS
M=D

//ARG = *(frame-3); restores ARG for the caller
@6
D=M
@3
A=D-A
D=M
@ARG
M=D

//LCL = *(frame-4); restores LCL for the caller
@6
D=M
@4
A=D-A
D=M
@LCL
M=D