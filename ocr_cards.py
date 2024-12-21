#!/usr/bin/env python3
"""
Name: AI OCR Card Reader
Description: Performs OCR over card data types.
Author: bshakhruz
"""
import ollama
MODEL_NAME = "llama3.2-vision:11b" #INFO: specify VISION model name


if __name__=="__main__":

    response = ollama.chat(model=MODEL_NAME, messages=[{
        "role": "system",
        "content": """You are OCR card reader. You can read cards and extract       information from it.
        
1.**Task**:
- read the card.
- perform OCR on the card.
- use tools to enhance quality of the card.
- extract information from the card.
- filter out the information.
- orginize as key value pairs
- match with input fields
- write code to autofill fields with extracted information.

2.**Toolkits**:
- OpenCV
- Tesseract
- Pytesseract
- PIL"""
    },
    {
        "role": "user",
        "content": "Follow the task and extract information from the card.",
        "images": list() #INFO: pass image path as an array of images
    }], stream=True)

    for chunk in response:
        print(chunk['content']['message'], end="", flush=True)   