"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing
import JackTokenizer


# Harel here - I didn't know how to write "tab" in python so I asked GPT,
# & he gave me the idea to write a function that write with indentation
# while keeping track of the indentations

# Conventions:
# Every method leaves the current token as the first one out of the section
# that the method dealt with

class CompilationEngine:
    """Gets input from a JackTokenizer and emits its parsed structure into an
    output stream.
    """

    def __init__(self, input_stream: JackTokenizer, output_stream) -> None:
        """
        Creates a new compilation engine with the given input and output. The
        next routine called must be compileClass()
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        """
        # Your code goes here!
        # Note that you can write to output_stream like so:
        # output_stream.write("Hello world! \n")
        self.tokenizer = input_stream
        self.output_stream = output_stream
        self.indentation = 0

    def indent(self) -> None:
        self.indentation += 1

    def unindent(self) -> None:
        self.indentation -= 1

    def write_and_indent(self, stringa: str) -> None:
        self.output_stream.write((self.indentation * "  ") + stringa + "\n")

    def write_keyword(self):
        # prints to the output file if it's a keyword because
        # the tokenizer keyword method returns the keyword in uppercase
        self.write_and_indent("<keyword> " + self.tokenizer.keyword().lower() + " </keyword>")

    def write_symbol(self):
        # prints to the output file if it's a symbol.
        # Note that in xml the characters '<', '>', &' are represented weirdly,
        # like so:
        replacements = {'<': '&lt;', '>': '&gt;', '&': '&amp;'}
        symbol = self.tokenizer.symbol()
        if symbol in replacements:
            symbol = replacements.get(symbol)
        self.write_and_indent("<symbol> " + symbol + " </symbol>")

    def write_identifier(self):
        # prints to the output file if it's a keyword because
        # the tokenizer keyword method returns the keyword in uppercase
        self.write_and_indent("<identifier> " + self.tokenizer.identifier() + " </identifier>")

    def write_int_const(self):
        # Prints an integer constant
        self.write_and_indent("<integerConstant> " + self.tokenizer.current_token + " </integerConstant>")

    def write_string_const(self):
        # Prints an integer constant
        self.write_and_indent("<stringConstant> " + self.tokenizer.current_token[1 : -1] + " </stringConstant>")

    def compile_class(self) -> None:
        """Compiles a complete class."""
        # Your code goes here!
        self.write_and_indent("<class>")
        self.indent()
        self.write_keyword()        # 'class'
        self.tokenizer.advance()
        self.write_identifier()     # For instance: 'square'
        self.tokenizer.advance()
        self.write_symbol()         # '{'
        self.tokenizer.advance()
        while self.tokenizer.token_type() != "SYMBOL":  # Meaning it's not an '}' that ends the class
            if self.tokenizer.keyword() == "FIELD" or self.tokenizer.keyword() == "STATIC":
                self.compile_class_var_dec()
            elif self.tokenizer.current_token in "method function constructor":
                self.compile_subroutine()
        self.write_symbol()        # '}'
        self.unindent()
        self.write_and_indent("</class>")

    def compile_class_var_dec(self) -> None:
        """Compiles a static declaration or a field declaration."""
        self.write_and_indent("<classVarDec>")
        self.indent()
        self.write_keyword()            # field
        self.tokenizer.advance()
        if self.tokenizer.token_type() == "KEYWORD":
            self.write_keyword()        # int
        else:
            self.write_identifier()     # Square
        self.tokenizer.advance()

        reached_end_of_line = False
        while not reached_end_of_line:
            self.write_identifier()     # x
            self.tokenizer.advance()
            self.write_symbol()         # ',' or ';'
            if self.tokenizer.symbol() == ";":
                reached_end_of_line = True
            self.tokenizer.advance()
            # We want to leave the marker on the next token for the next function called

        self.unindent()
        self.write_and_indent("</classVarDec>")

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        You can assume that classes with constructors have at least one field,
        you will understand why this is necessary in project 11.
        """
        self.write_and_indent("<subroutineDec>")
        self.indent()

        self.write_keyword()           # For instance: constructor
        self.tokenizer.advance()
        if self.tokenizer.token_type() == "KEYWORD":
            self.write_keyword()       # int
        else:
            self.write_identifier()    # square
        self.tokenizer.advance()
        self.write_identifier()        # new
        self.tokenizer.advance()
        self.write_symbol()            # (
        self.tokenizer.advance()

        self.compile_parameter_list()  # int Ax, int Ay

        self.write_symbol()            # )

        self.write_and_indent("<subroutineBody>")
        self.indent()
        self.tokenizer.advance()
        self.write_symbol()           # '{'
        self.tokenizer.advance()

        while self.tokenizer.current_token != "}":  # Meaning the subroutine ain't over

            if self.tokenizer.keyword() == "VAR":
                self.compile_var_dec()

            else:
                self.compile_statements()

        self.write_symbol()  # '}'
        self.unindent()
        self.write_and_indent("</subroutineBody>")
        self.unindent()
        self.write_and_indent("</subroutineDec>")
        self.tokenizer.advance()

    def compile_parameter_list(self) -> None:
        """Compiles a (possibly empty) parameter list, not including the 
        enclosing "()".
        """
        self.write_and_indent("<parameterList>")
        self.indent()
        while self.tokenizer.current_token != ")":
        # This loop runs until we reach an ')'

            if self.tokenizer.token_type() == "KEYWORD":
                self.write_keyword()     # int
            elif self.tokenizer.token_type() == "IDENTIFIER":
                self.write_identifier()  # Square

            self.tokenizer.advance()
            self.write_identifier()      # size
            self.tokenizer.advance()
            if self.tokenizer.current_token == ")":
                self.unindent()
                self.write_and_indent("</parameterList>")
                return
            self.write_symbol()          # ',' or ')'
            self.tokenizer.advance()
        self.unindent()
        self.write_and_indent("</parameterList>")

    def compile_var_dec(self) -> None:
        """Compiles a var declaration."""
        self.write_and_indent("<varDec>")
        self.indent()
        self.write_keyword()         # var
        self.tokenizer.advance()

        if self.tokenizer.token_type() == "IDENTIFIER":
            self.write_identifier()  # SquareGame

        elif self.tokenizer.token_type() == "KEYWORD":
            self.write_keyword()     # int
        self.tokenizer.advance()

        reached_end_of_line = False
        while not reached_end_of_line:
            if self.tokenizer.token_type() == "IDENTIFIER":
                self.write_identifier()  # x
                self.tokenizer.advance()
                self.write_symbol()      # , or ;
            if self.tokenizer.symbol() == ";":
                reached_end_of_line = True
            self.tokenizer.advance()
            # We want to leave the marker on the next token for the next function called

        self.unindent()
        self.write_and_indent("</varDec>")

    def compile_statements(self) -> None:
        """Compiles a sequence of statements, not including the enclosing 
        "{}".
        """
        STATEMENTS = {"LET": self.compile_let,
                      "DO": self.compile_do,
                      "IF": self.compile_if,
                      "WHILE": self.compile_while,
                      "RETURN": self.compile_return}

        relevant_function = STATEMENTS.get(self.tokenizer.keyword())

        self.write_and_indent("<statements>")
        self.indent()

        while self.tokenizer.token_type() != "SYMBOL":
            relevant_function()
                # We want to leave the marker on the '}' for compile_subroutine to handle
            if self.tokenizer.token_type() != "SYMBOL":
                relevant_function = STATEMENTS.get(self.tokenizer.keyword())

        self.unindent()
        self.write_and_indent("</statements>")

    def compile_do(self) -> None:
        """Compiles a do statement."""
        self.write_and_indent("<doStatement>")
        self.indent()
        self.write_keyword()     # do
        self.tokenizer.advance()

        self.write_identifier()  # For instance: 'Alloc'
        self.tokenizer.advance()
        self.write_symbol()      # '.' ot '('
        if self.tokenizer.symbol() == "(":
            self.tokenizer.advance()
            self.compile_expression_list()
        elif self.tokenizer.symbol() == ".":
            self.tokenizer.advance()
            self.write_identifier()
            self.tokenizer.advance()
            self.write_symbol()      # (
            self.tokenizer.advance()
            self.compile_expression_list()   # a, b, c

        self.write_symbol()         # ')'
        self.tokenizer.advance()
        self.write_symbol()         # ';'
        self.tokenizer.advance()

        self.unindent()
        self.write_and_indent("</doStatement>")

    def compile_let(self) -> None:
        """Compiles a let statement."""
        self.write_and_indent("<letStatement>")
        self.indent()

        self.write_keyword()             # let
        self.tokenizer.advance()
        self.write_identifier()          # x
        self.tokenizer.advance()
        if self.tokenizer.current_token == "[":
            self.write_symbol()          # [
            self.tokenizer.advance()
            self.compile_expression()    # b + 1
            self.write_symbol()          # ]
            self.tokenizer.advance()
        self.write_symbol()              # =
        self.tokenizer.advance()

        self.compile_expression()

        self.write_symbol()              # ;
        self.unindent()
        self.write_and_indent("</letStatement>")
        self.tokenizer.advance()

    def compile_while(self) -> None:
        """Compiles a while statement."""
        self.write_and_indent("<whileStatement>")
        self.indent()

        self.write_keyword()       # 'while'
        self.tokenizer.advance()
        self.write_symbol()        # '('
        self.tokenizer.advance()

        self.compile_expression()  # 'x = true'

        self.write_symbol()        # ')'
        self.tokenizer.advance()
        self.write_symbol()        # '{'
        self.tokenizer.advance()

        self.compile_statements()  # do so & so...

        self.write_symbol()        # '}'
        self.unindent()
        self.write_and_indent("</whileStatement>")
        self.tokenizer.advance()

    def compile_return(self) -> None:
        """Compiles a return statement."""
        self.write_and_indent("<returnStatement>")
        self.indent()
        self.write_keyword()       # 'return'
        self.tokenizer.advance()

        if self.tokenizer.current_token != ";":
            # Checking it's not returning void with an empty return
            self.compile_expression()

        self.write_symbol()        # ';'
        self.unindent()
        self.write_and_indent("</returnStatement>")
        self.tokenizer.advance()

    def compile_if(self) -> None:
        """Compiles an if statement, possibly with a trailing else clause."""
        self.write_and_indent("<ifStatement>")
        self.indent()

        self.write_keyword()           # 'if'
        self.tokenizer.advance()
        self.write_symbol()            # '('
        self.tokenizer.advance()

        self.compile_expression()      # 'x = true'

        self.write_symbol()            # ')'
        self.tokenizer.advance()
        self.write_symbol()            # '{'
        self.tokenizer.advance()

        self.compile_statements()      # do so & so...

        self.write_symbol()            # '}'
        self.tokenizer.advance()

        if self.tokenizer.current_token == "else":
            self.write_keyword()
            self.tokenizer.advance()
            self.write_symbol()        # '{'
            self.tokenizer.advance()

            self.compile_statements()  # do so & so...

            self.write_symbol()        # '}'
            self.tokenizer.advance()
        self.unindent()
        self.write_and_indent("</ifStatement>")

    def compile_expression(self) -> None:
        """Compiles an expression."""
        self.write_and_indent("<expression>")
        self.indent()

        self.compile_term()        # 'x'
        while self.tokenizer.symbol() in ['+', '-', '*', '/', '&', '|', '<', '>', '=', '~']:
            self.write_symbol()
            self.tokenizer.advance()
            self.compile_term()

        self.unindent()
        self.write_and_indent("</expression>")

    def compile_term(self) -> None:
        """Compiles a term. 
        This routine is faced with a slight difficulty when
        trying to decide between some of the alternative parsing rules.
        Specifically, if the current token is an identifier, the routing must
        distinguish between a variable, an array entry, and a subroutine call.
        A single look-ahead token, which may be one of "[", "(", or "." suffices
        to distinguish between the three possibilities. Any other token is not
        part of this term and should not be advanced over.
        """
        self.write_and_indent("<term>")
        self.indent()
        parenthesis = 0
        if self.tokenizer.current_token == "(":
            parenthesis += 1
            self.write_symbol()                 # (((((( as many as there are
            self.tokenizer.advance()
            self.compile_expression()

        if self.tokenizer.current_token in "- ~ ^ #":
            self.write_symbol()                 # '-' or '~'
            self.tokenizer.advance()
            self.compile_term()


        FUNCTIONS = {"INT_CONST": self.write_int_const,
                     "STRING_CONST": self.write_string_const,
                     "KEYWORD": self.write_keyword}

        simple_writing = FUNCTIONS.get(self.tokenizer.token_type())
        if simple_writing:
            simple_writing()
            self.tokenizer.advance()

        if self.tokenizer.token_type() == "IDENTIFIER":
            self.write_identifier()             # 'a'
            self.tokenizer.advance()

            if self.tokenizer.current_token in "; * / + - < > = & |":
                self.unindent()
                self.write_and_indent("</term>")
                return

            if self.tokenizer.current_token in "[ ( .":
                self.write_symbol()             # '[', '(' or '.'

            if self.tokenizer.current_token == "[":
                self.tokenizer.advance()
                self.compile_expression()       # b + 1
                self.write_symbol()             # ]
                self.tokenizer.advance()

            elif self.tokenizer.current_token == "(":
                self.tokenizer.advance()
                self.compile_expression_list()   # a, b, c
                self.write_symbol()             # ')'
                self.tokenizer.advance()

            elif self.tokenizer.current_token == ".":
                self.tokenizer.advance()
                self.write_identifier()         # function_name
                self.tokenizer.advance()
                self.write_symbol()             # (
                self.tokenizer.advance()
                self.compile_expression_list()  # a, b, c
                self.write_symbol()             # )
                self.tokenizer.advance()


        while self.tokenizer.current_token == ")" and parenthesis > 0:
            parenthesis -= 1
            self.write_symbol()                 # )))))) as many as there are
            self.tokenizer.advance()
            if self.tokenizer.current_token in "; * / + - < > = & |" and parenthesis > 0:
                # Maybe there's a term at the other side of the parenthesis
                self.write_symbol()
                self.tokenizer.advance()
                self.compile_term()

        self.unindent()
        self.write_and_indent("</term>")

    def compile_expression_list(self) -> None:
        """Compiles a (possibly empty) comma-separated list of expressions."""
        self.write_and_indent("<expressionList>")
        self.indent()

        if self.tokenizer.current_token != ")":
            self.compile_expression()   # c * 2

        while self.tokenizer.current_token != ")":
            self.write_symbol()         # ','
            self.tokenizer.advance()
            self.compile_expression()   # a + 1
            # Compile expression leaves us with the next token according to our API,
            # and this token is a comma. So there's no need to advance into the symbol

        self.unindent()
        self.write_and_indent("</expressionList>")





