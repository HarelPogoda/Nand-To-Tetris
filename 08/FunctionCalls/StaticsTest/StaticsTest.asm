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
//******function Class1.set 0******
(Class1.set)
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

//******pop static 0******
//write_push_pop
//write_pop_static
@SP
A=M-1
D=M
@Class1.0
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

//******pop static 1******
//write_push_pop
//write_pop_static
@SP
A=M-1
D=M
@Class1.1
M=D
@SP
M=M-1

//******push constant 0******
//write_push_pop
//push constant
@0
D=A
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

//******function Class1.get 0******
(Class1.get)
//lets make way for variables
//******push static 0******
//write_push_pop
//write_push_static
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1

//******push static 1******
//write_push_pop
//write_push_static
@Class1.1
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

//******function Class2.set 0******
(Class2.set)
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

//******pop static 0******
//write_push_pop
//write_pop_static
@SP
A=M-1
D=M
@Class2.0
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

//******pop static 1******
//write_push_pop
//write_pop_static
@SP
A=M-1
D=M
@Class2.1
M=D
@SP
M=M-1

//******push constant 0******
//write_push_pop
//push constant
@0
D=A
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

//******function Class2.get 0******
(Class2.get)
//lets make way for variables
//******push static 0******
//write_push_pop
//write_push_static
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1

//******push static 1******
//write_push_pop
//write_push_static
@Class2.1
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

//******function Sys.init 0******
(Sys.init)
//lets make way for variables
//******push constant 6******
//write_push_pop
//push constant
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

//******push constant 8******
//write_push_pop
//push constant
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

//******call Class1.set 2******
//*****call Class1.set *****
//pushing the return address
//push constant
@Class1.set.1
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
@7
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
// goto Class1.set
@Class1.set
0;JMP
(Class1.set.1)
//******pop temp 0 // Dumps the return value******
//write_push_pop
//pop temp
@0
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

//******push constant 23******
//write_push_pop
//push constant
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

//******push constant 15******
//write_push_pop
//push constant
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

//******call Class2.set 2******
//*****call Class2.set *****
//pushing the return address
//push constant
@Class2.set.1
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
@7
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
// goto Class2.set
@Class2.set
0;JMP
(Class2.set.1)
//******pop temp 0 // Dumps the return value******
//write_push_pop
//pop temp
@0
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

//******call Class1.get 0******
//*****call Class1.get *****
//pushing the return address
//push constant
@Class1.get.1
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
// goto Class1.get
@Class1.get
0;JMP
(Class1.get.1)
//******call Class2.get 0******
//*****call Class2.get *****
//pushing the return address
//push constant
@Class2.get.1
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
// goto Class2.get
@Class2.get
0;JMP
(Class2.get.1)
//******label WHILE******
// label WHILE
(WHILE)
//******goto WHILE******
// goto WHILE
@WHILE
0;JMP
