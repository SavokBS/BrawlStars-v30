from ByteStream.ByteStream import ByteStream


class OwnHomeData(ByteStream):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.id = 24101
        self.version = 1

    def encode(self):
        #LogicDailyData
        self.writeVInt(0) #current time and day
        self.writeVInt(0) #time remaining for next day
        self.writeVInt(0) #trophies
        self.writeVInt(0) #highest trophies
        self.writeVInt(0) #daily highest trophies
        self.writeVInt(1) #trophy road collected rewards
        self.writeVInt(0) #exp 
        self.writeDataReference(28, 0) #avatar
        self.writeDataReference(43, 0) #color name

        self.writeVInt(0) #played gamemodes

        self.writeVInt(0) #selected skins

        self.writeVInt(0) #unlocked skins

        self.writeVInt(0) #???

        self.writeVInt(0) #leaderboard region
        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0) #sub_3E2204
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(False) #sub_5F6754


        self.writeBoolean(False) #sub_5F6754

        self.writeBoolean(False)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(2) 
        self.writeVInt(0) #name cost
        self.writeVInt(0) #name timer

        self.writeVInt(0) #shop

        self.writeVInt(0) #sub_7631C

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0) #Array

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeDataReference(16, 0)
        self.writeString("RU")
        self.writeString("")

        self.writeVInt(0) #sub_1D13B8

        self.writeVInt(0) #sub_501D58

        self.writeVInt(0) #brawl pass sub_53CF8C

        self.writeVInt(0) #proleagueseasondata sub_24E284

        self.writeBoolean(True) #Quests sub_2EB594
        self.writeVInt(0)

        self.writeBoolean(True) #emotes&icons
        self.writeVInt(0)

        #LogicConfData

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0) #sub_124960

        self.writeVInt(0) #sub_1540BC

        self.writeVInt(0) #sub_1540BC

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(True)

        self.writeVInt(0) #sub_41100C
 
        self.writeVInt(1) #sub_1D13B8
        self.writeInt(1)
        self.writeInt(41000000)

        self.writeVInt(0) #sub_F3B8C

        self.writeVInt(0) #sub_5BA8B8

        #...

        self.writeLong(0, 1)
        self.writeVInt(0)

        self.writeVInt(0)

        self.writeBoolean(False)

        self.writeVInt(0)
        self.writeVInt(0)

        for i in range(3):
            self.writeVInt(0)
            self.writeVInt(1)
        
        self.writeString("SaVok")
        self.writeVInt(1)

        self.writeInt(0)

        self.writeVInt(8)

        self.writeVInt(1)
        self.writeDataReference(23, 0)

        self.writeVInt(1)
        self.writeDataReference(16, 0)

        self.writeVInt(1)
        self.writeDataReference(16, 0)

        self.writeVInt(1)
        self.writeDataReference(16, 0)

        self.writeVInt(0)

        self.writeVInt(1)
        self.writeDataReference(16, 0)
        
        self.writeVInt(1)
        self.writeDataReference(16, 0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(2)


        self.writeVInt(0)





        
