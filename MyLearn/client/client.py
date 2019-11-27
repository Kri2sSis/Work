import socket
import time


class BaseError(Exception):
    '''    Базовая ошибка   '''

class ClientError(BaseError):
    '''    Ошибка клиента    '''

class ServerError(BaseError):
    '''    Ошибка сервера   '''

class PakegError(BaseError):
    '''     Пропажа пакетов     '''


class Client:
    def __init__(self, host, port, timeout = None ):
        self.host = host
        self.port = port
        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError("Error create connection", err)

    def _read(self):
        data = b""

        while not data.endswith(b'\n\n'):
            try:
                data += self.connection.recv(1024)
            except socket.error as err:
                raise ServerError("Error create connection", err)

        data_decode = data.decode()
        status, payload = data_decode.split('\n', 1)
        payload = payload.strip()

        if status == "error":
            raise PakegError(payload)

        return payload

    def put(self, key, value, timestamp = None):
        timestamp = timestamp or int(time.time())
        try:
            self.connection.sendall(
                f"put {key} {value} {timestamp}\n".encode()
            )
        except socket.error as err:
            raise ServerError("error send data", err)

        self._read()

    def get(self, key):
        try:
            self.connection.sendall(
                f"get {key}\n".encode()
            )
        except socket.error as err:
            raise ServerError("error send data", err)

        payload = self._read()

        data = {}
        if payload == "":
            return data

        for row in payload.split("\n"):
            key, value, timestamp = row.split()
            if key not in data:
                data[key] = []
            data[key].append((int(timestamp), float(value)))

        return data


    def close(self):
        try:
            self.connection.close()
        except socket.error as err:
            raise ServerError("error close connection", err)


if __name__ == "__main__":
    client = Client("127.0.0.1", 8888, timeout=5)
    client.put("test", 0.5, timestamp=1)
    client.put("test", 2.0, timestamp=2)
    client.put("test", 0.5, timestamp=3)
    client.put("load", 3, timestamp=4)
    client.put("load", 4, timestamp=5)
    print(client.get("*"))

    client.close()