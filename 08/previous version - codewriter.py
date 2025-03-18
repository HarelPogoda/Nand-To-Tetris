"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing

COMMANDS_TO_STRINGS = {
    "sub": "//sub\n"
           "@SP\n"
           "A=M-1\n"
           "D=M\n"
           "A=A-1\n"
           "D=M-D\n"
           "M=D\n"
           "@SP\n"
           "M=M-1\n\n",

    "add": "//add\n"
           "@SP\n"
           "A=M-1\n"
           "D=M\n"
           "A=A-1\n"
           "D=D+M\n"
           "M=D\n"
           "@SP\n"
           "M=M-1\n\n",

    "neg": "//neg\n"
           "@SP\n"
           "A=M-1\n"
           "M=-M\n\n",

    "and": "//and \n"
           "@SP\n"
           "A=M-1\n"
           "D=M\n"
           "A=A-1\n"
           "M=D&M\n"
           "@SP\n"
           "M=M-1\n\n",

    "or": "//or\n"
          "@SP\n"
          "A=M-1\n"
          "D=M\n"
          "A=A-1\n"
          "M=D|M\n"
          "@SP\n"
          "M=M-1\n\n",

    "not": "//not\n"
           "@SP\n"
           "A=M-1\n"
           "M=!M\n\n"
}

SEGMENTS = {
    "local": "LCL",
    "argument": "ARG",
    "this": "THIS",
    "that": "THAT",
    "temp": "TEMP",
    "static": "STATIC",
    "pointer": "POINTER",
    "constant": "CONSTANT"
}


class CodeWriter:
    """Translates VM commands into Hack assembly code."""

    label_count = 0  # Static variable to make all labels unique -
    # otherwise assembly gets confused
    funcount = {}  # counter for return addresses, for functions

    def __init__(self, output_stream: typing.TextIO) -> None:
        """Initializes the CodeWriter.

        Args:
            output_stream (typing.TextIO): output stream.
        """
        # Your code goes here!
        # Note that you can write to output_stream like so:
        # output_stream.write("Hello world! \n")

        self.current_file = None
        self.output_stream = output_stream

    def set_file_name(self, filename: str) -> None:
        """Informs the code writer that the translation of a new VM file is
        started.

        Args:
            filename (str): The name of the VM file.
        """
        # Your code goes here!
        # This function is useful when translating code that handles the
        # static segment. For example, in order to prevent collisions between two
        # .vm files which push/pop to the static segment, one can use the current
        # file's name in the assembly variable's name and thus differentiate between
        # static variables belonging to different files.
        # To avoid problems with Linux/Windows/MacOS differences with regards
        # to filenames and paths, you are advised to parse the filename in
        # the function "translate_file" in Main.py using python's os library,
        # For example, using code similar to:
        # input_filename, input_extension = os.path.splitext(os.path.basename(input_file.name))

        self.current_file = filename

    def write_comparison_command(self, command):
        comparison_types = {"eq": "D;JEQ", "lt": "D;JGT", "gt": "D;JLT"}
        self.output_stream.write("//eq\n"
                                 "@SP\n"
                                 "A=M-1\n"
                                 "D=M\n"
                                 "A=A-1\n"
                                 "D=D-M\n"
                                 "@PUSHTRUE" + str(self.label_count) + "\n")
        self.output_stream.write(comparison_types.get(command) + "\n")
        self.output_stream.write("@PUSHFALSE" + str(self.label_count) + "\n"
                                 "0;JMP\n"
                                 "(PUSHTRUE" + str(self.label_count) + ")\n"
                                 "@SP\n"
                                 "A=M-1\n"
                                 "A=A-1\n"
                                 "M=-1\n"
                                 "@SP\n"
                                 "M=M-1\n"
                                 "@END" + str(self.label_count) + "\n"
                                 "0;JMP\n"
                                 "(PUSHFALSE" + str(self.label_count) + ")\n"
                                 "@SP\n"
                                 "A=M-1\n"
                                 "A=A-1\n"
                                 "M=0\n"
                                 "@SP\n"
                                 "M=M-1\n"
                                 "(END" + str(self.label_count) + ")\n\n")

    def write_arithmetic(self, command: str) -> None:
        """Writes assembly code that is the translation of the given
        arithmetic command. For the commands eq, lt, gt, you should correctly
        compare between all numbers our computer supports, and we define the
        value "true" to be -1, and "false" to be 0.

        Args:
            command (str): an arithmetic command.
        """
        # Your code goes here!
        if command in ["eq", "lt", "gt"]:
            self.write_comparison_command(command)
            self.label_count += 1
        else:
            assembly_translation = COMMANDS_TO_STRINGS.get(command)
            if assembly_translation is None:
                raise ValueError(f"{command} is Invalid")
            self.output_stream.write(assembly_translation)

    def write_push_segment_pointer(self, segment: str):
        # pushes the address of the segment on top of the stack
        self.output_stream.write("//push segment pointer\n"
                                 "@" + segment + "\n"
                                 "D=M\n"
                                 "@SP\n"
                                 "A=M\n"
                                 "M=D\n"
                                 "@SP\n"
                                 "M=M+1\n\n")

    def write_push_constant(self, value_to_push):
        self.output_stream.write("//push constant\n"
                                 "@" + str(value_to_push) + "\n"
                                 "D=A\n" +
                                 "@SP\n"
                                 "A=M\n"
                                 "M=D\n"
                                 "@SP\n"
                                 "M=M+1\n\n")

    def write_push_temp(self, index):
        self.output_stream.write("//push temp\n"
                                 "@" + str(index) + "\n"
                                 "D=A\n"
                                 "@5\n"
                                 "A=A+D\n"
                                 "D=M\n"
                                 "@SP\n"
                                 "A=M\n"
                                 "M=D\n"
                                 "@SP\n"
                                 "M=M+1\n\n")

    def write_pop_temp(self, index):
        self.output_stream.write("//pop temp\n"
                                 "@" + str(index) + "\n"
                                 "D=A\n"
                                 "@5\n"
                                 "D=A+D\n"
                                 "@SP\n"
                                 "A=M\n"
                                 "M=D\n"
                                 "A=A-1\n"
                                 "D=M\n"
                                 "A=A+1\n"
                                 "A=M\n"
                                 "M=D\n"
                                 "@SP\n"
                                 "M=M-1\n\n")

    def write_pop_pointer(self, index):
        if index == 0:
            self.output_stream.write("//write_pop_pointer 0\n"
                                     "@SP\n"
                                     "A=M-1\n"
                                     "D=M\n"
                                     "@THIS\n"
                                     "M=D\n"
                                     "@SP\n"
                                     "M=M-1\n\n")
        elif index == 1:
            self.output_stream.write("//write_pop_pointer 1\n"
                                     "@SP\n"
                                     "A=M-1\n"
                                     "D=M\n"
                                     "@THAT\n"
                                     "M=D\n"
                                     "@SP\n"
                                     "M=M-1\n\n")

    def write_push_static(self, index: str):
        self.output_stream.write("//write_push_static\n"
                                 "@" + index + "\n"
                                 "D=M\n"
                                 "@SP\n"
                                 "A=M\n"
                                 "M=D\n"
                                 "@SP\n"
                                 "M=M+1\n\n")

    def write_pop_static(self, index: str):
        self.output_stream.write("//write_pop_static\n"
                                 "@SP\n"
                                 "A=M-1\n"
                                 "D=M\n"
                                 "@" + index + "\n"
                                 "M=D\n"
                                 "@SP\n"
                                 "M=M-1\n\n")

    def write_push(self, segment, index):
        self.output_stream.write("//write_push\n"
                                 "@" + str(index) + "\n"
                                 "D=A\n"
                                 "@" + segment + "\n"
                                 "D=M+D\n"
                                 "A=D\n"
                                 "D=M\n"
                                 "@SP\n"
                                 "A=M\n"
                                 "M=D\n"
                                 "@SP\n"
                                 "M=M+1\n\n")

    def write_pop(self, segment, index):
        self.output_stream.write("//pop\n"
                                 "@" + str(index) + "\n"
                                 "D=A\n" +
                                 "@" + segment + "\n"
                                 "D=M+D\n"
                                 "@SP\n"
                                 "A=M\n"
                                 "M=D\n"
                                 "A=A-1\n"
                                 "D=M\n"
                                 "A=A+1\n"
                                 "A=M\n"
                                 "M=D\n"
                                 "@SP\n"
                                 "M=M-1\n\n")

    def write_push_pop(self, command: str, segment: str, index: int) -> None:
        """Writes assembly code that is the translation of the given
        command, where command is either C_PUSH or C_POP.

        Args:
            command (str): "C_PUSH" or "C_POP".
            segment (str): the memory segment to operate on.
            index (int): the index in the memory segment.
        """
        # Your code goes here!
        # Note: each reference to "static i" appearing in the file Xxx.vm should
        # be translated to the assembly symbol "Xxx.i". In the subsequent
        # assembly process, the Hack assembler will allocate these symbolic
        # variables to the RAM, starting at address 16.
        segment_call_in_assembly = SEGMENTS.get(segment)
        if segment_call_in_assembly is None:
            raise ValueError(f"{segment} is Invalid")
        if segment == "static":
            segment_call_in_assembly = self.current_file + "." + str(index)
        self.output_stream.write("//write_push_pop\n")

        if command == "push":
            if segment == "constant":
                self.write_push_constant(index)
            elif segment == "pointer":
                self.output_stream.write("//push pointer" + str(index) + "\n")
                if index == 0:
                    self.write_push_segment_pointer("THIS")
                elif index == 1:
                    self.write_push_segment_pointer("THAT")
            elif segment == "temp":
                self.write_push_temp(index)
            elif segment == "static":
                self.write_push_static(segment_call_in_assembly)
            else:
                self.write_push(segment_call_in_assembly, index)

        elif command == "pop":
            if segment == "temp":
                self.write_pop_temp(index)
            elif segment == "pointer":
                self.write_pop_pointer(index)
            elif segment == "static":
                self.write_pop_static(segment_call_in_assembly)
            else:
                self.write_pop(segment_call_in_assembly, index)

    def write_label(self, label: str) -> None:
        """Writes assembly code that affects the label command.

        Args:
            label (str): the label to write.
        """
        # Creates a unique label name using the current file and provided label
        self.output_stream.write(f"// label {label}\n")
        self.output_stream.write("(" + label + ")\n")

    def write_goto(self, label: str) -> None:
        """Writes assembly code that affects the goto command.

        Args:
            label (str): the label to go to.
        """
        # Unconditionally jumps to the specified label
        self.output_stream.write(f"// goto {label}\n")
        self.output_stream.write("@" + label + "\n")
        self.output_stream.write("0;JMP\n")

    def write_if(self, label: str) -> None:
        """Writes assembly code that affects the if-goto command.

        Args:
            label (str): the label to go to if the top stack value is not zero.
        """
        # Pops the top value from the stack and jumps to the label if the value is not zero
        self.output_stream.write(f"// if-goto {label}\n")
        self.output_stream.write("@SP\n")
        self.output_stream.write("AM=M-1\n")
        self.output_stream.write("D=M\n")
        self.output_stream.write("@" + label + "\n")
        self.output_stream.write("D;JNE\n")

    def write_function(self, function_name: str, n_vars: int) -> None:
        """Writes assembly code that affects the function command.
        The handling of each "function Xxx.foo" command within the file Xxx.vm
        generates and injects a symbol "Xxx.foo" into the assembly code stream,
        that labels the entry-point to the function's code.
        In the subsequent assembly process, the assembler translates this
        symbol into the physical address where the function code starts.

        Args:
            function_name (str): the name of the function.
            n_vars (int): the number of local variables of the function.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        # The pseudo-code of "function function_name n_vars" is:
        # (function_name)       // injects a function entry label into the code
        # repeat n_vars times:  // n_vars = number of local variables
        #   push constant 0     // initializes the local variables to 0
        self.output_stream.write("(" + function_name + ")\n")
        self.output_stream.write("//lets make way for variables\n")
        for i in range(n_vars):
            self.write_push_constant(0)

    def write_call(self, function_name: str, n_args: int) -> None:
        """Writes assembly code that affects the call command.
        Let "Xxx.foo" be a function within the file Xxx.vm.
        The handling of each "call" command within Xxx.foo's code generates and
        injects a symbol "Xxx.foo$ret.i" into the assembly code stream, where
        "i" is a running integer (one such symbol is generated for each "call"
        command within "Xxx.foo").
        This symbol is used to mark the return address within the caller's
        code. In the subsequent assembly process, the assembler translates this
        symbol into the physical memory address of the command immediately
        following the "call" command.

        Args:
            function_name (str): the name of the function to call.
            n_args (int): the number of arguments of the function.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        # The pseudo-code of "call function_name n_args" is:
        # push return_address   // generates a label and pushes it to the stack
        # push LCL              // saves LCL of the caller
        # push ARG              // saves ARG of the caller
        # push THIS             // saves THIS of the caller
        # push THAT             // saves THAT of the caller
        # ARG = SP-5-n_args     // repositions ARG
        # LCL = SP              // repositions LCL
        # goto function_name    // transfers control to the callee
        # (return_address)      // injects the return address label into the code
        if self.funcount.get(function_name):
            self.funcount[function_name] += 1
        else:
            self.funcount[function_name] = 1

        return_address = (function_name + "." +
                          str(self.funcount.get(function_name)))

        self.output_stream.write("//*****call " + function_name + " *****\n")
        self.output_stream.write("//pushing the return address\n")
        self.write_push_constant(return_address)
        self.write_push_segment_pointer("LCL")
        self.write_push_segment_pointer("ARG")
        self.write_push_segment_pointer("THIS")
        self.write_push_segment_pointer("THAT")

        self.output_stream.write("//ARG = SP-5-n_args - repositions ARG\n"
                                 "@" + str(5 + n_args) + "\n"
                                 "D=A\n"
                                 "@SP\n"
                                 "D=M-D\n"
                                 "@ARG\n"
                                 "M=D\n\n")

        self.output_stream.write("//LCL = SP - repositions LCL\n"
                                 "@SP\n"
                                 "D=M\n"
                                 "@LCL\n"
                                 "M=D\n")
        self.write_goto(function_name)
        self.output_stream.write("(" + return_address + ")\n")

    def write_return(self) -> None:
        """Writes assembly code that affects the return command."""
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        # The pseudo-code of "return" is:
        # frame = LCL                   // frame is a temporary variable
        # return_address = *(frame-5)   // puts the return address in a temp var
        # *ARG = pop()                  // repositions the return value for the caller -
        # pushes the return value to what will be the top of the stack
        # SP = ARG + 1                  // repositions SP for the caller
        # THAT = *(frame-1)             // restores THAT for the caller
        # THIS = *(frame-2)             // restores THIS for the caller
        # ARG = *(frame-3)              // restores ARG for the caller
        # LCL = *(frame-4)              // restores LCL for the caller
        # goto return_address           // go to the return address
        self.output_stream.write("//frame = LCL; PUSHING LCL to RAM[13]\n")
        self.output_stream.write("@LCL\n"
                                 "D=M\n"
                                 "@13\n"
                                 "M=D\n\n")

        # now lets push the return address to the top of the stack
        self.output_stream.write("\n//return_address = *(frame-5); puts the return address in RAM[14]\n"
                                 "@LCL\n"
                                 "D=M\n"
                                 "@5\n"
                                 "A=D-A\n"
                                 "D=M\n"
                                 "@14\n"
                                 "M=D\n"
                                 "@SP\n\n")

        self.output_stream.write("//*ARG = pop(); repositions the return value for the caller\n"
                                 "//segment the top value of the stack.\n"                                 
                                 "@SP\n"
                                 "A=M-1\n"
                                 "D=M\n"
                                 "@ARG\n"
                                 "A=M\n"
                                 "M=D\n"
                                 "@SP\n"
                                 "M=M-1\n\n")

        self.output_stream.write("//SP = ARG + 1; repositions SP for the caller\n"
                                 "//- moves it passed the return value we just pushed.\n"
                                 "@ARG\n"
                                 "D=M\n"
                                 "@SP\n"
                                 "M=D+1\n\n")

        self.output_stream.write("//lets reset all the segments now\n"
                                 "//THAT = *(frame-1); restores THAT for the caller\n"
                                 "@13\n"
                                 "A=M-1\n"
                                 "D=M\n"
                                 "@THAT\n"
                                 "M=D\n\n"

                                 "//THIS = *(frame-2); restores THIS for the caller\n"
                                 "@13\n"
                                 "D=M\n"
                                 "@2\n"
                                 "A=D-A\n"
                                 "D=M\n"
                                 "@THIS\n"
                                 "M=D\n\n"

                                 "//ARG = *(frame-3); restores ARG for the caller\n"
                                 "@13\n"
                                 "D=M\n"
                                 "@3\n"
                                 "A=D-A\n"
                                 "D=M\n"
                                 "@ARG\n"
                                 "M=D\n\n"

                                 "//LCL = *(frame-4); restores LCL for the caller\n"
                                 "@13\n"
                                 "D=M\n"
                                 "@4\n"
                                 "A=D-A\n"
                                 "D=M\n"
                                 "@LCL\n"
                                 "M=D\n\n")

        self.output_stream.write("//goto return_address\n"
                                 "@14\n"
                                 "A=M\n"
                                 "0;JMP\n\n")