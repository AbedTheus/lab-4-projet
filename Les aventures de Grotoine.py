import random
rand = random.randomint(1,10)
print ("grotoine entre dans la salle de sport")
entrainement = input ("voulez vous faire le haut du corp (h) ou le bas du corp (b) ?")
if entrainement == "h":
    print("vous vous dirigez vers le bench press")
    print("apres quelques séries, vous sentez vos muscles gonfler!")
elif entrainement == "b":
    print("vous vous dirigez vers le legpress")
    print("vos jambes tranblent apres une intense séances")
else:
    print("choix invalide. grostoine finit par hesiter et rentre chez lui sans entrainement")
print ("fin de la séance, grostoine rentre chez lui satisfait")
print("Un an après...")
print("Grotoine est devenu musclé et un jour, un recruteur de bodybuilding vien voir grotoine.")

choix = input ("voulez-vous suivre mon entrainement et prendre des produit dopant (oui) ou continuer à rester clean (non)?")
if choix == "oui":
    print ("Grotoine passe un an à s'entrainer sous stéroïdes")
    print ("Grotoine finit par être pret pour son premier tournoi")
elif choix == "non":
    print ("Grotoine continue de s'entrainer et reste naturel")
    print ("il finit par s'inscrire dans un concour de bodybuilding naturel sous les conseils de son gymbro")
