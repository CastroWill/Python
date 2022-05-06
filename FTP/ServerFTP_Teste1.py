from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer  # <-
from pyftpdlib.authorizers import DummyAuthorizer


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', '.')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = ThreadedFTPServer(('192.168.50.254', 2121), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
