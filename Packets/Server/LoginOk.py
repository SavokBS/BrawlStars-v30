from ByteStream.ByteStream import ByteStream


class LoginOk(ByteStream):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.id = 20104
        self.version = 1

    def encode(self):
        self.writeLong(0, 1) #Account
        self.writeLong(0, 1) #Home
        self.writeString("") #Token
        self.writeString("") #Facebook
        self.writeString("") #Gamecenter
        self.writeInt(30) #Major
        self.writeInt(1) #Minor
        self.writeInt(242) #Build
        self.writeString("prod") #Env
        self.writeInt(0) #???
        self.writeInt(0) #Playtime seconds
        self.writeInt(0) #Playdays count
        self.writeString("")
        self.writeString("")
        self.writeString("")
        self.writeInt(0)
        self.writeString("")
        self.writeString("RU") #Country
        self.writeString("")
        self.writeInt(1)
        self.writeString("")
        self.writeInt(0)
        self.writeInt(0)
        self.writeVInt(0)
        self.writeString("") #compressed string
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeString("")
        self.writeString("")
        self.writeString("")
        self.writeString("")
        self.writeString("")
        self.writeBoolean(False)