"""
some new techs with messaging. :upside_down: by 🌼
"""
class Messaging:
    def __init__(self, client):
        self.client = client
    
    def send(self, message):
        try:
            message.encode()
            print(f"[SERVER] <= ID: {message.id}, Length: {len(message.buffer)}")
            header = Messaging.writeHeader(message.id, len(message.buffer), message.version)
            self.client.send(header + message.buffer)
            
        except Exception as e:
            print(e)

    @staticmethod
    def writeHeader(type, length, version):
        buffer = b''
        buffer += int.to_bytes(type, 2, "big")
        buffer += int.to_bytes(length, 3, "big")
        buffer += int.to_bytes(version, 2, "big")
        return buffer

    @staticmethod
    def readHeader(buffer):
        return int.from_bytes(buffer[:2], "big"), int.from_bytes(buffer[2:5], "big"), int.from_bytes(buffer[5:], "big")