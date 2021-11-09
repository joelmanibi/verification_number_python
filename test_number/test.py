import re

# creation de liste et insertion de prefix en fontion du reseau
MTN = ["04", "05", "06", "44", "45", "46", "54", "55", "56",
 "64","65","66", "74", "75", "76", "84", "85", "86", "94", "95", "96"]

ORANGE = ["07", "08", "09", "47", "48", "49", "57", "58", "59",
"67", "68", "69", "77", "78", "79", "87", "88", "89", "97", "98"]

MOOV = ["01", "02", "03", "40", "41", "42", "43", "50", "51", "52", "53", "70", "71", "72", "73"]

# entrée du numero de tel 
phone = input("Entrer votre numero svp: ")

print('Vous avez entré le :',phone)
extension = phone[-8:12]
# print(extension)
prefix = extension[0:2]
print("Votre prefix actuel est:",prefix)

# verification et traitement du numero

if prefix in ORANGE:
    newpref= "07"
    numfinal = newpref+extension
    print("Orange est votre reseau actuel")
    print("votre nouveau numero est:",numfinal)

elif prefix in MTN:
    newpref= "05"
    numfinal = newpref+extension
    print("Mtn est votre reseau actuel")
    print("votre nouveau numero est:",numfinal)

else:
    newpref= "01"
    numfinal = newpref+extension
    print("moov est votre reseau actuel")
    print("votre nouveau numero est:",numfinal)

