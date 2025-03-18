//push constant
@10
D=A
@SP
A=M
M=D
@SP
M=M+1

//write_pop
@0
D=A
@LCL
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
@21
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@22
D=A
@SP
A=M
M=D
@SP
M=M+1

//write_pop
@2
D=A
@ARG
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
@ARG
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
@36
D=A
@SP
A=M
M=D
@SP
M=M+1

//write_pop
@6
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
@42
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@45
D=A
@SP
A=M
M=D
@SP
M=M+1

//write_pop
@5
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

//write_pop
@2
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

//push constant
@510
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop temp
@6
D=A
@5
D=A+D
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
@0
D=A
@LCL

D=M+D
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

//push
@5
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

//push
@1
D=A
@ARG

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
@THIS

D=M+D
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

//push
@6
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

//add
@SP
A=M-1
D=M
A=A-1
D=D+M
M=D
@SP
M=M-1

//sub
@SP
A=M-1
D=M
A=A-1
D=M-D
M=D
@SP
M=M-1

//push temp
@6
D=A
@5
A=A+D
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

