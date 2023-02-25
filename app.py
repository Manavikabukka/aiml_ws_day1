from flask import Flask, request, jsonify

app=Flask(__name__) 
#activating flask
#get and post are two methods which can be used 

@app.route('/api/test', methods={'GET','POST'})
def mytestfunction():
    if request.method == 'GET':
        return jsonify("hi am manavika")
    else:
        input_json = request.json
        X=input_json['X']
        Y=input_json['Y']
        output = {
            "function":"message",
            "result": X+Y
        }
        return jsonify(output)
    
if __name__ =='__main__':
    app.run('0.0.0.0',port=8423)
#port=8,batch=4,serial=23
