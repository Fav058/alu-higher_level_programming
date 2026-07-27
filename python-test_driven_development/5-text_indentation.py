#!/usr/bin/python3
"""Module that prints text with extra newlines after ., ? and :
"""


def text_indentation(text):
    """Print text, adding two newlines after each ., ? or : character.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
