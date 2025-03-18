"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing


class Parser:
    """Encapsulates access to the input code. Reads an assembly program
    by reading each command line-by-line, parses the current command,
    and provides convenient access to the commands components (fields
    and symbols). In addition, removes all white space and comments.
    """

    def __init__(self, input_file: typing.TextIO) -> None:
        """Opens the input file and gets ready to parse it.

        Args:
            input_file (typing.TextIO): input file.
        """
        # Your code goes here!
        # A good place to start is to read all the lines of the input:
        # input_lines = input_file.read().splitlines()

        #list of strings
        input_lines = input_file.read().splitlines()
        for i in range (len(input_lines)):
            input_lines[i] = input_lines[i].split("//")[0].strip()
        self.lines = input_lines
        self.current_index = 0  # Keep track of which line we're on
        self.current_command = None  # Store the current command


    def has_more_commands(self) -> bool:
        """Are there more commands in the input?

        Returns:
            bool: True if there are more commands, False otherwise.
        """
        if(self.current_index < len(self.lines)):
            return True
        return False



    def advance(self) -> None:
        """Reads the next command from the input and makes it the current command.
        Should be called only if has_more_commands() is true.
        """
        while self.has_more_commands():
            self.current_command = self.lines[self.current_index].strip()
            self.current_index += 1
            # Skip empty lines and comments
            if self.current_command == "" or self.current_command.startswith("//"):
                continue  # Continue skipping to the next line
            if "//" in self.current_command:
                self.current_command.split("//")[0].strip()
                self.current_command = self.current_command.strip()
            break  # We found a valid command, so break the loop


    def command_type(self) -> str:
        """
        Returns:
            str: the type of the current command:
            "A_COMMAND" for @Xxx where Xxx is either a symbol or a decimal number
            "C_COMMAND" for dest=comp;jump
            "L_COMMAND" (actually, pseudo-command) for (Xxx) where Xxx is a symbol
        """
        first_char = self.current_command[0]
        if first_char == '@':
            return "A_COMMAND"
        elif first_char == '(' and self.current_command[-1] == ')':
            return "L_COMMAND"
        else:
            return "C_COMMAND"


    def symbol(self) -> str:
        """
        Returns:
            str: the symbol or decimal Xxx of the current command @Xxx or
            (Xxx). Should be called only when command_type() is "A_COMMAND" or 
            "L_COMMAND".
        """
        # Your code goes here!
        command_str = self.command_type()
        if command_str == "A_COMMAND":
            # Remove the '@' and return the rest
            return self.current_command[1:]
        elif command_str == "L_COMMAND":
            # Remove the '(' and ')' and return the rest
            return self.current_command[1:-1]
        return ""



    def dest(self) -> str:
        """
        Returns:
            str: the dest mnemonic in the current C-command. Should be called 
            only when commandType() is "C_COMMAND".
        """
        # Your code goes here!
        dest_mnemonic = ""
        counter = 0

        if self.command_type() == "C_COMMAND":
            # Find the dest part (everything before '=')
            while counter < len(self.current_command) and self.current_command[counter] != "=":
                dest_mnemonic += self.current_command[counter]
                counter += 1

            # If there was no '=', it means there's no dest
            if dest_mnemonic == self.current_command:
                return ""

            return dest_mnemonic


    def comp(self) -> str:
        """
        Returns:
            str: the comp mnemonic in the current C-command. Should be called 
            only when commandType() is "C_COMMAND".
        """
        # Your code goes here!
        comp_mnemonic = ""
        counter = 0

        if self.command_type() == "C_COMMAND":
            # Skip until '=' if there's a dest part
            while counter < len(self.current_command) and self.current_command[counter] != "=":
                counter += 1

            # Start reading the comp part (between '=' and ';')
            if counter < len(self.current_command):
                counter += 1  # Move past the '='

            while counter < len(self.current_command) and self.current_command[counter] != ";":
                comp_mnemonic += self.current_command[counter]
                counter += 1

            if comp_mnemonic == "":
                counter = 0;
                while self.current_command[counter] != ";":
                    comp_mnemonic += self.current_command[counter]
                    counter += 1

            return comp_mnemonic


    def jump(self) -> str:
        """
        Returns:
            str: the jump mnemonic in the current C-command. Should be called 
            only when commandType() is "C_COMMAND".
        """
        # Your code goes here!
        jump_mnemonic = ""
        counter = 0

        if self.command_type() == "C_COMMAND":
            # Find where the ';' is, indicating the start of the jump mnemonic
            while counter < len(self.current_command) and self.current_command[counter] != ";":
                counter += 1

            # If ';' is found, extract the jump part
            if counter < len(self.current_command):
                counter += 1  # Move past the ';'
                while counter < len(self.current_command):
                    jump_mnemonic += self.current_command[counter]
                    counter += 1

            return jump_mnemonic

