#  Copyright (c) 2016-2017 Rocky Bernstein
"""
spark grammar differences over Python 3.1 for Python 3.0.
"""
from __future__ import print_function

from uncompyle6.parser import PythonParserSingle
from uncompyle6.parsers.parse31 import Python31Parser

class Python30Parser(Python31Parser):

    def p_30(self, args):
        """

        # FIXME: combine with parse3.2
        whileTruestmt     ::= SETUP_LOOP l_stmts_opt JUMP_BACK
                              COME_FROM_LOOP
        whileTruestmt     ::= SETUP_LOOP returns
                              COME_FROM_LOOP

        # In many ways Python 3.0 code generation is more like Python 2.6 than
        # it is 2.7 or 3.1. So we have a number of 2.6ish (and before) rules below
        # Specifically POP_TOP is more prevelant since there is no POP_JUMP_IF_...
        # instructions

        _ifstmts_jump  ::= c_stmts_opt JUMP_FORWARD _come_froms POP_TOP COME_FROM

        # Used to keep index order the same in semantic actions
        jb_pop_top     ::= JUMP_BACK POP_TOP

        while1stmt ::= SETUP_LOOP l_stmts COME_FROM_LOOP

        else_suitel ::= l_stmts COME_FROM_LOOP JUMP_BACK

        ifelsestmtl ::= testexpr c_stmts_opt jb_pop_top else_suitel

        withasstmt    ::= expr setupwithas store suite_stmts_opt
                          POP_BLOCK LOAD_CONST COME_FROM_FINALLY
                          LOAD_FAST DELETE_FAST WITH_CLEANUP END_FINALLY
        setupwithas   ::= DUP_TOP LOAD_ATTR STORE_FAST LOAD_ATTR CALL_FUNCTION_0 setup_finally
        setup_finally ::= STORE_FAST SETUP_FINALLY LOAD_FAST DELETE_FAST

        # Need to keep LOAD_FAST as index 1
        set_comp_func_header ::=  BUILD_SET_0 DUP_TOP STORE_FAST
        set_comp_func ::= set_comp_func_header
                          LOAD_FAST FOR_ITER store comp_iter
                          JUMP_BACK POP_TOP JUMP_BACK RETURN_VALUE RETURN_LAST

        list_comp_header ::=  BUILD_LIST_0 DUP_TOP STORE_FAST
        list_comp      ::= list_comp_header
                           LOAD_FAST FOR_ITER store comp_iter
                           JUMP_BACK


        comp_if       ::= expr jmp_false comp_iter
        comp_iter     ::= expr expr SET_ADD
        comp_iter     ::= expr expr LIST_APPEND

        jump_forward_else ::= JUMP_FORWARD POP_TOP
        jump_absolute_else ::= JUMP_ABSOLUTE POP_TOP

        # In many ways 3.0 is like 2.6. The below rules in fact are the same or similar.

        jmp_true       ::= JUMP_IF_TRUE POP_TOP
        jmp_false      ::= JUMP_IF_FALSE POP_TOP
        for_block      ::= l_stmts_opt _come_froms POP_TOP JUMP_BACK
        except_handler ::= JUMP_FORWARD COME_FROM_EXCEPT except_stmts
                           POP_TOP END_FINALLY come_froms
        return_if_stmt ::= ret_expr RETURN_END_IF POP_TOP
        and            ::= expr JUMP_IF_FALSE POP_TOP expr COME_FROM
        whilestmt      ::= SETUP_LOOP testexpr l_stmts_opt
                           JUMP_BACK POP_TOP POP_BLOCK COME_FROM_LOOP
        """

    def customize_grammar_rules(self, tokens, customize):
        super(Python30Parser, self).customize_grammar_rules(tokens, customize)
        return
    pass

class Python30ParserSingle(Python30Parser, PythonParserSingle):
    pass
