//push constant
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

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
D;JEQ
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
D;JEQ
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
D;JEQ
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

//push constant
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

//eq or lt or gt
@SP
A=M-1
@AISMINUS2
M;JLT
A=A-1
@BISMINUS2
M;JLT
(START2)
@SP
A=M-1
D=M
A=A-1
D=D-M
@PUSHTRUE2
D;JEQ
@PUSHFALSE2
0;JMP
(AISMINUS2)
A=A-1
@AISMINUSBISPLUS2
M;JGT
@START2
0;JMP
(AISMINUSBISPLUS2)
A=A+1
D=M
@PUSHTRUE2
D;JEQ
@PUSHFALSE2
0;JMP
(BISMINUS2)
A=A+1
D=M
@AISPLUSBISMINUS2
D;JGT
@START2
0;JMP
(AISPLUSBISMINUS2)
@PUSHTRUE2
D;JEQ
@PUSHFALSE2
0;JMP
(PUSHTRUE2)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
@END2
0;JMP
(PUSHFALSE2)
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
(END2)

//push constant
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//eq or lt or gt
@SP
A=M-1
@AISMINUS4
M;JLT
A=A-1
@BISMINUS4
M;JLT
(START4)
@SP
A=M-1
D=M
A=A-1
D=D-M
@PUSHTRUE4
D;JEQ
@PUSHFALSE4
0;JMP
(AISMINUS4)
A=A-1
@AISMINUSBISPLUS4
M;JGT
@START4
0;JMP
(AISMINUSBISPLUS4)
A=A+1
D=M
@PUSHTRUE4
D;JEQ
@PUSHFALSE4
0;JMP
(BISMINUS4)
A=A+1
D=M
@AISPLUSBISMINUS4
D;JGT
@START4
0;JMP
(AISPLUSBISMINUS4)
@PUSHTRUE4
D;JEQ
@PUSHFALSE4
0;JMP
(PUSHTRUE4)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
@END4
0;JMP
(PUSHFALSE4)
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
(END4)

//push constant
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//eq or lt or gt
@SP
A=M-1
@AISMINUS6
M;JLT
A=A-1
@BISMINUS6
M;JLT
(START6)
@SP
A=M-1
D=M
A=A-1
D=D-M
@PUSHTRUE6
D;JGT
@PUSHFALSE6
0;JMP
(AISMINUS6)
A=A-1
@AISMINUSBISPLUS6
M;JGT
@START6
0;JMP
(AISMINUSBISPLUS6)
A=A+1
D=M
@PUSHTRUE6
D;JGT
@PUSHFALSE6
0;JMP
(BISMINUS6)
A=A+1
D=M
@AISPLUSBISMINUS6
D;JGT
@START6
0;JMP
(AISPLUSBISMINUS6)
@PUSHTRUE6
D;JGT
@PUSHFALSE6
0;JMP
(PUSHTRUE6)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
@END6
0;JMP
(PUSHFALSE6)
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
(END6)

//push constant
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

//eq or lt or gt
@SP
A=M-1
@AISMINUS8
M;JLT
A=A-1
@BISMINUS8
M;JLT
(START8)
@SP
A=M-1
D=M
A=A-1
D=D-M
@PUSHTRUE8
D;JGT
@PUSHFALSE8
0;JMP
(AISMINUS8)
A=A-1
@AISMINUSBISPLUS8
M;JGT
@START8
0;JMP
(AISMINUSBISPLUS8)
A=A+1
D=M
@PUSHTRUE8
D;JGT
@PUSHFALSE8
0;JMP
(BISMINUS8)
A=A+1
D=M
@AISPLUSBISMINUS8
D;JGT
@START8
0;JMP
(AISPLUSBISMINUS8)
@PUSHTRUE8
D;JGT
@PUSHFALSE8
0;JMP
(PUSHTRUE8)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
@END8
0;JMP
(PUSHFALSE8)
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
(END8)

//push constant
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//eq or lt or gt
@SP
A=M-1
@AISMINUS10
M;JLT
A=A-1
@BISMINUS10
M;JLT
(START10)
@SP
A=M-1
D=M
A=A-1
D=D-M
@PUSHTRUE10
D;JGT
@PUSHFALSE10
0;JMP
(AISMINUS10)
A=A-1
@AISMINUSBISPLUS10
M;JGT
@START10
0;JMP
(AISMINUSBISPLUS10)
A=A+1
D=M
@PUSHTRUE10
D;JGT
@PUSHFALSE10
0;JMP
(BISMINUS10)
A=A+1
D=M
@AISPLUSBISMINUS10
D;JGT
@START10
0;JMP
(AISPLUSBISMINUS10)
@PUSHTRUE10
D;JGT
@PUSHFALSE10
0;JMP
(PUSHTRUE10)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
@END10
0;JMP
(PUSHFALSE10)
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
(END10)

//push constant
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//eq or lt or gt
@SP
A=M-1
@AISMINUS12
M;JLT
A=A-1
@BISMINUS12
M;JLT
(START12)
@SP
A=M-1
D=M
A=A-1
D=D-M
@PUSHTRUE12
D;JLT
@PUSHFALSE12
0;JMP
(AISMINUS12)
A=A-1
@AISMINUSBISPLUS12
M;JGT
@START12
0;JMP
(AISMINUSBISPLUS12)
A=A+1
D=M
@PUSHTRUE12
D;JLT
@PUSHFALSE12
0;JMP
(BISMINUS12)
A=A+1
D=M
@AISPLUSBISMINUS12
D;JGT
@START12
0;JMP
(AISPLUSBISMINUS12)
@PUSHTRUE12
D;JLT
@PUSHFALSE12
0;JMP
(PUSHTRUE12)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
@END12
0;JMP
(PUSHFALSE12)
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
(END12)

//push constant
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

//eq or lt or gt
@SP
A=M-1
@AISMINUS14
M;JLT
A=A-1
@BISMINUS14
M;JLT
(START14)
@SP
A=M-1
D=M
A=A-1
D=D-M
@PUSHTRUE14
D;JLT
@PUSHFALSE14
0;JMP
(AISMINUS14)
A=A-1
@AISMINUSBISPLUS14
M;JGT
@START14
0;JMP
(AISMINUSBISPLUS14)
A=A+1
D=M
@PUSHTRUE14
D;JLT
@PUSHFALSE14
0;JMP
(BISMINUS14)
A=A+1
D=M
@AISPLUSBISMINUS14
D;JGT
@START14
0;JMP
(AISPLUSBISMINUS14)
@PUSHTRUE14
D;JLT
@PUSHFALSE14
0;JMP
(PUSHTRUE14)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
@END14
0;JMP
(PUSHFALSE14)
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
(END14)

//push constant
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//eq or lt or gt
@SP
A=M-1
@AISMINUS16
M;JLT
A=A-1
@BISMINUS16
M;JLT
(START16)
@SP
A=M-1
D=M
A=A-1
D=D-M
@PUSHTRUE16
D;JLT
@PUSHFALSE16
0;JMP
(AISMINUS16)
A=A-1
@AISMINUSBISPLUS16
M;JGT
@START16
0;JMP
(AISMINUSBISPLUS16)
A=A+1
D=M
@PUSHTRUE16
D;JLT
@PUSHFALSE16
0;JMP
(BISMINUS16)
A=A+1
D=M
@AISPLUSBISMINUS16
D;JGT
@START16
0;JMP
(AISPLUSBISMINUS16)
@PUSHTRUE16
D;JLT
@PUSHFALSE16
0;JMP
(PUSHTRUE16)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
@END16
0;JMP
(PUSHFALSE16)
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
(END16)

//push constant
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant
@53
D=A
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

//push constant
@112
D=A
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

//neg
@SP
A=M-1
M=-M

//and 
@SP
A=M-1
D=M
A=A-1
M=D&M
@SP
M=M-1

//push constant
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

//or
@SP
A=M-1
D=M
A=A-1
M=D|M
@SP
M=M-1

//not
@SP
A=M-1
M=!M

