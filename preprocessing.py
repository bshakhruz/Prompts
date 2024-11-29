#!/usr/bin/env python3
"""
Name: AI Preprocessor
Description: Performs preprocessing over text data types.
Author: bshakhruz
"""
import ollama

def system_instruction():
    """Preprocess texts"""
    return {
    "role": "system",
    "content": f"""You are text preprocessor.\n
    **Task**\n
    - perform preprocessing on all steps over texts.\n
    - minimaze tokens and garbages\n
    """,
    #TO-DO: pass additional params
            }