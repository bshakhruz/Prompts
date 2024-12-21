"""
name: address interpreter
description: automatically translates your addresses between EN and UZ  
"""

import ollama

def infrastructure(model:str, query_prompt, stream: bool=False):
    assert model is not None, TypeError("Specify model name.")
    return ollama.chat(model=model,
                       messages=[
                           {
                               "role": "system",
                               "content": """You are address translator between English and Uzbek languages. Rule of thumb is Uzbekistan rule is from top-down; meaning it starts from index code, state name and for English it rather is vice versa: meaning from bottom-to-top."""
                           },
                           {
                               "role": 'user',
                               "content": query_prompt,
                           }
                       ],
                       stream=stream)


if __name__=="__main__":
    pass