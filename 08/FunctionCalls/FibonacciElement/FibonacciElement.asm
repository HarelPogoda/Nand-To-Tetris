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
//******function Main.fibonacci 0******
(Main.fibonacci)
//lets make way for variables
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

//******push constant 2******
//write_push_pop
//push constant
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

//******lt                     // checks if n<2******
//eq or lt or gt
@SP
A=M-1
@AISMINUS0
M;JLT
A=A-1
@BISMINUS0
M;JLT
(START0)
@SP
A=M-1
D=M
A=A-1
D=D-M
@PUSHTRUE0
D;JGT
@PUSHFALSE0
0;JMP
(AISMINUS0)
A=A-1
@AISMINUSBISPLUS0
M;JGT
@START0
0;JMP
(AISMINUSBISPLUS0)
A=A+1
D=M
@PUSHTRUE0
D;JGT
@PUSHFALSE0
0;JMP
(BISMINUS0)
A=A+1
D=M
@AISPLUSBISMINUS0
D;JGT
@START0
0;JMP
(AISPLUSBISMINUS0)
@PUSHTRUE0
D;JGT
@PUSHFALSE0
0;JMP
(PUSHTRUE0)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
@END0
0;JMP
(PUSHFALSE0)
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
(END0)

//******if-goto IF_TRUE******
// if-goto IF_TRUE
@SP
AM=M-1
D=M
@IF_TRUE
D;JNE
//******goto IF_FALSE******
// goto IF_FALSE
@IF_FALSE
0;JMP
//******label IF_TRUE          // if n<2, return n******
// label IF_TRUE
(IF_TRUE)
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

//******label IF_FALSE         // if n>=2, returns fib(n-2)+fib(n-1)******
// label IF_FALSE
(IF_FALSE)
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

//******push constant 2******
//write_push_pop
//push constant
@2
D=A
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

//******call Main.fibonacci 1  // computes fib(n-2)******
//*****call Main.fibonacci *****
//pushing the return address
//push constant
@Main.fibonacci.1
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
@6
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
// goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci.1)
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

//******push constant 1******
//write_push_pop
//push constant
@1
D=A
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

//******call Main.fibonacci 1  // computes fib(n-1)******
//*****call Main.fibonacci *****
//pushing the return address
//push constant
@Main.fibonacci.2
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
@6
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
// goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci.2)
//******add                    // returns fib(n-1) + fib(n-2)******
//add
@SP
A=M-1
D=M
A=A-1
D=D+M
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

//******function Sys.init 0******
(Sys.init)
//lets make way for variables
//******push constant 4******
//write_push_pop
//push constant
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

//******call Main.fibonacci 1   // computes the 4'th fibonacci element******
//*****call Main.fibonacci *****
//pushing the return address
//push constant
@Main.fibonacci.3
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
@6
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
// goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci.3)
//******label WHILE******
// label WHILE
(WHILE)
//******goto WHILE              // loops infinitely******
// goto WHILE
@WHILE
0;JMP
