import http.server
import socketserver


def serve_results():
    port = 6677

    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print("Open http://localhost:6677/reports/ on your browser to see results" + str(port))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            httpd.server_close()


if __name__ == '__main__':
    serve_results()
