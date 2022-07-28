from Core.ConnectionHandler import Server

print("""
      
██╗   ██╗██████╗  ██████╗ 
██║   ██║╚════██╗██╔═████╗
██║   ██║ █████╔╝██║██╔██║
╚██╗ ██╔╝ ╚═══██╗████╔╝██║
 ╚████╔╝ ██████╔╝╚██████╔╝
  ╚═══╝  ╚═════╝  ╚═════╝ 
                          
   by SaVok.
                   
""")

server = Server('0.0.0.0', 9339) #Binding
server.start() #Starting