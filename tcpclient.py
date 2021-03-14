import socket

class TCPClient:
    """
    TCP通信を行うクライアントを表すクラス
    """

    def request(self):
        """
        サーバーへリクエストを送信する
        """

        print("=== クライアントを起動します ===")

        try:
            # socketを生成
            client_socket = socket.socket()
            client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        finally:
            pass
