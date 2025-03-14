from engine.handbook._tokens import Tokens
import string, logger

class HandbookLexer():
    def lex_raw_string(self, raw_string:str):
        logger.debug(f"|LEXER| Input: {raw_string}")
        raw_tokens = ''.join(char if char not in string.whitespace else ' ' for char in raw_string).split()
        logger.debug(f"|LEXER| Whitespace Split: {raw_tokens}")
        token_list = []
        for _t in raw_tokens:
            if Tokens.TOKENS.get(_t.upper()):
                logger.debug(f"|LEXER| TOKEN: {_t.upper(), Tokens.TOKENS.get(_t.upper())}")
                token_list.append([_t.upper(), Tokens.TOKENS.get(_t.upper())])
            else:
                logger.debug(f"|LEXER| Missing TOKEN for: {_t.upper()} trying MISC Matches")
                try:
                    logger.debug(f"|LEXER| TOKEN: {int(_t), 'INT'}")
                    token_list.append([int(_t), "INT"])
                except:
                    logger.debug(f"|LEXER| TOKEN: {_t, 'ERROR'}")
                    token_list.append([_t.upper(), "ERROR"])
        return token_list
