from ByteStream.ByteStream import ByteStream
from Logic.Messaging import Messaging
from Packets.Server.LoginOk import LoginOk
from Packets.Server.OwnHomeMessage import OwnHomeData


class Login(ByteStream):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
        self.HighID = self.readInt()
        self.LowID = self.readInt()
        # self.Token = self.readString()
        # self.Major = self.readInt()
        # self.Minor = self.readInt()
        # self.Build = self.readInt()
        # self.FingerprintSHA = self.readString()
        # self.Device = self.readString()
        # self.PreferredLanguage = self.readDataReference()
        # self.PreferredDeviceLanguage = self.readString()
        # self.OSVersion = self.readString()
        # self.isAndroid = self.readBoolean()
       
    
    def process(self):
        Messaging(self.client).send(LoginOk(self.player))
        Messaging(self.client).send(OwnHomeData(self.player))
