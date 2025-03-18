//push constant
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1

//write_pop_pointer 0
@SP
A=M-1
D=M
@THIS
M=D
@SP
M=M-1

//push constant
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1

//write_pop_pointer 1
@SP
A=M-1
D=M
@THAT
M=D
@SP
M=M-1

//push constant
@32
D=A
@SP
A=M
M=D
@SP
M=M+1

//write_pop
@2
D=A
@THIS
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

//push constant
@46
D=A
@SP
A=M
M=D
@SP
M=M+1

//write_pop
@6
D=A
@THAT
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

//push pointer0
//push segment pointer
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

//push pointer1
//push segment pointer
@THAT
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

//push
@2
D=A
@THIS

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
@6
D=A
@THAT

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

