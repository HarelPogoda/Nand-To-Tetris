// Test A = A <<; jump
load CpuMul.hdl,
output-file CpuMulShift.out,

output-list time%S0.4.0 inM%D0.6.0 instruction%B0.16.0 reset%B2.1.2 outM%D1.6.0 writeM%B3.1.3 addressM%D0.5.0 pc%D0.5.0 DRegister[]%D1.6.1;

set instruction %B0011000000111001, // @12345 (set A to 12345)
tick, output, tock, output;

set instruction %B1010100000010111, // A = A <<; jump
tick, output, tock, output;
