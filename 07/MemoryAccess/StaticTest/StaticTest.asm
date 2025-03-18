//push constant
@111
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@333
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@888
D=A
@SP
A=M
M=D
@SP
M=M+1

//write_pop
@8
D=A
@STATIC
D=M+D
@SP
A=M
M=D
A=A-1
D=M
A=A+1
A=M
M=D
@SP
M=M-1

//write_pop
@3
D=A
@STATIC
D=M+D
@SP
A=M
M=D
A=A-1
D=M
A=A+1
A=M
M=D
@SP
M=M-1

//write_pop
@1
D=A
@STATIC
D=M+D
@SP
A=M
M=D
A=A-1
D=M
A=A+1
A=M
M=D
@SP
M=M-1

//push
@3
D=A
@STATIC

D=M+D
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

//push
@1
D=A
@STATIC

D=M+D
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

//sub
@SP
A=M-1
D=M
A=A-1
D=M-D
M=D
@SP
M=M-1

//push
@8
D=A
@STATIC

D=M+D
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

//add
@SP
A=M-1
D=M
A=A-1
D=D+M
M=D
@SP
M=M-1

