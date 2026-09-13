import math 

print ("---CALCULATRICE----")
while True:
    opérateur = input("Quelle opération voulez vous effectuer ?(reel ou vectorielle) ")
    if opérateur == "reel":
        while True:
            op_réel = input("quelle operation voulez vous effectuer : addition, soustraction,multiplication,division,puissance ? ")
            A = float(input("Veuillez saisir un nombre: "))
            if A > 0: 
                print ("le nombre est positf")
            elif A < 0: 
                print("le nombre est négatif")
            else: 
                print("Le nombre est neurtre")

            B = float(input("Veuillez saisir un nombre: "))
            if B  > 0:
                print("le nombre est positif")
            elif B < 0:
                print("le nombre est négatif")
            else: 
                print("Le nombre est neutre")
     
   

            if (op_réel == "addition"):
                print ("La somme est:",A+B) 
            elif ( op_réel == "soustraction"):
                print ("Le reste est:",A-B)
            elif(op_réel== "multiplication"):
                print  ("Le produit est:",A*B)     
            elif(op_réel == "division"):
                if B != 0: 
                    print ("Le quotient est:",format(A/B,".2f")) 
                else: 
                    print("Division par zéro impossible")
            elif (op_réel == "puissance"):
                print("La puissance est:",A**B)
            else: 
                print("Opérateur incorrect")
            réponse = input("Veux refaire un calcul réel ?(O/N)")
            if réponse == "N":
                break
        break
     
    elif opérateur == "vectorielle":
        print("1 - Composante scalaire") 
        print("2 - Produit scalaire") 
        print("3 - Orthogonalité")
        print("4 - Distance entre deux point") 
        print("5 - Colinéarité ")
        op_vecteur = int(input("Quelle calcul veux tu effectuer (1,2,3,4,5) ? "))
        if op_vecteur == 1:
            xa = float(input("Veuillez entrer les coordonnés de xa: "))
            ya = float(input("Veuillez entrer les coordonnés de ya: "))
            xb = float(input("Veuillez entrer les coordonnés de xb: "))
            yb = float(input("Veuillez entrer les coordonnés de yb: "))
            x_AB =xb - xa 
            y_AB = yb -ya
            AB =(x_AB,y_AB)
            print("les coordonnées du vecteur AB sont:",AB)

        elif op_vecteur == 2: 
            xa = float(input("Veuillez entrer les coordonnés de xa: "))
            ya = float(input("Veuillez entrer les coordonnés de ya: "))
            xb = float(input("Veuillez entrer les coordonnés de xb: "))
            yb = float(input("Veuillez entrer les coordonnés de yb: "))
            AB = (xb-xa)**2 + (yb-ya)**2
            math.sqrt (AB)
            xc = float(input("Veuillez entrer les coordonnés de xc: "))
            yc = float(input("Veuillez entrer les coordonnés de yc: "))
            AC = (xc-xa)**2 + (yc - ya)**2
            math.sqrt (AC)
            angle = float(input("Angle BÂC = "))
            produit_scalaire = AB * AC * math.cos(angle)
            print("Le produit scalaire est:",format(produit_scalaire,".2f"))

        elif op_vecteur == 3:
            xa = float(input("Veuillez entrer les coordonnés de xa: "))
            ya = float(input("Veuillez entrer les coordonnés de ya: "))
            xb = float(input("Veuillez entrer les coordonnés de xb: "))
            yb = float(input("Veuillez entrer les coordonnés de yb: "))
            AB = (xb-xa)**2 + (yb-ya)**2
            math.sqrt (format(AB,".2f"))

            xc = float(input("Veuillez entrer les coordonnés de xc: "))
            yc = float(input("Veuillez entrer les coordonnés de yc: "))
            AC = (xc-xa)**2 + (yc - ya)**2
            math.sqrt (format(AC,".2f"))
            angle = float(input("Angle BÂC = "))
            produit_scalaire = AB * AC * math.cos(angle)
            if produit_scalaire == 0:
                print("Les vecteurs AB et AC sont orthogonaux.")
            else: 
                print("Les vecteurs AB et AC ne sont pas orthogonaux")

        elif op_vecteur == 4: 
            xa = float(input("Veuillez entrer les coordonnés de xa: "))
            ya = float(input("Veuillez entrer les coordonnés de ya: "))
            xb = float(input("Veuillez entrer les coordonnés de xb: "))
            yb = float(input("Veuillez entrer les coordonnés de yb: "))

            AB = (xb-xa)**2 + (yb-ya)**2
            math.sqrt(AB)
            print("La distance AB est:",format(AB,".2f"))

        elif op_vecteur == 5: 
            x_AB =float(input("Veuillez entrer les coordonnées de x_AB: "))
            y_AB =float(input("Veuillez entrer les coordonnées de y_AB: "))
            x_AM =float(input("Veuillez entrer les coordonnées de x_AM: "))
            y_AM =float(input("Veuillez entrer les coordonnées de y_AM: "))
            det = (x_AB*y_AM) - (x_AM*y_AB)
            if det == 0: 
                print('Ces deux vecteurs sont colinéaires.')
            else: 
                print("Ces deux vecteurs ne sont pas colinéaires.")
        else:
            print('Choix du calcul incorrect')
    else: 
        print("Opérateur incorrect !")
    reponse = input("Veux tu refaire un calcul ?(O/N)")
    if reponse == "N": 
        break 





    
