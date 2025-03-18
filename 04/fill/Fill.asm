// This file is part of nand2tetris, as taught in The Hebrew University, and
// was written by Aviv Yaish. It is an extension to the specifications given
// [here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
// as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
// Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

// This program illustrates low-level handling of the screen and keyboard
// devices, as follows.
//
// The program runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.
// 
// Assumptions:
// Your program may blacken and clear the screen's pixels in any spatial/visual
// Order, as long as pressing a key continuously for long enough results in a
// fully blackened screen, and not pressing any key for long enough results in a
// fully cleared screen.
//
// Test Scripts:
// For completeness of testing, test the Fill program both interactively and
// automatically.
// 
// The supplied FillAutomatic.tst script, along with the supplied compare file
// FillAutomatic.cmp, are designed to test the Fill program automatically, as 
// described by the test script documentation.
//
// The supplied Fill.tst script, which comes with no compare file, is designed
// to do two things:
// - Load the Fill.hack program
// - Remind you to select 'no animation', and then test the program
//   interactively by pressing and releasing some keyboard keys

// Put your code here

// M=-1 for black, M=0 for white

(START)
    @KBD       // Check if any key is pressed
    D=M        // Load keyboard state into D register
    
    @color
    M=-1
    @DRAW_SCREEN
    D;JGT      // If any key is pressed, set black color

    @color
    M=0       // Set color to white if no key is pressed
    @DRAW_SCREEN
    0;JMP      // Jump to draw the screen


// draw the screen based on @color
(DRAW_SCREEN)
    @SCREEN    // Load base address of the screen
    D=A
    @ptr       // Store it in a pointer
    M=D

    @8192      // Set a counter for 8192 iterations (512*256/16)
    D=A
    @counter
    M=D

// Loop over the entire screen
(FILL_SCREEN_LOOP)
    @color     // Load the current color (black or white)
    D=M
    @ptr       // Get the pointer to the current screen address
    A=M        // Dereference the pointer (A = *ptr)
    M=D        // Set the pixel to the current color

    @ptr       // Increment the pointer
    M=M+1

    @24576     // Check if pointer exceeds 24575 (end of screen memory)
    D=A
    @ptr
    A=Ms
    D=D-A
    @START
    D;JEQ      // If pointer exceeds 24575, restart the loop

    @counter   // Decrement the counter
    M=M-1
    D=M
    @START     // If counter == 0, restart the program
    D;JEQ      // Exit loop when counter is 0
    @FILL_SCREEN_LOOP
    0;JMP      // Jump back to fill the next pixel
