"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing

COMMANDS_TO_STRINGS = {
    "keyword": ['class', 'constructor', 'function', 'method', 'field',
                'static', 'var', 'int', 'char', 'boolean', 'void', 'true',
                'false', 'null', 'this', 'let', 'do', 'if', 'else',
                'while', 'return'],

    "symbol": ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+',
               '-', '*', '/', '&', '|', '<', '>', '=', '~', '^', '#'],
}


class JackTokenizer:
    """Removes all comments from the input stream and breaks it
    into Jack language tokens, as specified by the Jack grammar.
    
    # Jack Language Grammar

    A Jack file is a stream of characters. If the file represents a
    valid program, it can be tokenized into a stream of valid tokens. The
    tokens may be separated by an arbitrary number of whitespace characters, 
    and comments, which are ignored. There are three possible comment formats: 
    /* comment until closing */ , /** API comment until closing */ , and 
    // comment until the lines end.

    - ‘xxx’: quotes are used for tokens that appear verbatim (‘terminals’).
    - xxx: regular typeface is used for names of language constructs 
           (‘non-terminals’).
    - (): parentheses are used for grouping of language constructs.
    - x | y: indicates that either x or y can appear.
    - x?: indicates that x appears 0 or 1 times.
    - x*: indicates that x appears 0 or more times.

    ## Lexical Elements

    The Jack language includes five types of terminal elements (tokens).

    - keyword: 'class' | 'constructor' | 'function' | 'method' | 'field' | 
               'static' | 'var' | 'int' | 'char' | 'boolean' | 'void' | 'true' |
               'false' | 'null' | 'this' | 'let' | 'do' | 'if' | 'else' | 
               'while' | 'return'
    - symbol: '{' | '}' | '(' | ')' | '[' | ']' | '.' | ',' | ';' | '+' | 
              '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' | '~' | '^' | '#'
    - integerConstant: A decimal number in the range 0-32767.
    - StringConstant: '"' A sequence of Unicode characters not including 
                      double quote or newline '"'
    - identifier: A sequence of letters, digits, and underscore ('_') not 
                  starting with a digit. You can assume keywords cannot be
                  identifiers, so 'self' cannot be an identifier, etc'.

    ## Program Structure

    A Jack program is a collection of classes, each appearing in a separate 
    file. A compilation unit is a single class. A class is a sequence of tokens 
    structured according to the following context free syntax:
    
    - class: 'class' className '{' classVarDec* subroutineDec* '}'
    - classVarDec: ('static' | 'field') type varName (',' varName)* ';'
    - type: 'int' | 'char' | 'boolean' | className
    - subroutineDec: ('constructor' | 'function' | 'method') ('void' | type) 
    - subroutineName '(' parameterList ')' subroutineBody
    - parameterList: ((type varName) (',' type varName)*)?
    - subroutineBody: '{' varDec* statements '}'
    - varDec: 'var' type varName (',' varName)* ';'
    - className: identifier
    - subroutineName: identifier
    - varName: identifier

    ## Statements

    - statements: statement*
    - statement: letStatement | ifStatement | whileStatement | doStatement | 
                 returnStatement
    - letStatement: 'let' varName ('[' expression ']')? '=' expression ';'
    - ifStatement: 'if' '(' expression ')' '{' statements '}' ('else' '{' 
                   statements '}')?
    - whileStatement: 'while' '(' 'expression' ')' '{' statements '}'
    - doStatement: 'do' subroutineCall ';'
    - returnStatement: 'return' expression? ';'

    ## Expressions
    
    - expression: term (op term)*
    - term: integerConstant | stringConstant | keywordConstant | varName | 
            varName '['expression']' | subroutineCall | '(' expression ')' | 
            unaryOp term
    - subroutineCall: subroutineName '(' expressionList ')' | (className | 
                      varName) '.' subroutineName '(' expressionList ')'
    - expressionList: (expression (',' expression)* )?
    - op: '+' | '-' | '*' | '/' | '&' | '|' | '<' | '>' | '='
    - unaryOp: '-' | '~' | '^' | '#'
    - keywordConstant: 'true' | 'false' | 'null' | 'this'
    
    Note that ^, # correspond to shiftleft and shiftright, respectively.
    """

    def __init__(self, input_stream: typing.TextIO) -> None:
        """Opens the input stream and gets ready to tokenize it.

        Args:
            input_stream (typing.TextIO): input stream.
        """
        input_lines = input_stream.read().splitlines()
        clean_lines = []
        inside_comment_block = False

        for line in input_lines:
            line = line.strip()

            # Handle block comments /* ... */
            # I allowed up to 1.5 comments in one line, to make life easier
            if "/*" in line:
                inside_comment_block = True
                second_half = line.split("/*")[1].strip()
                line = line.split("/*")[0].strip()
                # If the '*/' is in the same line - meaning the comment is over
                if "*/" in second_half:
                    line = line + ' ' + second_half.split("*/")[1].strip()
                    inside_comment_block = False
                continue

            if inside_comment_block:
                if "*/" in line:
                    line = line.split("*/")[1].strip()
                    inside_comment_block = False
                    if "/*" in line:
                    # Same here, 2 comments might end and start in the same line
                        line = line.split("/*")[0].strip()
                        inside_comment_block = True
                continue

            # Remove inline comments //
            if "//" in line:
                line = line.split("//")[0].strip()

            if line:  # Skip empty lines
                clean_lines.append(line)

        self.lines = clean_lines
        self.current_line_index = 0
        self.next_token_index = 0
        self.current_token = None
        self.advance()

    def has_more_tokens(self) -> bool:
        """Do we have more tokens in the input?

        Returns:
            bool: True if there are more tokens, False otherwise.
        """

        if self.current_line_index >= len(self.lines):
            return False

        while self.current_line_index < len(self.lines):
            # Split the current line into tokens using whitespace or symbols as delimiters
            tokens = self.tokenize_line(self.lines[self.current_line_index])

            # If we have more tokens in this line, return True
            if self.next_token_index < len(tokens):
                return True
            else:
                # Reset token index and move to the next line
                self.current_line_index += 1
                self.next_token_index = 0

        # If we've gone through all lines, return False
        return False



    def advance(self) -> None:
        """Gets the next token from the input and makes it the current token. 
        This method should be called if has_more_tokens() is true. 
        Initially there is no current token.
        """
        # Your code goes here!
        """ My idea here:
        
        """

        if not self.has_more_tokens():
            raise ValueError("No more tokens available to advance.")

            # Tokenize the current line
        tokens = self.tokenize_line(self.lines[self.current_line_index])

        # Get the current token
        self.current_token = tokens[self.next_token_index]

        # Move to the next token
        self.next_token_index += 1

    def get_next_token(self) -> str:
        """Gets the next token from the input and makes it the current token.
        This method should be called if has_more_tokens() is true.
        Initially there is no current token.
        """
        # Your code goes here!
        """ My idea here:

        """

        if not self.has_more_tokens():
            raise ValueError("No more tokens available to advance.")

            # Tokenize the current line
        tokens = self.tokenize_line(self.lines[self.current_line_index])

        # Get the current token
        return tokens[self.next_token_index]

    def tokenize_line(self, line: str):
        """Tokenizes a line into Jack language tokens (keywords, symbols, identifiers, etc.)."""

        tokens = []
        token = ""
        i = 0

        symbols = {'{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*',
                   '/', '&', '|', '<', '>', '=', '~', '^', '#'}

        while i < len(line):
            char = line[i]

            # Skip whitespace characters
            if char.isspace():
                i += 1
                continue

            # Handle symbols (single-character tokens)
            if char in symbols:
                if token:
                    tokens.append(token)
                    token = ""
                tokens.append(char)
                i += 1
                continue

            # Handle string constants (everything inside double quotes as one token)
            if char == '"':
                if token:
                    tokens.append(token)
                    token = ""
                # Find the closing quote
                end_quote = line.find('"', i + 1)
                if end_quote == -1:
                    # If no closing quote is found, append the rest of the line as the string
                    tokens.append(line[i:])
                    i = len(line)
                else:
                    # Include the string with quotes
                    tokens.append(line[i:end_quote + 1])
                    i = end_quote + 1
                continue

            # Handle identifiers and numbers (sequences of letters, digits, or underscores)
            while i < len(line) and (line[i].isalnum() or line[i] == '_'):
                token += line[i]
                i += 1

            # If we collected a token, add it to the tokens list
            if token:
                tokens.append(token)
                token = ""

        return tokens

    """
     ## Lexical Elements

    The Jack language includes five types of terminal elements (tokens).

    - keyword: 'class' | 'constructor' | 'function' | 'method' | 'field' | 
               'static' | 'var' | 'int' | 'char' | 'boolean' | 'void' | 'true' |
               'false' | 'null' | 'this' | 'let' | 'do' | 'if' | 'else' | 
               'while' | 'return'
    - symbol: '{' | '}' | '(' | ')' | '[' | ']' | '.' | ',' | ';' | '+' | 
              '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' | '~' | '^' | '#'
    - integerConstant: A decimal number in the range 0-32767.
    - StringConstant: '"' A sequence of Unicode characters not including 
                      double quote or newline '"'
    - identifier: A sequence of letters, digits, and underscore ('_') not 
                  starting with a digit. You can assume keywords cannot be
                  identifiers, so 'self' cannot be an identifier, etc'.
    """

    def token_type(self) -> str:
        """
        Returns:
            str: the type of the current token, which can be
            "KEYWORD", "SYMBOL", "IDENTIFIER", "INT_CONST", "STRING_CONST"
        """
        # Convert token to lower for keyword matching
        keywords = {'class', 'constructor', 'function', 'method', 'field',
                    'static', 'var', 'int', 'char', 'boolean', 'void',
                    'true', 'false', 'null', 'this', 'let', 'do', 'if',
                    'else', 'while', 'return'}

        if self.current_token.lower() in keywords:
            return "KEYWORD"

        symbols = {'{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*',
                   '/', '&', '|', '<', '>', '=', '~', '^', '#'}
        if self.current_token in symbols:
            return "SYMBOL"

        if self.current_token.isdigit() and 0 <= int(self.current_token) <= 32767:
            return "INT_CONST"

        if self.current_token.startswith('"') and self.current_token.endswith('"'):
            return "STRING_CONST"

        return "IDENTIFIER"




    def keyword(self) -> str:
        """
        Returns:
            str: the keyword which is the current token.
            Should be called only when token_type() is "KEYWORD".
            Can return "CLASS", "METHOD", "FUNCTION", "CONSTRUCTOR", "INT", 
            "BOOLEAN", "CHAR", "VOID", "VAR", "STATIC", "FIELD", "LET", "DO", 
            "IF", "ELSE", "WHILE", "RETURN", "TRUE", "FALSE", "NULL", "THIS"
        """
        # Your code goes here!
        if(self.token_type()=="KEYWORD"):
            return self.current_token.upper()



    def symbol(self) -> str:
        """
        Returns:
            str: the character which is the current token.
            Should be called only when token_type() is "SYMBOL".
            Recall that symbol was defined in the grammar like so:
            symbol: '{' | '}' | '(' | ')' | '[' | ']' | '.' | ',' | ';' | '+' | 
              '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' | '~' | '^' | '#'
        """
        # Your code goes here!
        if (self.token_type() == "SYMBOL"):
            return self.current_token

    def identifier(self) -> str:
        """
        Returns:
            str: the identifier which is the current token.
            Should be called only when token_type() is "IDENTIFIER".
            Recall that identifiers were defined in the grammar like so:
            identifier: A sequence of letters, digits, and underscore ('_') not 
                  starting with a digit. You can assume keywords cannot be
                  identifiers, so 'self' cannot be an identifier, etc'.
        """
        # Your code goes here!
        if (self.token_type() == "IDENTIFIER"):
            return self.current_token

    def int_val(self) -> int:
        """
        Returns:
            str: the integer value of the current token.
            Should be called only when token_type() is "INT_CONST".
            Recall that integerConstant was defined in the grammar like so:
            integerConstant: A decimal number in the range 0-32767.
        """
        # Your code goes here!
        if (self.token_type() == "INT_CONST"):
            return int(self.current_token)


    def string_val(self) -> str:
        """
        Returns:
            str: the string value of the current token, without the double 
            quotes. Should be called only when token_type() is "STRING_CONST".
            Recall that StringConstant was defined in the grammar like so:
            StringConstant: '"' A sequence of Unicode characters not including 
                      double quote or newline '"'
        """
        # Your code goes here!
        if (self.token_type() == "STRING_CONST"):
            return self.current_token[1:-1]  # Remove the first and last ("")
