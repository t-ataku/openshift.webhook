#
# HOW TO RUN
# FLASK_APP=app.py python3 -m flask run --host=0.0.0.0 --port=1080
#

from flask import Flask, request, render_template
#from redis import Redis, RedisError
import os
import socket

#redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():

    visits = ":Visited:"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1080)

@app.route("/help")
def help():
    print("help")
    html = "<html><head><title>Help Page</title></head>" \
           "<body>" \
           "<h1>Index of Help</h1>" \
           "<p>" \
           "Index would be here" \
           "</body>"
    return html

@app.route("/Users/<username>")
def user(username):
    html = "<html><head><title>User Page</title></head>" \
           "<body>" \
           "<h1>Index for %s </h1>" \
           "<p>" \
           "Index would be here" \
           "</body>"  % username
    return html

@app.route("/post", methods=['POST'])
def postchekerOK():
  html = "<html><head><title>OK</title></head><body>POST method.</body></html>"
  return html

@app.route("/post", methods=["GET"])
def postcheckerNG():
    return "<html><head><title>GET method</title></head><body>GET method.  It seemed not to be OK</body></html>"

@app.route("/index.html", methods=['POST', 'GET'])
def indexPOST():
    return url_for('static', filename='index.html')

@app.route("/render/<filename>", methods=['POST', 'GET'])
def renderFile(filename):
    return render_template('index.templ',name=filename)

@app.route("/postdata", methods=['POST','GET'])
def postdata():
    if request.method == 'POST':
        return render_template('posteddata.html', name=request.form['value'])
    else:
        return "<html><head><title>Enter your name</title></head>" \
            "<body><form method=POST>" \
            "<input type=text name=value>" \
            "<input type=submit>" \
            "</form></body></html>"

@app.route("/apis/build.openshift.io/v1/namespaces/<ns>/buildconfigs/<bc>/webhooks/<id>/github", methods=['POST'])
#NS: okdsample
#BC: httpd-example2
#ID: xxx
def webhook_post(ns, bc, id):

    print("METHOD: %s\n" % request.method)
    print("HEADERS: %s\n" % request.headers)
    print("DATA: %s\n" % request.data)

    response = app.make_response('NS: {0}\r\nBC: {1}\r\nID: {2}\r\n'.format(ns, bc, id))
#    response.headers.add('myKey', 'myValue')
    print('--------------------------------------------------')
    print(response)
    print('--------------------------------------------------')
    return response

@app.route("/apis/build.openshift.io/v1/namespaces/<ns>/buildconfigs/<bc>/webhooks/<id>/github", methods=['GET'])
def webhook_get(ns, bc, id):
    response = app.make_response("<html>" \
                                 "<head><title>Input Values</title></head>" \
                                 "<body><form method=POST>" \
                                 "Namespace: <input type=string name=ns value={0}><br>" \
                                 "BuildConfig: <input type=string name=bc value={1}><br>" \
                                 "ID: <input type=string name=id value={2}><br>" \
                                 "<input type=submit>" \
                                 "</form></body>" \
                                 "</html>".format(ns, bc, id))
#    response.headers.add('myKey', 'myValue')
    print("--------------------------------------------------")
    print(response)
    print("--------------------------------------------------")
    return response
