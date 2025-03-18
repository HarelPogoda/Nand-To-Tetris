// This file is part of nand2tetris, as taught in The Hebrew University, and
// was written by Aviv Yaish. It is an extension to the specifications given
// [here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
// as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
// Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

// The program should swap between the max. and min. elements of an array.
// Assumptions:
// - The array's start address is stored in R14, and R15 contains its length
// - Each array value x is between -16384 < x < 16384
// - The address in R14 is at least >= 2048
// - R14 + R15 <= 16383
//
// Requirements:
// - Changing R14, R15 is not allowed.

// Put your code here.


@R14
D=M
@MAX
M=D
@MIN
M=D
@POINTER
M=D

(LOOP)
    // UPDATE POINTER
    @POINTER
    M=M+1

    // CHECK IF POINTER IS EQUAL TO R15+R14
    @R15
    D=M
    @R14
    D=D+M
    @POINTER
    D=D-M

    // JUMP TO END IF SO
    @ENDLOOP
    D;JLE

    // CHECK IF THE VALUE IN POINTER IS LARGER THAN MAX
    @POINTER
    D=M
    A=D
    D=M
    @MAX
    A=M
    D=D-M
    @UPDATEMAX
    D;JGT

    // ELSE:
    @CHECKMIN
    0;JMP
    //UPDATE MAX

    (UPDATEMAX)
    @POINTER
    D=M
    @MAX
    M=D

    // CHECK IF SMALLER THAN MIN
    (CHECKMIN)
    @POINTER
    D=M
    A=D
    D=M
    @MIN
    A=M
    D=D-M
    @UPDATEMIN
    D;JLT
    // ELSE
    @LOOP
    0;JMP

    // UPDATE MIN
    (UPDATEMIN)
    @POINTER
    D=M
    @MIN
    M=D

    // UNCONDITIONAL JUMP TO LOOP CUZ WE'VE CHECKED WETHER THIS IS THE END OF THE ARRAY
    @LOOP
    0;JMP

(ENDLOOP)

// SWITCHING
@MAX
D=M
A=D
D=M
@TEMPMAX // HOLDING THE MAX VALUE
M=D
@MIN
D=M
A=D
D=M
@MAX // PUT MINIMUM INTO MAXIMUM
A=M
M=D
@TEMPMAX
D=M
@MIN // PUT WHAT WAS IN MAXIMUM IN MINIMUM
A=M
M=D
(ENDPROGRAM)

@ENDPROGRAM
0;JMP
