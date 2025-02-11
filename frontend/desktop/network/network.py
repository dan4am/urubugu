import socket
import httpx


# class Network:
#     def __init__(self):
#         self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.server = "192.168.1.64"
#         self.port = 5555
#         self.addr = (self.server, self.port)
#         self.player_number = self.connect()
#         # print(self.pos)
#
#     def connect(self):
#         try:
#             self.client.connect(self.addr)
#             return self.client.recv(2048).decode()
#         except:
#             pass
#
#     def send(self, data):
#         try:
#             self.client.send(str.encode(data))
#             return self.client.recv(2048).decode()
#         except socket.error as e:
#             print(e)
#


class Network:
    def __init__(self):
        self.server_url = "http://192.168.1.64:8000"  # FastAPI server URL
        self.client = httpx.Client()
        self.player_number = self.connect()

    def connect(self):
        """
        Registers the player with the server and retrieves the player ID.
        """
        try:
            response = self.client.post(f"{self.server_url}/game/join", json={"player_id": None})
            if response.status_code == 200:
                return response.json().get("player_id")
            else:
                print(f"Error connecting to server: {response.json()}")
        except httpx.RequestError as e:
            print(f"Request failed: {e}")
        return None

    def send(self, endpoint: str, data: dict):
        """
        Sends data to the specified FastAPI endpoint.
        """
        try:
            response = self.client.post(f"{self.server_url}{endpoint}", json=data)
            return response.json()
        except httpx.RequestError as e:
            print(f"Error sending data: {e}")
            return None



def main():
  pass

if __name__ =="__main__":

    main()