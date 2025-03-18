"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing


class Parser:
    """
    # Parser
    
    Handles the parsing of a single .vm file, and encapsulates access to the
    input code. It reads VM commands, parses them, and provides convenient 
    access to their components. 
    In addition, it removes all white space and comments.

    ## VM Language Specification

    A .vm file is a stream of characters. If the file represents a
    valid program, it can be translated into a stream of valid assembly 
    commands. VM commands may be separated by an arbitrary number of whitespace
    characters and comments, which are ignored. Comments begin with "//" and
    last until the lines end.
    The different parts of each VM command may also be separated by an arbitrary
    number of non-newline whitespace characters.

    - Arithmetic commands:
      - add, sub, and, or, eq, gt, lt
      - neg, not, shiftleft, shiftright
    - Memory segment manipulation:
      - push <segment> <number>
      - pop <segment that is not constant> <number>
      - <segment> can be any of: argument, local, static, constant, this, that, 
                                 pointer, temp
    - Branching (only relevant for project 8):
      - label <label-name>
      - if-goto <label-name>
      - goto <label-name>
      - <label-name> can be any combination of non-whitespace characters.
    - Functions (only relevant for project 8):
      - call <function-name> <n-args>
      - function <function-name> <n-vars>
      - return
    """

    def __init__(self, input_file: typing.TextIO) -> None:
        """Gets ready to parse the input file.

        Args:
            input_file (typing.TextIO): input file.
        """
        # Your code goes here!
        # A good place to start is to read all the lines of the input:
        # input_lines = input_file.read().splitlines()
        # list of strings
        input_lines = input_file.read().splitlines()
        self.lines = input_lines
        self.current_index = 0  # Keep track of which line we're on
        self.current_command = None  # Store the current command


    def has_more_commands(self) -> bool:
        """Are there more commands in the input?

        Returns:
            bool: True if there are more commands, False otherwise.
        """
        # Your code goes here!
        length_of_lines = len(self.lines)
        if (length_of_lines - self.current_index > 0):
            return True
        return False


    def advance(self) -> None:
        """Reads the next command from the input and makes it the current 
        command. Should be called only if has_more_commands() is true. Initially
        there is no current command.
        """
        # Your code goes here!
        while self.has_more_commands():
            self.current_command = self.lines[self.current_index].strip()
            self.current_index += 1
            # Skip empty lines and comments
            if self.current_command == "" or self.current_command.startswith("//"):
                continue  # Continue skipping to the next line
            break  # We found a valid command, so break the loop


    def command_type(self) -> str:
        """
        Returns:
            str: the type of the current VM command.
            "C_ARITHMETIC" is returned for all arithmetic commands.
            For other commands, can return:
            "C_PUSH", "C_POP", "C_LABEL", "C_GOTO", "C_IF", "C_FUNCTION",
            "C_RETURN", "C_CALL".
        """
        arguments = self.current_command.split()

        # Your code goes here!
        if arguments[0]=="goto":
            return "C_GOTO"
        elif arguments[0]=="label":
            return "C_LABEL"
        elif arguments[0]=="if-goto":
            return "C_IF"
        elif arguments[0]=="function":
            return "C_FUNCTION"
        elif arguments[0]=="return":
            return "C_RETURN"
        elif arguments[0]=="call":
            return "C_CALL"
        elif arguments[0]=="push":
            return "C_PUSH"
        elif arguments[0]=="pop":
            return "C_POP"
        else:
            return "C_ARITHMETIC"


    def arg1(self) -> str:
        """
        Returns:
            str: the first argument of the current command. In case of 
            "C_ARITHMETIC", the command itself (add, sub, etc.) is returned. 
            Should not be called if the current command is "C_RETURN".
        """
        # Your code goes here!
        # Split the string into a list of words
        arguments = self.current_command.split()
        if (self.command_type() == "C_ARITHMETIC"):
            return self.current_command
        else:
            return str(arguments[0] + " " + arguments[1])  # the first and second word of the current command



    def arg2(self) -> int:
        """
        Returns:
            int: the second argument of the current command. Should be
            called only if the current command is "C_PUSH", "C_POP", 
            "C_FUNCTION" or "C_CALL".
        """
        # Your code goes here!
        if (self.command_type()=="C_PUSH" or self.command_type()=="C_POP"
                or self.command_type()=="C_FUNCTION" or self.command_type()=="C_CALL"):
            arguments = self.current_command.split()
            # the second word (as integer) of the current command
            return int(arguments[2])
