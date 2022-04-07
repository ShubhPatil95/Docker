'''
URL Format 
Addition: http://localhost:8000/addition
Substraction: http://localhost:8000/substraction
'''

from flask import Flask
import json

def get_params():
	with open("inputs.json") as file:
		config=json.load(file)
	a=(config["a"])
	b=(config["b"])
	return a,b

app=Flask(__name__)

@app.route('/substraction')
def Substraction():      
    a,b=get_params()
    c=int(a)-int(b)
    with open("substraction.txt","w") as file:
        a,b=get_params()
        f = str(a)+","+str(b)+"Substraction"
        file.write(f)
    return f"Substraction is {c}"

@app.route('/addition')
def Addition():
    a,b=get_params()
    c=int(a)+int(b)
    with open("addition.txt","w") as file:
        a,b=get_params()
        f = str(a)+","+str(b)+"Addtion"
        file.write(f)
    return f"Addition is {c}"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)

    
