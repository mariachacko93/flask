from flask import Flask,redirect,url_for


app=Flask(__name__)  #takes name of current module as argument

#  url bounding function
@app.route('/admin')
def admin ():
    return 'Hello!! Admin!'

@app.route('/guest/<guest>')
def guest (guest):
    return 'Welcome!! %s as Guest !' % guest
    
@app.route('/user/<name>')
def user (name):
    if name =='admin':
        return redirect(url_for('admin'))
    elif name=='guest':
        return redirect(url_for('guest',guest=name))
    else:
        return 'welcome %s' %name


if __name__=='__main__':
    app.run(debug=True) #run 