import socket, sys, os

def main():
    ls = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    port = int(sys.argv[1])
    ls.bind(('', port))
    ls.listen(1)
    (conn, addr) = ls.accept()
    while 1:
        l = raw_input()
        conn.send(l)

if __name__ == '__main__':
    main()
