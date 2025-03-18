// This file is part of nand2tetris, as taught in The Hebrew University, and
// was written by Aviv Yaish. It is an extension to the specifications given
// [here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
// as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
// Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

// Multiplies R0 and R1 and stores the result in R2.
//
// Assumptions:
// - R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.
// - You can assume that you will only receive arguments that satisfy:
//   R0 >= 0, R1 >= 0, and R0*R1 < 32768.
// - Your program does not need to test these conditions.
//
// Requirements:
// - Your program should not change the values stored in R0 and R1.
// - You can implement any multiplication algorithm you want.

// Put your code here.

    //result=0                                                                               
    @result
    M=0
    //counter=0
    @counter
    M=0

(LOOP)
    //if (counter>=R0) goto STOP
    @counter
    D=M
    @R0
    D=D-M
    @STOP
    D;JGE 

    //result=result+R1
    @result
    D=M
    @R1
    D=D+M
    @result
    M=D

    //counter=counter+1    
    @counter
    M=M+1    

    //goto LOOP
    @LOOP
    0;JMP


(STOP)
    //R2=result
    @result
    D=M
    @R2
    M=D

//Infinite Loop
(END)
    @END
    0;JMP
