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

//******pop pointer 1           // that = argument[1]******
//write_push_pop
//write_pop_pointer 1
@SP
A=M-1
D=M
@THAT
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

//******pop that 0              // first element in the series = 0******
//write_push_pop
//pop
@0
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

//******pop that 1              // second element in the series = 1******
//write_push_pop
//pop
@1
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

//******pop argument 0          // num_of_elements -= 2 (first 2 elements are set)******
//write_push_pop
//pop
@0
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

//******label MAIN_LOOP_START******
// label MAIN_LOOP_START
(MAIN_LOOP_START)
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

//******if-goto COMPUTE_ELEMENT // if num_of_elements > 0, goto COMPUTE_ELEMENT******
// if-goto COMPUTE_ELEMENT
@SP
AM=M-1
D=M
@COMPUTE_ELEMENT
D;JNE
//******goto END_PROGRAM        // otherwise, goto END_PROGRAM******
// goto END_PROGRAM
@END_PROGRAM
0;JMP
//******label COMPUTE_ELEMENT******
// label COMPUTE_ELEMENT
(COMPUTE_ELEMENT)
//******push that 0******
//write_push_pop
//write_push
@0
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

//******push that 1******
//write_push_pop
//write_push
@1
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

//******pop that 2              // that[2] = that[0] + that[1]******
//write_push_pop
//pop
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

//******push pointer 1******
//write_push_pop
//push pointer1
//push segment pointer
@THAT
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

//******pop pointer 1           // that += 1******
//write_push_pop
//write_pop_pointer 1
@SP
A=M-1
D=M
@THAT
M=D
@SP
M=M-1

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

//******pop argument 0          // num_of_elements--******
//write_push_pop
//pop
@0
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

//******goto MAIN_LOOP_START******
// goto MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP
//******label END_PROGRAM******
// label END_PROGRAM
(END_PROGRAM)
