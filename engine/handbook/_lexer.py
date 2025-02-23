from engine.handbook._tokens import Tokens
import string, logging

class HandbookLexer():
    def lex_raw_string(self, raw_string:str):
        logging.debug(f"|LEXER| Input: {raw_string}")
        raw_tokens = ''.join(char if char not in string.whitespace else ' ' for char in raw_string).split()
        logging.debug(f"|LEXER| Whitespace Split: {raw_tokens}")
        token_list = []
        for _t in raw_tokens:
            try:
                logging.debug(f"|LEXER| TOKEN: {_t.upper(), Tokens.TOKENS.get(_t.upper())}")
                token_list.append([_t.upper(), Tokens.TOKENS.get(_t.upper())])
            except:
                logging.debug(f"|LEXER| Missing TOKEN for: {_t.upper()}")
                token_list.append([_t.upper()])
        return token_list
