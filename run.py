import web
import boto
import boto.ec2

urls = (
    '/', 'index',
    '/ec2/connect/', 'ec2_connect'
)

class index:
    def GET(self):
        return 'AWS API'

class ec2_connect:
    def GET(self):
        conn = boto.ec2.connect_to_region("us-west-2")
        print conn

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 9080))