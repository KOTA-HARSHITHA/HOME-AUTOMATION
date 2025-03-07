Last login: Tue May 21 18:59:49 on console
kotaharshitha@kotas-MacBook-Air ~ % nano voice_assistant.py






















  UW PICO 5.09                File: voice_assistant.py                Modified  

        camera=cv2.VideoCapture(0)
        Name=input("enter your name: ")
        for i in range(10):
            return_value, image = camera.read()
            cv2.imwrite(Name+str(i)+'.png', image)
        del(camera)
        file=open("F:/actors.csv","a")
        file.write("\n"+str(counter)+","+Name+",C:/Users/DELL/OneDrive/Desktop/$
        file.close()
    
        
counter = 0
while True:
    run_alexa()
    counter +=1
        
        
        
        

^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Pg   ^K Cut Text  ^C Cur Pos   
^X Exit      ^J Justify   ^W Where is  ^V Next Pg   ^U UnCut Text^T To Spell  
