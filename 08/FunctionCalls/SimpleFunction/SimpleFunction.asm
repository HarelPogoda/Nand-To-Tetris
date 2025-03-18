//boot
@256
D=A
@SP
M=D

@0
D=A
@1
M=D
@2
M=D
@3
M=D
@4
M=D

//*****call Sys.init *****
//pushing the return address
//push constant
@Sys.init.1
D=A
@SP
A=M
M=D
@SP
M=M+1

//push segment pointer
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

//push segment pointer
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

//push segment pointer
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

//push segment pointer
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

//ARG = SP-5-n_args - repositions ARG
@5
D=A
@SP
D=M-D
@ARG
M=D

//LCL = SP - repositions LCL
@SP
D=M
@LCL
M=D
// goto Sys.init
@Sys.init
0;JMP
(Sys.init.1)
//******function SimpleFunction.test 2******
(SimpleFunction.test)
//lets make way for variables
//push constant
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

//******push local 0******
//write_push_pop
//write_push
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

//******push local 1******
//write_push_pop
//write_push
@1
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

//******add******
//add
@SP
A=M-1
D=M
A=A-1
D=D+M
M=D
@SP
M=M-1

//******not******
//not
@SP
A=M-1
M=!M

//******push argument 0******
//write_push_pop
//write_push
@0
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

//******add******
//add
@SP
A=M-1
D=M
A=A-1
D=D+M
M=D
@SP
M=M-1

//******push argument 1******
//write_push_pop
//write_push
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

//******sub******
//sub
@SP
A=M-1
D=M
A=A-1
D=M-D
M=D
@SP
M=M-1

//******return******
//frame = LCL; PUSHING LCL to RAM[13]
@LCL
D=M
@13
M=D


//return_address = *(frame-5); puts the return address in RAM[14]
@LCL
D=M
@5
A=D-A
D=M
@14
M=D
@SP

//*ARG = pop(); repositions the return value for the caller
//segment the top value of the stack.
@SP
A=M-1
D=M
@ARG
A=M
M=D
@SP
M=M-1

//SP = ARG + 1; repositions SP for the caller
//- moves it passed the return value we just pushed.
@ARG
D=M
@SP
M=D+1

//lets reset all the segments now
//THAT = *(frame-1); restores THAT for the caller
@13
A=M-1
D=M
@THAT
M=D

//THIS = *(frame-2); restores THIS for the caller
@13
D=M
@2
A=D-A
D=M
@THIS
M=D

//ARG = *(frame-3); restores ARG for the caller
@13
D=M
@3
A=D-A
D=M
@ARG
M=D

//LCL = *(frame-4); restores LCL for the caller
@13
D=M
@4
A=D-A
D=M
@LCL
M=D

//goto return_address
@14
A=M
0;JMP

