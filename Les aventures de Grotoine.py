import random
rand = random.randint(1,10)
print ("grotoine doit s'entrainer dans la salle de sport mais avant il doit manger sainement")
manger = input ("grotoine hesite entre un burger (bur) ou des pâtes avec une poitrine de poulet (pat) ?")
while manger != "pat":
    manger = input ("grotoine hesite entre un burger (bur) ou des pâtes avec une poitrine de poulet (pat) ?")
entrainement = input ("voulez vous faire le haut du corp (h) ou le bas du corp (b) ?")
if entrainement == "h":
    print("grotoine se dirige vers le bench press aidez le a compter ses séries")
    for i in range(1, 13):
        print(i)
    print("apres quelques séries, il sentez vos muscles gonfler!")
elif entrainement == "b":
    print("vous vous dirigez vers le legpress")
    print("vos jambes tranblent apres une intense séances")
else:
    print("choix invalide. grostoine finit par hesiter et rentre chez lui sans entrainement")
print ("fin de la séance, grostoine rentre chez lui satisfait")
print ("pour que grotoine recoisune occasion en or essayer de deviner mon chiffre")
choixnbr = int(input("choisit un nombre entre (1,10)"))
while rand != choixnbr:
    choixnbr = int(input("choisit un nombre entre (1,10)"))
    if rand == choixnbr:
        break
print("Grotoine est devenu musclé et un jour, un recruteur de bodybuilding vien voir grotoine.")
choix = input ("voulez-vous suivre mon entrainement et prendre des produit dopant (oui) ou continuer à rester clean (non)?")
if choix == "oui":
    print ("Grotoine passe un an à s'entrainer sous stéroïdes")
    print ("Grotoine finit par être pret pour son premier tournoi")
elif choix == "non":
    print ("Grotoine continue de s'entrainer et reste naturel")
    print ("il finit par s'inscrire dans un concour de bodybuilding naturel sous les conseils de son gymbro")
