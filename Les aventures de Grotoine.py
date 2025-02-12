import random
rand = random.randint(1,10)
print ("grotoine doit s'entrainer dans la salle de sport mais avant il doit manger sainement")
# cette variable permet de choisir entre un burger ou des pâtes avec une poitrine de poulet
manger = input ("grotoine hesite entre un burger (bur) ou des pâtes avec une poitrine de poulet (pat) ?")
#cette boucle permet de forcer le personnage a manger sainement en le faisant recommencer si il choisit le burger
while manger != "pat":
    manger = input ("grotoine hesite entre un burger (bur) ou des pâtes avec une poitrine de poulet (pat) ?")
entrainement = input ("voulez vous faire le haut du corp (h) ou le bas du corp (b) ?")
#CONDITION PERMETTANT faire un choix entre le haut du corp ou le bas du corp
if entrainement == "h":
    print("grotoine se dirige vers le bench press aidez le a compter ses séries")
    for i in range(1, 13):
        print(i)
    print("apres quelques séries, il sentez vos muscles gonfler!")
elif entrainement == "b":
    print("grotoine se dirige vers le legpress aidez le a compter ses séries")
    for i in range(1, 15):
        print(i)
    print("ses jambes tramblent apres une intense séances")
else:
    print("choix invalide. grostoine finit par hesiter et rentre chez lui sans entrainement")
print ("fin de la séance, grostoine rentre chez lui satisfait")
print ("pour que grotoine recois  une occasion en or essayer de deviner mon chiffre")
#Boucle permettant de deviner le chiffre aléatoire grace a un input qui permet de choisir un chiffre entre 1 et 10.(ne pas oublier int pour convertir le str en int)
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
