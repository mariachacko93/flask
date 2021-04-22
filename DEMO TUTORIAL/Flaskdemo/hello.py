from flask import Flask


app=Flask(__name__)  #takes name of current module as argument

#  url bounding function
@app.route('/hello/<name>')
def hello_world (name):
    return 'hello %s!' % name

# or


# def hello_world ():
#     return 'hello world'
#     app.add_url_rule('/','hello',hello_world)

if __name__=='__main__':
    app.run(debug=True) #run 