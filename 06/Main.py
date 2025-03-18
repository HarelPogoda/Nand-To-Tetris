"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import os
import sys
import typing
from SymbolTable import SymbolTable
from Parser import Parser
from Code import Code


def assemble_file(
        input_file: typing.TextIO, output_file: typing.TextIO) -> None:
    """Assembles a single file.

    Args:
        input_file (typing.TextIO): the file to assemble.
        output_file (typing.TextIO): writes all output to this file.
    """
    # Your code goes here!
    # A good place to start is to initialize a new Parser object:
    # parser = Parser(input_file)
    # Note that you can write to output_file like so:
    # output_file.write("Hello world! \n")

    # First pass- reads all the program lines, focusing only on (label)
    #declarations. Adds the found labels to the symbol table
    # Initialize parser and symbol table
    parser = Parser(input_file)
    symbol_table = SymbolTable()

    # First pass - handle labels
    first_pass(parser, symbol_table)

    # Proceed with the second pass...
    code=Code()
    second_pass(parser, symbol_table, code)



def first_pass(parser: Parser, symbol_table: SymbolTable) -> None:
    """First pass: reads all the program lines, focusing on (label) declarations,
    and adds the found labels to the symbol table.

    Args:
        parser (Parser): The Parser object that reads the assembly file.
        symbol_table (SymbolTable): The symbol table that stores label declarations.
    """
    instruction_address = 0  # Track the address of each instruction (excluding labels)

    while parser.has_more_commands():
        parser.advance()
        command_type = parser.command_type()

        if command_type == "L_COMMAND":
            # Extract label symbol and add it to the symbol table with the current instruction address
            label = parser.symbol()  # This will give you the label (without parentheses)
            symbol_table.add_entry(label, instruction_address)
        elif command_type == "A_COMMAND" or command_type == "C_COMMAND":
            # Only increment instruction address for A and C commands (not for labels)
            instruction_address += 1

def second_pass(parser: Parser, symbol_table: SymbolTable, code: Code) -> None:
    # Reset the parser to the beginning of the file
    parser.current_index = 0

    while parser.has_more_commands():
        # Gets the next instruction and parses it
        parser.advance()
        command_type = parser.command_type()

        #If the instruction is @symbol:
        if command_type == "A_COMMAND":

            symbol = parser.symbol()
            # Check if the symbol is a number (constant), if so, convert it directly
            if symbol.isdigit():
                address = int(symbol)
            else:
                # If the symbol is not in the symbol table, add it with the next available address
                if not symbol_table.contains(symbol):
                    symbol_table.add_entry(symbol, symbol_table.next_avaliable_address)
                    symbol_table.next_avaliable_address += 1

                # Get the address of the symbol from the symbol table
                address = symbol_table.get_address(symbol)

            # Convert the address to a 16-bit binary string (A-instruction starts with '0')
            binary_value = f"{address:016b}"

        # If the instruction is dest=comp; jump
        elif command_type == "C_COMMAND":
            binary_dest = code.dest(parser.dest())
            binary_comp = code.comp(parser.comp())
            binary_jump = code.jump(parser.jump())

            # C-instruction starts with '111'
            binary_value = "111" + binary_comp + binary_dest + binary_jump
            # binary_value=binary_dest+binary_comp+binary_jump

        # Write the binary value to the output file (each instruction is 16 bits long)
        if parser.current_command[0] != "(":
            output_file.write(binary_value + '\n')

if "__main__" == __name__:
    # Parses the input path and calls assemble_file on each input file.
    # This opens both the input and the output files!
    # Both are closed automatically when the code finishes running.
    # If the output file does not exist, it is created automatically in the
    # correct path, using the correct filename.
    if not len(sys.argv) == 2:
        sys.exit("Invalid usage, please use: Assembler <input path>")
    argument_path = os.path.abspath(sys.argv[1])
    if os.path.isdir(argument_path):
        files_to_assemble = [
            os.path.join(argument_path, filename)
            for filename in os.listdir(argument_path)]
    else:
        files_to_assemble = [argument_path]
    for input_path in files_to_assemble:
        filename, extension = os.path.splitext(input_path)
        if extension.lower() != ".asm":
            continue
        output_path = filename + ".hack"
        with open(input_path, 'r') as input_file, \
                open(output_path, 'w') as output_file:
            assemble_file(input_file, output_file)
