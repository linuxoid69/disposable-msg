from flask import Flask, render_template, request,session
import uuid
from lib import libgen
from hashlib import md5

genlib = libgen.Gen()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    idsession = uuid.uuid4()
    pw = md5(str(idsession))
    passwd = pw.hexdigest()
    if request.method == 'POST':
       if (request.form['message']):
          genlib.write_message(passwd, idsession, request.form['message'])
       return render_template('form.html', link='%s?idsession=%s&passwd=%s' % (request.base_url, idsession, passwd))

    if (request.args.get('idsession', '') and  request.args.get('passwd', '')):
        ids = request.args.get('idsession', '')
        pss = request.args.get('passwd', '')
        message = genlib.read_message(pss, ids)
        if message == None:
            return render_template('page404.html')
        genlib.delete_message(pss, ids)
        return render_template('form.html', message=message)
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True,host='10.5.5.10', port=8080)
