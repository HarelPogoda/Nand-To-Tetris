"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""


class Code:
    """Translates Hack assembly language mnemonics into binary codes."""
    
    @staticmethod
    def dest(mnemonic: str) -> str:
        """
        Args:
            mnemonic (str): a dest mnemonic string.

        Returns:
            str: 3-bit long binary code of the given mnemonic.
        """
        # Your code goes here!
        binary_str="000"
        if(mnemonic=="M"):
            binary_str="001"
        elif(mnemonic=="D"):
            binary_str="010"
        elif(mnemonic=="MD"):
            binary_str="011"
        elif(mnemonic=="A"):
            binary_str="100"
        elif(mnemonic=="AM"):
            binary_str="101"
        elif(mnemonic=="AD"):
            binary_str="110"
        elif(mnemonic=="ADM"):
            binary_str="111"
        return binary_str

    @staticmethod
    def comp(mnemonic: str) -> str:
        """
        Args:
            mnemonic (str): a comp mnemonic string.

        Returns:
            str: the binary code of the given mnemonic.
        """
        # Your code goes here!
        binary_str = ""

        # Determine if it's A (a=0) or M (a=1)
        a_bit = "0"  # Default for A
        if "M" in mnemonic:
            a_bit = "1"  # Switch to 1 for M

        # Remove M or A for the lookup
        mnemonic = mnemonic.replace("M", "A")

        # Now map the comp part (without M/A)
        if mnemonic == "0":
            binary_str = "101010"
        elif mnemonic == "1":
            binary_str = "111111"
        elif mnemonic == "-1":
            binary_str = "111010"
        elif mnemonic == "D":
            binary_str = "001100"
        elif mnemonic == "A":
            binary_str = "110000"
        elif mnemonic == "!D":
            binary_str = "001101"
        elif mnemonic == "!A":
            binary_str = "110001"
        elif mnemonic == "-D":
            binary_str = "001111"
        elif mnemonic == "-A":
            binary_str = "110011"
        elif mnemonic == "D+1":
            binary_str = "011111"
        elif mnemonic == "A+1":
            binary_str = "110111"
        elif mnemonic == "D-1":
            binary_str = "001110"
        elif mnemonic == "A-1":
            binary_str = "110010"
        elif mnemonic == "D+A":
            binary_str = "000010"
        elif mnemonic == "D-A":
            binary_str = "010011"
        elif mnemonic == "A-D":
            binary_str = "000111"
        elif mnemonic == "D&A":
            binary_str = "000000"
        elif mnemonic == "D|A":
            binary_str = "010101"

        # Return the full 7-bit comp code including the a-bit
        return a_bit + binary_str



    @staticmethod
    def jump(mnemonic: str) -> str:
        """
        Args:
            mnemonic (str): a jump mnemonic string.

        Returns:
            str: 3-bit long binary code of the given mnemonic.
        """
        # Your code goes here!
        binary_str="000"
        if(mnemonic=="JGT"):
            binary_str="001"
        elif (mnemonic == "JEQ"):
            binary_str = "010"
        elif (mnemonic == "JGE"):
            binary_str = "011"
        elif (mnemonic == "JLT"):
            binary_str = "100"
        elif (mnemonic == "JNE"):
            binary_str = "101"
        elif (mnemonic == "JLE"):
            binary_str = "110"
        elif (mnemonic == "JMP"):
            binary_str = "111"
        return binary_str
