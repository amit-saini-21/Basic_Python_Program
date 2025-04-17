import random
a=["Rock","Paper","Scissor"]
print("\t\t\tLet's Play Rock✊ Paper🖐 Scissor✌  ")
print("\t\t\t——————————————————————————————————")
print("Note:- Write any one From rock,paper,scissor\n\n")
while(True):
 b=input("Choose any one from Rock,Paper,Scissor or exit:\n")
 if(b=="Rock" or b=="Paper" or b=="Scissor" or b=="rock" or b=="paper" or b=="Scissor" or b=="scissor" or b=="Exit" or b=="exit"):
    c=random.choice(a)
    if(((b=="Rock" or b=="rock") and c=="Rock") or ((b=="Paper" or b=="paper") and c=="Paper") or ((b=="Scissor" or b=="scissor") and c=="Scissor")):
       print("\t\t\t\t🙄 Draw")
    elif((b=="Rock" or b=="rock") and c=="Paper"):
       print(c,"\t\t\t\nYou lose 😛")
    elif((b=="Rock" or b=="rock") and c=="Scissor"):
       print(c,"\t\t\t\nYou Win 😎")
    elif((b=="Paper" or b=="paper") and c=="Rock"):
       print(c,"\t\t\t\nYou Win 😎")
    elif((b=="Paper" or b=="paper") and c=="Scissor"):
       print(c,"\t\t\t\nYou lose 😛")
    elif((b=="Scissor" or b=="scissor") and c=="Rock"):
       print(c,"\t\t\t\nYou lose 😛")
    elif((b=="Scissor" or b=="scissor") and c=="Paper"):
       print(c,"\t\t\t\nYou Win 😎")
    else:
      break
 else:
    print("Try Again or Wrong Input")
print("\t\t\t\tThank you for Playing")
