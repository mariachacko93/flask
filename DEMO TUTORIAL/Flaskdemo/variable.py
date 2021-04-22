from flask import Flask


app=Flask(__name__)  #takes name of current module as argument

#  url bounding function
@app.route('/blog/<int:postID>')
def blog (postID):
    return 'Hello!! your blog number is %d!' % postID


@app.route('/rev/<float:revNo>')
def revision (revNo):
    return 'Hello!! your Revision number %f!' % revNo
    
if __name__=='__main__':
    app.run(debug=True) #run 