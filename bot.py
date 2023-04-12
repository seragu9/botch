import ch
import time
import random

class bot(ch.RoomManager):


    #ncount = 0
    def onInit(self):
        self.setNameColor("E5DE0B")
        #self.setFontColor("FFFFFF")
        self.setFontFace("Courier")
        self.setFontSize(13)
        #print(self.getUserlist())
    
    def onMessage(self, room, user, message):
        print("[{0}] {1}: {2}".format(room.name, user.name.title(), message.body))
        #print(room.getUserNames())
        print(message.getUid())
        print(message.getUser())        
        if self.user == user:
            return
        
        try:
          cmd, args = message.body.split(" ", 1)
        except:
          cmd, args = message.body, ""
          
        ran = random.uniform(0, 1)
        #print(ran)
        if cmd.lower() == ("@"+self.user.name) and ran > 0.6:
            if (user.name == "1ssirena" or user.name == "doge2023"):
                room.message("*rolleyes*")
            return
            
            if (ran > 0.9):
                room.message("*bored*")
                return
            room.message("no hablo con homosexuales")
            return
        if cmd == ("@"+self.user.name) and ran < 0.01:
            room.message("oe basura")
            room.message("si quieres los comandos pon !cmd")
            
            return
        if cmd == ("@"+self.user.name) and ran < 0.1:
            room.message("calla reconchatumare")
            return
        if cmd.lower() == "asu" and ran > 0.4:
            room.message("ala mela")
            return
        if cmd.lower() == "sobres" and ran > 0.4:
            room.message("ya vayanse a la verga changos mugrosos reconchasumare")
            return
        if cmd.lower() == ("zas") and ran < 0.4:
            room.message("largo chango viejo mugroso")
            return
        if (cmd.lower() == "ptm" or cmd.lower() == "tmr") and ran > 0.4:
            room.message("asu")
            
        if cmd.lower()[:5] == "http:":
            if user.name[0] == '!' or user.name[0] == '#':
            
                nn = user.name[1:]
            else:
                nn = user.name
                
            room.message(f"@{nn} que weadas posteas reconchatumare")
        
        if args[-5:] == "*lol*" and ran > 0.7:
            room.message("*lol*+20")
        #quita prefijo si valio
        if cmd[0] == "!":
          
          prfx = True
          cmd = cmd[1:]
        else:
          prfx = False
          
        if cmd.lower() == "cmd" and prfx:
          room.message("los comandos son estos rctmre")
          room.message("foto, y nada mas")
          return
        if cmd.lower() == "di" and prfx:
          #print(args)
          room.message(args)
          #print(findUser(message, user.name))
          #room.message(args)
        if cmd.lower() == "foto" and prfx:
          #print(args)
          if args.find(" ") == -1:
            room.message(f"https://ust.chatango.com/profileimg/{args[0]}/{args[1]}/{args}/full.jpg")
          return
        
        
    def onJoin(self, room, user):
        #print(user.name.lower())
        if user.name.lower() == 'justo' or user.name == 'ascopan' or user.name == 'loboespartano' or user.name == 'cutielord' or user.name == 'bernardino1' or user.name == 'zonavipp':
            room.message(f"ptm")
            room.message(f"ya vino el mollejas @{user.name} csm ")
        
        elif user.name.lower() == 'ohdiossa':
            room.message(f"ya vino la morsa @{user.name} csm https://ust.chatango.com/um/e/l/elperrocalato/img/l_2.jpg")
            
        elif user.name.lower() == 'alexmohas':
            room.message(f"ptm")
            room.message(f"ya vino el mochado @{user.name} csm")
            
        elif user.name == 'pzicopatha':
            room.message(f"ya vino romanela alias el cubetas @{user.name} csm https://ust.chatango.com/um/i/m/imbatible/img/l_5452.jpg")
            
        elif user.name == '1ssirena':
            room.message("asu")
            room.message("nera cachera tas?")
            room.message("https://ust.chatango.com/um/b/o/bombardero14/img/l_8550.jpg")
            
        elif user.name == 'ranitauwu' or user.name == 'clarisacristi':
            room.message(f"vino el queso @{user.name} csm https://media.discordapp.net/attachments/501417284737171471/1049108999070560277/imageedit_1_3045689395.png")
            
        elif user.name == 'imbatible':
            room.message(f"ya vino este enano pelao @{user.name} rcsmre https://i.postimg.cc/LsQ27KW6/Whats-App-Image-2023-01-24-at-1-17-03-AM.jpg")
            
        elif user.name.lower() == 'neninchat':
            room.message(f"ya vino el tucan @{user.name} csm https://ust.chatango.com/um/n/e/nenincxats/img/l_31.jpg")
            
        elif user.name == 'viejillorancio' or user.name == 'josepan' or user.name == 'altobarbon' or user.name == 'elmirochido' or user.name == 'cocolichetuntun' or user.name == 'viejorata' or user.name == 'viejozopilotefeo' or user.name == 'chagani' or user.name == 'culofrijoloso' or user.name == 'changoperraloca' or user.name == 'viejillorogon':
            
            room.message(f"ya vino este viejo de costrapan @{user.name} csm https://i.postimg.cc/4dh8dm4M/l-2977.jpg")
            room.message(f"pelea de changos subnormales")
            room.message("en 3")
            room.message("2")
            room.message("1 ...")
            
        elif user.name.lower() == 'buchonahermosa':
            room.message(f"tmr ya vino la putilla de costrapan @{user.name} csm https://ust.chatango.com/um/c/a/cabronsote00/img/l_3020.jpg")
            
        elif user.name.lower() == 'alkaboy' or user.name == 'alka':
            room.message(f"ya vino el tobi @{user.name} csm")
            
        elif user.name.lower() == 'coneja10':
            room.message("asu")
            room.message("la coneja csm")
            room.message("gordeja bola de grasa tas?")
            
        elif user.name.lower() == 'letmelickurnipples':
            room.message("gato seco tas?")
            
        elif user.name.lower() == 'doge2023':
            room.message("llego el gran doge https://imgflip.com/s/meme/Doge.jpg")
            
        elif user.name == 'devany' or user.name == 'diabla' or user.name == 'uf':
            room.message(f"ya vino la momia @{user.name} csm https://ust.chatango.com/um/a/n/ancianas/img/l_92.jpg")
            
        elif user.name.lower() == 'batmanyrobbin':
            #room.message("asu")
            room.message(f"teton rafa leonardo leonel garcia rodriguez alias gorgojo tas?")
            oom.message("responde cagada")
        else:
            
            room.message(f"ya vino @{user.name.lower()} csm")
            
            
    def onLeave(self, room, user):
        if user.name.lower() == 'justo' or user.name == 'ascopan' or user.name == 'loboespartano' or user.name == 'cutielord' or user.name == 'bernardino1' or user.name == 'zonavipp':
            room.message("se abrio el mollejas")
            room.message("que putiza le dieron al mollejas csm")
            
        elif user.name.lower() == '1ssirena':
            room.message("se fue la nera cachera")
            
        elif user.name.lower() == 'ohdiossa':
            room.message(f"se abrio la morsa")
        
        elif user.name.lower() == 'pzicopatha':
            room.message(f"se abrio el cubetas")
            
        elif user.name == 'ranitauwu' or user.name == 'clarisacristi':
            room.message(f"se fue el queso")
            
        elif user.name == 'imbatible':
            room.message(f"se abrio el enano pelao")
        
        elif user.name == 'letmelickurnipples':
            room.message("se fue el gato seco csm")
            
        elif user.name.lower() == 'alexmohas':
            room.message(f"se abrio el mochado")
            
        elif user.name == 'buchonahermosa':
            room.message(f"se fue la buches putilla de costrapan")
            
        elif user.name == 'viejillorancio' or user.name == 'josepan' or user.name == 'altobarbon' or user.name == 'elmirochido' or user.name == 'cocolichetuntun' or user.name == 'viejorata' or user.name == 'viejozopilotefeo' or user.name == 'perrochillon' or user.name == 'culofrijoloso' or user.name == 'changoperraloca' or user.name == 'viejillorogon':
            room.message(f"se abrio costrapan y no de anon")
            
        elif user.name.lower() == 'alkaboy' or user.name == 'alka':
            room.message(f"se abrio el tobi")
            
        elif user.name.lower() == 'coneja10':
            room.message(f"se fue la coneja csm")
            
        elif user.name.lower() == 'batmanyrobbin':
            room.message(f"se fue el teton csm")
            
        elif user.name.lower() == 'doge2023':
            room.message(f"se fue el gran doge")
            
        elif user.name == 'devany' or user.name == 'diabla' or user.name == 'uf':
            room.message(f"se fue la momia")
            
        else:
            #time.sleep(3)
            room.message(f"se fue {user.name.lower()}")
            
    def onFloodWarning(self, room):
        print("onflood, vamos a reconect")
        time.sleep(5)
        room.reconnect()
        time.sleep(5)


#clase ch user
rooms = ["todocritv", "fulltvhd"]
username = "eleuterio077"
password = "quispe"

bot.easy_start(rooms,username,password)



# b'bmsg:tl2r:<f x13000="Courier"><nE5DE0B/>ya vino @ruizkarely csm\r\n\x00'