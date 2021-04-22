from flask import Flask


app=Flask(__name__)
# app.config['DEBUG']=True
# DEBUG=True
app.config.from_object(__name__)
# app.config.from_pyfile('config.cfg')


@app.route('/')
def index():
    return 'Helo'


if __name__=='__main__':
    app.run(debug=True)

