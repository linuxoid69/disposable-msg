from flask import Flask, render_template, request,session
from hashlib import md5
from lib import libgen

genlib = libgen.Gen()



app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    idsession = genlib.gen_idsession() + '-' + genlib.gen_idsession()
    passwd = genlib.gen_idsession()
    if request.method == 'POST':
       if (request.form['message']):
          genlib.write_message(passwd, idsession, request.form['message'])

       return render_template('main.html', link='%s?idsession=%s&passwd=%s' % (request.base_url, idsession, passwd))

    # if (request.args.get('idsession', '') and  request.args.get('passwd', '')):
    #     ids = request.args.get('idsession', '')
    #     pss = request.args.get('passwd', '')
    #     message = 'test'
    #     return render_template('main.html', message=message)
    return render_template('main.html')




if __name__ == '__main__':
    app.run(debug=True)
