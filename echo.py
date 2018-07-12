#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        request_headers = self.headers
        content_length = request_headers.get('Content-Length')
        length = int(content_length) if content_length else 0
        payload = self.rfile.read(length)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(payload)

    do_PUT = do_POST


def main(port):
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-p", "--port", dest="port",
                      help="set port to listen on", default=8910, type=int)
    parser.usage = ("Creates an http-server that will echo out body of POST request\n"
                    "Run:\n\n"
                    "   echo")
    (options, args) = parser.parse_args()

    main(options.port)

