#!/usr/bin/env python


from collector import simple_app


def test_print_hello():
    assert simple_app.print_hello()=='Hello'
