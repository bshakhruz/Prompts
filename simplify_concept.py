#!/usr/bin/env python3
"""
Name: Concept Simplifier
Description: Explain complex ideas into plain language, even to a kid is tangible and fun!
Dependencies: [
    ollama>=0.4.1,
              ]
Author: bshakhruz 
"""
import ollama

def Prompt_Instruction():
    """Prompt instruction."""
    return {
    "role": "system",
    "content": f"""You are concept simplifier. You explain existed ideas in simple plain language.\n\t**Task**\n- Read <|given_complex_terms|>\n- Break down them and rewrite into simple words\n- Give good examples\n- Based on contexts, make them interactive and fun.""",
    # "images": [pass as array of list all images if the model is multimodal]
    #TO-DO: pass additional params
}