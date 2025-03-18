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

//******pop local 0         // initializes sum = 0******
//write_push_pop
//pop
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

//******label LOOP_START******
// label LOOP_START
(LOOP_START)
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

//******pop local 0	        // sum = sum + counter******
//write_push_pop
//pop
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

//******pop argument 0      // counter--******
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

//******if-goto LOOP_START  // If counter != 0, goto LOOP_START******
// if-goto LOOP_START
@SP
AM=M-1
D=M
@LOOP_START
D;JNE
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

