'''
URL Format 
Variable: http://localhost:8000/env_variable
'''

from flask import Flask
import json
import os

app=Flask(__name__)

@app.route('/env_variable')
def env_variable():
    Read_from_Config = os.getenv("Read_from_Config")
    Read_from_Config_text = os.getenv("Read_from_Config_text")
    Read_harcoded = os.getenv("Read_harcoded")
    Read_hardcoded_text =os.getenv("Read_hardcoded_text")
    return f"Read_from_Config: {Read_from_Config} <br/> Read_from_Config_text: {Read_from_Config_text}<br/> Read_harcoded: {Read_harcoded} <br/> Read_hardcoded_text:{Read_hardcoded_text}"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)

    
