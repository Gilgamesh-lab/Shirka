#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def bloquer():
    pass
    #os.popen("attrib +r +h  Donnee.json")
    
def debloquer():
    pass
    #os.popen("attrib -r -h   Donnee.json")


# In[ ]:


import json

def save(dico,name):
    #debloquer()
   # try:
     #   tf = open(f"{name}.json", "w")
        
   # except PermissionError:
     #   bloquer()
      #  debloquer()
      #  tf = open(f"{name}.json", "w")
       
    tf = open(f"{name}.json", "w")
    json.dump(dico,tf)
    tf.close()
    #bloquer()
    
def load(file):
    tf = open(f"{file}.json", "r")
    new_dict = json.load(tf)
    tf.close()
    return new_dict


# In[ ]:




def copier(chaine):
    
    # set clipboard data
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()    
    win32clipboard.SetClipboardText(chaine)
    win32clipboard.CloseClipboard()

def coller():
   
    try:
        # get clipboard data
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data
    
    except TypeError:
        return ""


# In[ ]:




def souris():
    t = True
    while t:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                b = int(pos[0]) // 10
                a = int(pos[1]) // 10
                return a,b
            if event.type == QUIT:    
                pygame.quit()
                sys.exit()


# In[ ]:


def appoint2(nb,appoint):
    lg = nb // 10 
    if nb / 10 - lg >= appoint:
        nb += 1 
    return nb 


# In[ ]:


def appoint(nb,appoint):
    lg = nb // 10 
    if nb / 10 - lg >= appoint:
        lg += 1 
    return lg


# In[ ]:


def cryptage(chaine_non_cryptee,clée_codage):
    """
    Renvoie une chaîne de caractères modifiée dans laquelle le code de chaque lettre a été augmenté de 4
    - Entrée : chaine_non_cryptee (chaîne de caractères)
    - Sortie : chaine_cryptee (chaîne de caractères)
    """
    if type(chaine_non_cryptee) != bool or chaine_non_cryptee != '':
        if type(chaine_non_cryptee) != str:
            raise TypeError('le paramètre doit être une chaîne de caractères')
        chaine_cryptee = ''
        for lettre in chaine_non_cryptee:
            if lettre != ' ':
                chaine_cryptee = chaine_cryptee + chr(ord(lettre) + clée_codage)
            else:
                chaine_cryptee = chaine_cryptee + ' '
        return chaine_cryptee


# In[ ]:


def decryptage(chaine_cryptee,nb):
    """
    Renvoie une chaîne de caractères modifiée dans laquelle le code de chaque lettre a été diminué de 4
    - Entrée : chaine_cryptee (chaîne de caractères)
    - Sortie : chaine_non_cryptee (chaîne de caractères)
    """
    if type(chaine_cryptee) != str:
        raise TypeError('le paramètre doit être une chaîne de caractères')
    chaine_non_cryptee = ''
    for lettre in chaine_cryptee:
        if lettre != ' ':
            chaine_non_cryptee = chaine_non_cryptee + chr(ord(lettre) - nb)
        else:
            chaine_non_cryptee = chaine_non_cryptee + ' '
    return chaine_non_cryptee


# In[ ]:


def asci(phrase):
    """
    Transforme une chaîne de caractères en enlevant majuscules et accents.
    - Entrée : phrase (chaîne de caractères)
    - Sortie : nouvelle_phrase (chaîne de caractères)
    """
    if type(phrase) != str:
        raise TypeError('le paramètre doit être une chaîne de caractères')
    nouvelle_phrase = ''
    for lettre in phrase:
        if lettre == '[':
            nouvelle_phrase += ' '
        elif lettre == ']':
            nouvelle_phrase += ' '
        elif lettre == "'":
            nouvelle_phrase += ' '
        elif lettre == ',':
            nouvelle_phrase += ' '
        else:
            nouvelle_phrase += lettre
    return nouvelle_phrase


# In[ ]:


def asci2(phrase):
    """
    Transforme une chaîne de caractères en enlevant majuscules et accents.
    - Entrée : phrase (chaîne de caractères)
    - Sortie : nouvelle_phrase (chaîne de caractères)
    """
    if type(phrase) != str:
        raise TypeError('le paramètre doit être une chaîne de caractères')
    nouvelle_phrase = ''
    for lettre in phrase:
        if lettre == '[':
            nouvelle_phrase += ' '
        elif lettre == ']':
            nouvelle_phrase += ' '
        elif lettre == "'":
            nouvelle_phrase += ' '
        elif lettre == ' ':
            nouvelle_phrase += ' ' + ' , ' + ' '
        elif lettre == ',':
            nouvelle_phrase += ' ' 
        else:
            nouvelle_phrase += lettre
    return nouvelle_phrase


# In[ ]:


def asci3(phrase):
    """
    Transforme une chaîne de caractères en enlevant majuscules et accents.
    - Entrée : phrase (chaîne de caractères)
    - Sortie : nouvelle_phrase (chaîne de caractères)
    """
    if type(phrase) != str:
        raise TypeError('le paramètre doit être une chaîne de caractères')
    alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','é',
           '(',')','_','è','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
          'X','Y','Z','à','ç','1','2','3','4','5','6','7','9','@','?','!','.','*','ù', "/" , "=","=","+","-","/"]
    k = 0
    nouvelle_phrase = ''
    for lettre in phrase:
        for o in range(len(alp)):
            if lettre == alp[o]:
                nouvelle_phrase += lettre
                k = 1
            if lettre == ' ' and k == 1:
                nouvelle_phrase += ' ' + ',' + ' ' 
                k = 0
    return nouvelle_phrase


# In[ ]:


def chiffrage(phrase):
    """
    Transforme une chaîne de caractères en enlevant majuscules et accents.
    - Entrée : phrase (chaîne de caractères)
    - Sortie : nouvelle_phrase (chaîne de caractères)
    """
    if type(phrase) != str:
        raise TypeError('le paramètre doit être une chaîne de caractères')
    nouvelle_phrase = ''
    for lettre in phrase:
        if lettre == '1':
            nouvelle_phrase += 'h '
        elif lettre == '2':
            nouvelle_phrase += 'i '
        elif lettre == "3":
            nouvelle_phrase += 'k '
        elif lettre == '4':               
            nouvelle_phrase += 'd '
        elif lettre == '5':
            nouvelle_phrase += 'v '
        elif lettre == "6":
            nouvelle_phrase += 'q '
        elif lettre == '7':
            nouvelle_phrase += 'y '
        elif lettre == '8':                 
            nouvelle_phrase += 'p '
        elif lettre == "9":
            nouvelle_phrase += 's '
        else:
            nouvelle_phrase += lettre
    nouvelle_phrase = correct(nouvelle_phrase)
    return nouvelle_phrase


# In[ ]:


def dechiffrage(phrase):
    """
    Transforme une chaîne de caractères en enlevant majuscules et accents.
    - Entrée : phrase (chaîne de caractères)
    - Sortie : nouvelle_phrase (chaîne de caractères)
    """
    if type(phrase) != str:
        raise TypeError('le paramètre doit être une chaîne de caractères')
    nouvelle_phrase = ''
    phrase = decorrect(phrase)
    for lettre in phrase:
        if lettre == 'h':
            nouvelle_phrase += '1 '
        elif lettre == 'i':
            nouvelle_phrase += '2 '
        elif lettre == "k":
            nouvelle_phrase += '3 '
        elif lettre == 'd':
            nouvelle_phrase += '4 '
        elif lettre == 'v':
            nouvelle_phrase += '5 '
        elif lettre == "q":
            nouvelle_phrase += '6 '
        elif lettre == 'y':
            nouvelle_phrase += '7 '
        elif lettre == 'p':
            nouvelle_phrase += '8 '
        elif lettre == "s":
            nouvelle_phrase += '9 '
        else:
            nouvelle_phrase += lettre
    return nouvelle_phrase


# In[ ]:


def surcorrect(phrase):# enlève les espaces
    """
    Transforme une chaîne de caractères en enlevant majuscules et accents.
    - Entrée : phrase (chaîne de caractères)
    - Sortie : nouvelle_phrase (chaîne de caractères)
    """
    if type(phrase) != str:
        raise TypeError('le paramètre doit être une chaîne de caractères')
    nouvelle_phrase = ''
    for lettre in phrase:
        if lettre == ' ':
            nouvelle_phrase = nouvelle_phrase
        else:
            nouvelle_phrase += lettre
    
    return nouvelle_phrase


# In[ ]:


def correct(phrase):
    """
    Transforme une chaîne de caractères en enlevant majuscules et accents.
    - Entrée : phrase (chaîne de caractères)
    - Sortie : nouvelle_phrase (chaîne de caractères)
    """
    if type(phrase) == bool:
        return phrase
    else:
        if type(phrase) != str:
            raise TypeError('le paramètre doit être une chaîne de caractères')
        nouvelle_phrase = ''
        for lettre in phrase:
            if lettre == ' ':
                nouvelle_phrase += '_'
            else:
                nouvelle_phrase += lettre

        return nouvelle_phrase


# In[ ]:


def decorrect(phrase):
    """
    Transforme une chaîne de caractères en enlevant majuscules et accents.
    - Entrée : phrase (chaîne de caractères)
    - Sortie : nouvelle_phrase (chaîne de caractères)
    """
    if type(phrase) != str:
        raise TypeError('le paramètre doit être une chaîne de caractères')
    nouvelle_phrase = ''
    for lettre in phrase:
        if lettre == '_':
            nouvelle_phrase += ' '
        else:
            nouvelle_phrase += lettre
    
    return nouvelle_phrase


# In[ ]:


def decorrect2(phrase):
    """
    Transforme une chaîne de caractères en enlevant majuscules et accents.
    - Entrée : phrase (chaîne de caractères)
    - Sortie : nouvelle_phrase (chaîne de caractères)
    """
    if type(phrase) != str:
        raise TypeError('le paramètre doit être une chaîne de caractères')
    nouvelle_phrase = ''
    for lettre in phrase:
        if lettre == '_':
            nouvelle_phrase += ' '
        elif lettre == "'":
            nouvelle_phrase += ' '
        elif lettre == '[':
            nouvelle_phrase += ' '
        elif lettre == ']':
            nouvelle_phrase += ' '
        else:
            nouvelle_phrase += lettre
    
    return nouvelle_phrase


# In[ ]:



def aléa():
    
    choix = randint(0,4)
    if choix == 0:
        g = randint(65,90)
    if choix == 1:
        g = randint(97,122)
    if choix == 2:
        g = randint(48,57)
    if choix == 3:
        g = 63
    if choix == 4:
        g = 33
    v = chr(g)
    return v


# In[ ]:


def afficher(z,ecran,x,y,s = False,t = False,h = False):
    """
    affiche un caractère passé en paramètre lettre par lettre
    z le caractère à afficher, x et y les cordonnées , s pour cacher le contenue, t = pour ne pas raffraichir l'écran et h
    pour afficher le bouton home
    """
    if s == True:
        if h == True:
            home(ecran)
            if t == False:
                ecran.fill((43, 250, 250))
            for k in range(len(z)):
                i = '*'
                font=pygame.font.SysFont("broadway",12,bold=False,italic=False)# réglage de la police,gras et italique
                text=font.render(i,1,(0, 0, 0))# définition couleur
                ecran.blit(text,(x,y ))
                t = font.get_height()
                g = font.get_linesize()
                r = font.size(i)
                x += r[0]
                if x >= 690:
                    x = 0
                    y += 10
            pygame.display.flip()#mise à jour
            
    if s == True and h != True:
        if t == False:
            ecran.fill((43, 250, 250))
        for k in range(len(z)):
            i = '*'
            font=pygame.font.SysFont("broadway",12,bold=False,italic=False)# réglage de la police,gras et italique
            text=font.render(i,1,(0, 0, 0))# définition couleur
            ecran.blit(text,(x,y ))
            t = font.get_height()
            g = font.get_linesize()
            r = font.size(i)
            x += r[0]
            if x >= 690:
                x = 0
                y += 10
        pygame.display.flip()#mise à jou
        
    elif t == True:
        if s == False:
            if h == True:
                home(ecran)
            for k in range(len(z)):
                i = z[k]
                font=pygame.font.SysFont("broadway",12,bold=False,italic=False)# réglage de la police,gras et italique
                text=font.render(i,1,(0, 0, 0))# définition couleur
                ecran.blit(text,(x,y ))
                r = font.size(i)
                x += r[0]
                if x >= 690:
                    x = 0
                    y += 10
            pygame.display.flip()#mise à jour
    else:
        if s == False:
            if h == True:
                home(ecran)
            ecran.fill((43, 250, 250))
            for k in range(len(z)):
                i = z[k]
                font=pygame.font.SysFont("broadway",12,bold=False,italic=False)# réglage de la police,gras et italique
                text=font.render(i,1,(0, 0, 0))# définition couleur
                ecran.blit(text,(x,y ))
                t = font.get_height()
                g = font.get_linesize()
                r = font.size(i)
                x += r[0]
                if x >= 690:
                    x = 0
                    y += 10
            pygame.display.flip()#mise à jour


# In[ ]:



def clavier(question,ecran,x,y,s = False,h = False,r = False):
    """
    fonction: input pour pygame --> affiche du texte et permet à l'utilisateur d'y répondre
    paramètre d'entrée : question : str , ecran : interface pygame , x,y : entier (coordonnée)
    effet de bord : affiche du texte et affiche la saisie de la réponse en cours
    paramètre de sortie : renvoie la réponse de l'utilisateur
    """
    
    afficher(question,ecran,x,y,False,r)
    z = ""
    n = ""
    t = True
    if h == True:
        home(ecran)
    while t:
        for evenement in pygame.event.get():
            keys = pygame.key.get_pressed()
            
            
            if keys[pygame.K_a]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT] and not keys[K_BACKQUOTE] and not keys[K_CARET]:
                    z += "a"
                    
                    
                if keys[K_CARET]:
                    z += "â"
                
                if   keys[K_RSHIFT] or keys[K_LSHIFT]:
                    z += "A"
                
                
            if keys[K_0] and not keys[K_RALT] and not keys[K_LALT] :
                z += "à"
                
                
            if keys[K_0] and  keys[K_RALT] or keys[K_LALT]:
                z += "@"
                
                    
            if keys[pygame.K_b]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "b"
                else:
                    z += "B"
                
                
            if keys[pygame.K_c] and not keys[K_RCTRL] and not keys[K_LCTRL]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "c"
                if   keys[K_RSHIFT] or keys[K_LSHIFT]:
                    z += "C"
                
                
            if keys[K_9]:
                z += "ç"
                
                
            if keys[K_8]:
                z += "_"
                
                    
            if keys[pygame.K_d]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "d"
                else:
                    z += "D"
                
                
            if keys[pygame.K_e]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT] and not keys[K_BACKQUOTE] and not keys[K_CARET] :
                    z += "e"
                    
                if keys[K_BACKQUOTE]:
                    z += "è"
                    
                if keys[K_CARET]:
                    z += "ê"
                    
                if   keys[K_RSHIFT] or keys[K_LSHIFT]:
                    z += "E"
                
                    
            if keys[K_2]:
                z +="é"
                
            if keys[K_7]:
                z +="è"
                
                    
                    
            if keys[pygame.K_f]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "f"
                else:
                    z += "F"
                
                    
            if keys[pygame.K_g]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "g"
                else:
                    z += "G"
                
                    
            if keys[pygame.K_h]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "h"
                else:
                    z += "H"
                
                
            if keys[pygame.K_i]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "i"
                else:
                    z += "I"
                
                
            if keys[pygame.K_j]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "j"
                else:
                    z += "J"
                
                
            if keys[pygame.K_k]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "k"
                else:
                    z += "K"
                
                
            if keys[pygame.K_l]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "l"
                else:
                    z += "L"
                
                
            if keys[pygame.K_m]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "m"
                else:
                    z += "M"
                
                
            if keys[pygame.K_n]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "n"
                else:
                    z += "N"
                
                
            if keys[pygame.K_o]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "o"
                else:
                    z += "O"
                
                
            if keys[pygame.K_p]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "p"
                else:
                    z += "P"
                
                
            if keys[pygame.K_q]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "q"
                else:
                    z += "Q"
                
                
            if keys[pygame.K_r]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "r"
                else:
                    z += "R"
                
                
            if keys[pygame.K_s]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "s"
                else:
                    z += "S"
                
                
            if keys[pygame.K_t]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "t"
                else:
                    z += "T"
                
                
            if keys[pygame.K_u]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "u"
                else:
                    z += "U"
                
            if keys[pygame.K_v] and not keys[K_RCTRL] and not keys[K_LCTRL]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "v"
                else:
                    z += "V"
                
                
            if keys[pygame.K_w]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "w"
                else:
                    z += "W"
                
                
            if keys[pygame.K_x]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "x"
                else:
                    z += "X"
                
                
            if keys[pygame.K_y]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "y"
                else:
                    z += "Y"
                
                
            if keys[pygame.K_z]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "z"
                else:
                    z += "Z"
                
                
            if keys[K_5] and not keys[K_RALT] and not keys[K_LALT] :
                z += "("
                
            
            if keys[K_RIGHTPAREN] and not keys[K_RALT] and not keys[K_LALT] :
                z += ")"
                
            
                
            if keys[pygame.K_KP0]:
                z += "0"
                
                
            if keys[pygame.K_KP1]:
                z += "1"
                
                
            if keys[pygame.K_KP2]:
                z += "2"
                
                
            if keys[pygame.K_KP3]:
                z += "3"
                
                
            if keys[pygame.K_KP4]:
                z += "4"
                
                
            if keys[pygame.K_KP5]:
                z += "5"
                
                
            if keys[pygame.K_KP6]:
                z += "6"
                
                
            if keys[pygame.K_KP7]:
                z += "7"
                
                
            if keys[pygame.K_KP8]:
                z += "8"
                
                
            if keys[pygame.K_KP9]:
                z += "9"
                
                
            if keys[pygame.K_KP_PERIOD]:
                z += "."
                

            
                 
            if  keys[K_RCTRL] or keys[K_LCTRL] and  keys[pygame.K_c] and s == False :
                copier(z)
            
            #if  keys[K_RCTRL] or keys[K_LCTRL] and  keys[pygame.K_x] and s == False :
                #copier(z)
                #z = ''
                
            if  keys[K_RCTRL] or keys[K_LCTRL] and  keys[pygame.K_v]:
                z += coller()
                
            if keys[pygame.K_SPACE]: 
                z += ' '
                
            
                
            if keys[K_RETURN]:
                if len(z) > 0:
                    return z
                
            if keys[pygame.K_BACKSPACE]:
                b = ""
                for k in range(len(z)-1):
                    b = b + z[k]
                z = b
                if h == True:
                    home(ecran)
                    
            
            if n != z:#pygame.draw.rect(ecran,(43, 250, 250),(x,y,cadrage(z),10))
                afficher(question,ecran,x,y,False,False,h)
                afficher(z,ecran,x,y + 30,s,True,h)
                n = z[:]
                pygame.event.wait()
                if h == True:
                    home(ecran)
            
            if evenement.type == QUIT:    
                pygame.quit()
                sys.exit()
                  
            if evenement.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = int(pos[0]) // 10
                b = int(pos[1]) // 10
                if grille[b][a] == 'home':
                    return True
                
            #if event.type == pygame.VIDEORESIZE:
                #scrsize = event.size
                #width   = event.w
                #hight   = event.h
                #screen = pygame.display.set_mode(scrsize,RESIZABLE)
                #changed = True
        

            
            


# In[ ]:


def menu(ecran):
    liste = ['Aide','Liste','Nouveau','Changer','Mot de passe','Créer','Supprimer','Téléverser','Paramètre']
    ecran.fill((43, 250, 250))
    for k in range(len(liste)):
        chaine= liste[k]# message d'échec
        font=pygame.font.SysFont("broadway",32,bold=False,italic=False)# réglage de la police,gras et italique
        text=font.render(chaine,1,(0, 0, 0))# définition couleur
        ecran.blit(text,(330,k*70 + 50))#position(x,y) 
        pygame.display.flip()#mise à jour


# In[ ]:


def println(string,ecran,x,y,taille = 32):
    chaine = string # message d'échec
    font = pygame.font.SysFont("broadway",taille,bold=False,italic=False)# réglage de la police,gras et italique
    text = font.render(chaine,1,(0, 0, 0))# définition couleur
    ecran.blit(text,(x,y))#position(x,y) 
    pygame.display.flip()#mise à jour


# In[ ]:


def home(ecran):
    font=pygame.font.SysFont("broadway",18,bold=False,italic=False)# réglage de la police,gras et italique
    text=font.render('Accueil',1,(0, 0, 0))# définition couleur
    ecran.blit(text,(5,660))#position(x,y)
    pygame.display.flip()#mise à jour


# In[ ]:


def home_b():
    for event in pygame.event.get():
        if event.type == QUIT:    
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            a = int(pos[0]) // 10
            b = int(pos[1]) // 10
            if grille[b][a] == 'home':
                return True
            else:
                return False


# In[ ]:


def cadrage(chaine,taille = 12,police = "broadway" ,i = False):
    pygame.init()
    font=pygame.font.SysFont(police,taille,bold=False,italic=False)# réglage de la police,gras et italique
    text=font.render(chaine,1,(0, 0, 0))# définition couleur
    t = font.get_height()
    r = font.size(chaine)[0]
    if i == False:
        t = appoint(t,0.5)
        r = appoint(r,0.5)
    return t,r


# In[ ]:


def cadre(x,y,chaine,taille,grille,nb,police = "broadway",texte = False): #(x,y,chaine,taille,grille,nb,police
    long = cadrage(chaine,taille,police)[1]
    if nb == 0:
        nb = 1
    lar = cadrage(chaine,taille,police)[0]
    x = x // 10 
    y = y // 10
    for n in range(x,x + long):# grille = cadre(330,620,"fin",32,grille,9)
        if n >= 69:
            long = (x + long) - n
            x = 0
            n = 0
            k = 0 
            y = y + lar
        for k in range(y,y + lar):
            grille[k][n] = nb
    return grille


# In[ ]:


import pygame
from time import sleep
from pygame.locals import*
import os
import sys
from random import randint 
import win32clipboard
import json
import ctypes

user32 = ctypes.windll.user32
#screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)-50

af_x = 50
af_y = 100
ecran = pygame.display.set_mode((700, 700))
pygame.init()
ecran.fill((43, 250, 250))
pygame.display.set_caption('Shirka')
#Icone = pygame.image.load('embleme_du_feu.ico')
#pygame.display.set_icon(Icone)
pygame.display.flip()





a = " "

r = 0
w = 0
Lost_Blue = ''

grille = [[0 for _ in range(70)]for _ in range(70)] # menu
grille_parametre = [[0 for _ in range(70)]for _ in range(70)]  #1er sous-menu
grille_changer = [[0 for _ in range(70)]for _ in range(70)] # 2ème sous-menu



grille = cadre(330,50,"Aide",32,grille,1) #cadre(33,5,4,8,grille,1)# aide
grille = cadre(330,130,"Liste",32,grille,2) #cadre(330,13,4,8,grille,2)# liste
grille = cadre(330,200,"Nouveau",32,grille,3) #cadre(33,20,4,18,grille,3)# nouveau
grille = cadre(330,270,"Modifier",32,grille,4) #cadre(33,27,4,16,grille,4) # modifier 
grille = cadre(330,340,"Mot de passe",32,grille,5) #cadre(33,34,4,8,grille,5)# mdp
grille = cadre(330,410,"Créer",32,grille,6) #cadre(33,41,4,8,grille,6)# créer
grille = cadre(330,480,"Supprimer",32,grille,7) #cadre(33,48,4,20,grille,7)# supprimer
grille = cadre(330,550,"Téléverser",32,grille,8) #cadre(33,55,4,20,grille,8)# téléverser
grille = cadre(330,620,"Paramètre",32,grille,9) #cadre(33,62,4,6,grille,9)# fin
grille = cadre(10,660,"Accueil",32,grille,'home') #cadre(1,66,2,5,grille,10)# home 

grille_parametre = cadre(af_x - 45,af_y,"Changer le mot de passe du gestionnaire",24,grille_parametre,'mdp')
grille_parametre = cadre(af_x - 45,af_y + 70,"Changer la question",24,grille_parametre,'question')
grille_parametre = cadre(af_x - 45,af_y + 140,"Réinitialiser les données",24,grille_parametre,'donnee')



grille_changer = cadre(af_x - 45,af_y,"Changer un mot de passe",24,grille_changer,'mdp')
grille_changer = cadre(af_x - 45 ,af_y + 70,"Changer le nom d'un mot de passe",24,grille_changer,'nom')

               



if os.path.exists('Donnee.json') == True:
    donnee = load("Donnee")
    nb = donnee['nb']
    nb = int(surcorrect(dechiffrage(nb)))
    mdp = decryptage(donnee['mdp'],nb)
    reponse = decryptage(donnee['reponse'],nb)
    question = decryptage(donnee['question'],nb)
    l = clavier('Entrez le mot de passe du gestionnaire : ',ecran,af_x,af_y,True)
    l = correct(l)
    while l != mdp:
        r = r + 1 
        l = clavier('Mot de passe du gestionnaire erroné , veuiller réessayer : ' ,ecran,af_x,af_y,True)
        l = correct(l)
        
        if r == 2:
            question = str(question)
            reponse = str(reponse)
            question = decorrect(question)
            reponse = decorrect(reponse)
            u = clavier(decorrect(question) ,ecran,af_x,af_x)
            while u != reponse:
                afficher('Mauvaise réponse',ecran,af_x,af_y)
                sleep(2)
                u = clavier(decorrect(question) ,ecran,af_x,af_y)
                if u == 'home':
                    break
            if u == reponse:
                w = 1
                afficher('Bonne réponse',ecran,af_x,af_y)
                mdp = clavier('Entrez un nouveau mot de passe pour le gestionnaire: ',ecran,af_x,af_y,True) 
                z = clavier('Entrez à nouveau mot de passe pour le gestionnaire: ',ecran,af_x,af_y,True) 
                while z != mdp:
                    afficher("La seconde entrée n'est pas la même que la première, réessayer",ecran,af_x,af_y)
                    sleep(2)
                    mdp = clavier('Entrez un nouveau mot de passe pour le gestionnaire: ',ecran,af_x,af_y,True)
                    z = clavier('Entrez à nouveau mot de passe pour le gestionnaire: ',ecran,af_x,af_y,True)
                mdp = correct(mdp)
                donnee['mdp'] = cryptage(mdp,nb)
                save(donnee,'Donnee')
                break
                
    if w != 1:
        bonjour_phrase = randint(0,14)
        
        if bonjour_phrase == 0:
            afficher('Mot de passe correcte, bienvenue :)',ecran,af_x,af_y)
            
        if bonjour_phrase == 1:
            afficher('Ravie de vous revoir :)',ecran,af_x,af_y)
            
        if bonjour_phrase == 2:
            afficher('Content de vous retrouver :)',ecran,af_x,af_y)
            
        if bonjour_phrase == 3:
            afficher('Identification réussie, bienvenue :)',ecran,af_x,af_y)
            
        if bonjour_phrase == 4:
            afficher('Connexion réussie, heureux de vous revoir :)',ecran,af_x,af_y)
            
        if bonjour_phrase == 5:
            afficher('Initialisation du processus terminé, prêt à vous servir :)',ecran,af_x,af_y)
            
        if bonjour_phrase == 6:
            afficher('Formalité terminée , time to work   :)',ecran,af_x,af_y)
            
        if bonjour_phrase == 7:
            afficher('Code correct, chargement du menu :)',ecran,af_x,af_y)
            
        if bonjour_phrase == 8 :
            afficher("Code d'identification valide, bonne arrivée :)",ecran,af_x,af_y)
            
        if bonjour_phrase == 9 :
            afficher("Phase d'identification terminé, bienvenue :)",ecran,af_x,af_y)
            
        if bonjour_phrase == 10 :
            afficher("Code correct, heureux de vous accueillir :)",ecran,af_x,af_y)
            
        if bonjour_phrase == 11 :
            afficher("Mot de passe correcte, welcome :)",ecran,af_x,af_y)
        
        if bonjour_phrase == 12 :
            afficher("Mot de passe correcte, bonne naviguation :)",ecran,af_x,af_y)
            
        if bonjour_phrase == 13 :
            afficher("Mot de passe valide, bonne utilisation :)",ecran,af_x,af_y)
                     
        if bonjour_phrase == 14 :
            afficher("Phase d'identification terminé, chargement du menu  :)",ecran,af_x,af_y)
            
        sleep(2)
else:
    donnee = {}
    nb = randint(20,500) 
    donnee = {'nb' : {} ,'mdp' : {} ,'question' : {} ,'reponse' : {} , 'donnee' : {} }
    donnee['nb'] = chiffrage(str(nb))
    mdp = clavier( 'Entrez un mot de passe pour le gestionnaire: ',ecran,af_x,af_y,True )
    z = clavier( 'Entrez à nouveau le mot de passe pour le gestionnaire: ',ecran,af_x,af_y,True )
    while z != mdp:
        afficher("La seconde entrée n'est pas la même que la première, réessayer",ecran,af_x,af_y)
        sleep(5)
        clavier( 'Entrez un mot de passe pour le gestionnaire: ',ecran,af_x,af_y,True )
        z = clavier( 'Entrez à nouveau le mot de passe pour le gestionnaire: ',ecran,af_x,af_y,True )
    mdp = correct(mdp)
    donnee['mdp'] = cryptage(mdp,nb)
    question = clavier('Au cas où vous oublierez votre mot de passe entrer une question à laquelle vous seul pouvez répondre : ',ecran,af_x,af_y)
    question = correct(question)
    donnee['question'] = cryptage(question,nb)
    reponse =  clavier('Entrez la réponse à cette question : ' , ecran,af_x,af_y)      
    z = clavier('Entrez à nouveau  la réponse à cette question : ' , ecran,af_x,af_y)
    
    while z != reponse:
        afficher("La seconde entrée n'est pas la même que la première, réessayer", ecran,af_x,af_y)
        sleep(2)
        reponse = clavier('Entrez la réponse à cette question : ' , ecran,af_x,af_y)
        z = clavier('Entrez à nouveau  la réponse à cette question : ' , ecran,af_x,af_y)
    reponse = correct(reponse)
    donnee['reponse'] = cryptage(reponse,nb)
    donnee['donnee'] = {}
    save(donnee,'Donnee')
    bloquer()
    
menu(ecran) 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
                
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            b = int(pos[0]) // 10
            a = int(pos[1]) // 10
            
        
            
            
            if grille[a][b] == 1: #aide
                afficher('Voici la liste des commandes : ', ecran,af_x,af_y)
                afficher('Aide : Affiche toutes les commandes et leurs fonctions', ecran,af_x,af_y + 10,t = True)
                afficher('Liste : Ecran tactile qui affiche les noms des mots de passes , cliquer sur un mot pour le copier ', ecran,af_x,af_y + 20,t = True)
                afficher('Nouveau : Permet de créer un nouveau mot de passe avec sa signfication', ecran,af_x,af_y + 30,t = True)
                afficher('Changer : Permet de modifier un mot de passe', ecran,af_x,af_y + 40,t = True)
                afficher("Mdp : Permet d'obtenir les mots de passes via leurs significations", ecran,af_x,af_y + 50,t = True)
                afficher('Fin : Met fin au programme et permet de sauvegarder et crypter les données', ecran,af_x,af_y + 60,t = True)
                afficher('Créer : Permet de créer un mot de passe aléatoirement', ecran,af_x,af_y + 70,t = True)
                afficher('Supprimer : Permet de supprimer un mot de passe et sa signification', ecran,af_x,af_y + 80,t = True)
                afficher("Accueil : Permet de revenir au menu principal où vous pouvez choisir une commande ", ecran,af_x,af_y + 90,t = True )
                afficher("Téléverser : permet de télécharger toutes les données dans un fichier nommée 'contenue_gestionnaire'", ecran,af_x,af_y + 100,t = True)
                home(ecran)
                while home_b() != True:
                    pass
                menu(ecran)
            if grille[a][b] == 2: #liste
                grille_liste = [[0 for _ in range(70)]for _ in range(70)]
                cadre(10,660,"home",32,grille_liste,'home')
                ecran.fill((43, 250, 250))
                
                if len(donnee["donnee"]) == 0:
                    afficher('la liste ne contient pas encore de noms de mots de passes',ecran,af_x,af_y)
                    sleep(2)
                else:
                    t = ''
                    for cle, valeur in donnee["donnee"].items():
                        t +=  decryptage(cle,nb) + ' , '
                    t = t[:-2]
                    afficher(f'Noms des mots de passes = {t}',ecran,af_x,af_y,False,True)
                    t = asci(t)
                    j = cadrage('Noms des mots de passes = ')[1]*10
                    t = t.split()
                    code = 1
                    x2 = 50 
                    y2 = 100
                    m = 1
                    for d in range(len(t)):
                        reste = 0
                        for g in range(len(t[d])):
                            if str(t[d][g]) != ',' and str(t[d][g]) != "[" and str(t[d][g]) != "]" and str(t[d][g]) != "'"  :
                                grille_liste = cadre(x2 + j,y2,(str(t[d][g])),12,grille_liste,code,texte = True)
                                j = j + cadrage(str(t[d][g]),12,i = True)[1]
                                if x2 + j + cadrage(str(t[d][g]),12)[1]*10 >= 690:
                                    reste = x2 + j + cadrage(str(t[d][g]),12)[1]*10 - 690
                                    x2 = 0
                                    j = reste
                                    y2 += 10
                                    reste = 0
                                    
                        j += cadrage(' , ')[1]*10  #15,  cadrage(' , ')[1]*10
                        code += 1
                    home(ecran)
                    u = True
                    while u:
                        f = souris()
                        if grille_liste[f[0]][f[1]] != 0 and  grille_liste[f[0]][f[1]] != 'home' :
                            copier(decryptage(donnee["donnee"][cryptage(t[grille_liste[f[0]][f[1]]-1],nb)],nb))
                            afficher(f'Le mot de passe pour {t[grille_liste[f[0]][f[1]]-1]} as bien été copié dans le presse-papier',ecran,50,350)
                            sleep(2)
                            ecran.fill((43, 250, 250))
                            t = ''
                            for cle, valeur in donnee["donnee"].items():
                                t +=  decryptage(cle,nb) + ' , '
                            t = t[:-2]
                            afficher(f'Noms des mots de passes = {t}',ecran,af_x,af_y,False,True)
                            t = asci(str(t))
                            t = t.split()
                            home(ecran)
                        if grille_liste[f[0]][f[1]] == 'home':
                            break
                            u = False
                menu(ecran)
            if grille[a][b] == 3: #nouveau
                ecran.fill((43, 250, 250))
                home(ecran)
                l = clavier( 'Entrer le nom du nouveau mot de passe à créer : ',ecran,af_x,af_y,False,True)
                if l == True:
                    menu(ecran)
                else:
                    while  cryptage(l,nb)  in donnee["donnee"]: 
                        l = clavier('Nom de mot de passe déjà existant, veuillez en choisir un autre :  ',ecran,af_x,af_y,False,True)
                        if l == True :
                            break
                    l = correct(l)
                    m = clavier( 'Entrer le  mot de passe à créer : ',ecran,af_x,af_y,False,True)
                    if m == True:
                        pass
                    else:
                        m = correct(m)
                        l = cryptage(l,nb)
                        m = cryptage(m,nb)
                        donnee["donnee"][l] = m
                        save(donnee,'Donnee')
                        afficher('Le mot de passe a été crée avec succès',ecran,af_x,af_y)
                        sleep(2)
                    menu(ecran)
                    
            if grille[a][b] == 4: #changer
                ecran.fill((43, 250, 250))
                println('Changer un mot de passe',ecran,af_x - 45,af_y,24)
                println("Changer le nom d'un mot de passe",ecran,af_x - 45 ,af_y + 70,24)
                home(ecran)
                u = True
                while u:
                    f = souris()
                    if grille_changer[f[0]][f[1]] == 'mdp':
                        ecran.fill((43, 250, 250))
                        home(ecran)
                        l = clavier( 'Entrer le nom mot de passe  : ',ecran,af_x,af_y,False,True)
                        if l == True:
                            menu(ecran)     
                        else:
                            while not cryptage(l,nb)  in donnee["donnee"]: 
                                l = clavier( 'Nom de  mot de passe non reconnue , réessayer : ',ecran,af_x,af_y,False,True)
                                if l == True :
                                    break
                            else:
                                if l != True:
                                    l = correct(l)
                                    if cryptage(l,nb) in donnee["donnee"]:
                                        m = clavier( 'Entrer le nouveau mot de passe : ',ecran,af_x,af_y,False,True)
                                        if m == True:
                                            pass  
                                        else:
                                            m = correct(m)
                                            donnee["donnee"][cryptage(l,nb)] = cryptage(m,nb)
                                            save(donnee,'Donnee')
                                            afficher('le mot de passe a été changé avec succès',ecran,af_x,af_y)
                                            sleep(2)
                        menu(ecran)
                        break
                                            
                    if grille_changer[f[0]][f[1]] == 'nom':
                        ecran.fill((43, 250, 250))
                        home(ecran)
                        mdp = ''
                        l = clavier( 'Entrer le nom du mot de passe  : ',ecran,af_x,af_y,False,True)
                        if l != True:
                            while not cryptage(l,nb)  in donnee["donnee"]: 
                                l = clavier( 'Nom de  mot de passe non reconnue , réessayer : ',ecran,af_x,af_y,False,True)
                                if l == True :
                                    break
                            else:
                                if l != True:
                                    l = correct(l)
                                    if cryptage(l,nb) in donnee["donnee"]:
                                        m = clavier( 'Entrer le nouveau nom du mot de passe : ',ecran,af_x,af_y,False,True)
                                        if m == True:
                                            pass  
                                        else:
                                            m = correct(m)
                                            mdp = donnee["donnee"][cryptage(l,nb)] 
                                            del donnee["donnee"][cryptage(l,nb)]
                                            donnee["donnee"][cryptage(m,nb)] = cryptage(mdp,nb)
                                            save(donnee,'Donnee')
                                            afficher('le nom du mot de passe a été changé avec succès',ecran,af_x,af_y)
                                            sleep(2)
                        menu(ecran)
                        break
            if grille[a][b] == 5: #mdp
                t = clavier('Entrer le nom du  mot de passe : ',ecran,af_x,af_y,False,True)
                if t == True:
                    pass
                else:
                    while not cryptage(t,nb) in donnee["donnee"]:
                        t = clavier('Nom de  mot de passe non reconnue , réessayer :  ',ecran,af_x,af_y,False,True )
                        if t == True :
                            break
                    if t != True:
                        t = correct(t)
                        if cryptage(t,nb) in donnee["donnee"]:
                            s = decryptage(str(donnee["donnee"][cryptage(t,nb)]),nb) 
                            copier(s)
                            afficher(f'Le mot de passe pour {t} as été copié dans le presse papier',ecran,af_x,af_y)
                            sleep(2)
                menu(ecran)
            if grille[a][b] == 6:#créer
                l = clavier('Entrer le nom du nouveau mot de passe : ',ecran,af_x,af_y,False,True)
                if l == True:
                    pass
                else:
                    while  cryptage(l,nb) in donnee["donnee"]:
                        l = clavier('Nom de mot de passe déjà existant, veuillez en choisir un autre : ',ecran,af_x,af_y,False,True )
                        if l == True :
                            break
                    if l != True:
                        l = correct(l)
                        z = randint(8,16)
                        mot = ""
                        for k in range(z):
                            d = aléa()
                            mot = mot + d
                        l = cryptage(l,nb)
                        mot = cryptage(mot,nb)
                        donnee["donnee"][l] = mot
                        save(donnee,'Donnee')
                        afficher(f'Nouveau mot de passe crée : {decryptage(mot,nb)}',ecran,af_x,af_y)
                        
                        sleep(2)
                menu(ecran)
                
            if grille[a][b] == 7:#supprimer 
                m = clavier( 'Entrer le nom du mot de passe à supprimer : ',ecran,af_x,af_y,False,True)
                if m == True:
                    pass
                else:
                    while not cryptage(m,nb) in donnee["donnee"]:
                        m = clavier('Nom de  mot de passe non reconnue , réessayer : ',ecran,af_x,af_y,False,True)
                        if m == True:
                            break
                    if m != True:
                        m = correct(m)
                        del donnee["donnee"][cryptage(m,nb)] 
                        save(donnee,'Donnee')
                        afficher(f'le mot de passe a bien été supprimé ',ecran,af_x,af_y)
                        sleep(2)
                menu(ecran)  
                
            if grille[a][b] == 8:#téléverser
                l = clavier('Entrez le mot de passe du gestionnaire : ',ecran,af_x,af_y,False,True)
                if l == True:
                    pass
                else:
                    while correct(cryptage(l,nb)) != decorrect(donnee['mdp']):
                        l = clavier('Mot de passe du gestionnaire erroné , veuiller réessayer : ' ,ecran,af_x,af_y,False,True)
                        if l == True:
                            break
                    if l != True:
                        l = correct(l)
                        for cle, valeur in donnee["donnee"].items():
                            cle = decryptage(cle,nb)
                            valeur = decryptage(str(valeur),nb)
                            Lost_Blue += 'Le mot de passe pour ' + cle + ' est : ' + valeur + ' , '
                        commandement =  Lost_Blue +  'la question est : ' +  decryptage(donnee['question'],nb) + ' , ' + 'la réponse à la question est : ' +  decryptage(donnee['reponse'],nb) 
                        with open('Contenue_gestionnaire.txt', 'w', encoding = 'utf-8') as fichier:
                            fichier.write(commandement)
                        afficher('Mot de passe correct, téléversement terminé',ecran,af_x,af_y)
                        sleep(2)
                menu(ecran)
                
            if grille[a][b] == 9:#Paramètre
                ecran.fill((43, 250, 250))
                println('Changer le mot de passe du gestionnaire',ecran,af_x - 45,af_y,24)
                println("Changer la question en cas d'oublie du mot de passe",ecran,af_x - 45 ,af_y + 70,24)
                println("Réinitialiser les données ",ecran,af_x - 45 ,af_y + 140,24)
                home(ecran)
                u = True
                while u:
                    f = souris()
                    if grille_parametre[f[0]][f[1]] == 'mdp':
                        l = clavier('Entrez le mot de passe actuel du gestionnaire : ',ecran,af_x,af_y,True, h = True)
                        if l == True:
                            pass
                        else:
                            r = 1
                            while cryptage(correct(l),nb) != donnee['mdp']:
                                l = clavier('Mot de passe du gestionnaire erroné , veuiller réessayer : ' ,ecran,af_x,af_y,True)
                                if l == True:
                                    break
                                r += 1
                                if r == 3:
                                    l = clavier((decryptage(decorrect(question)),nb) ,ecran,af_x,af_x)
                                    while cryptage(l,nb) != decorrect(donnee['reponse']):
                                        afficher('Mauvaise réponse',ecran,af_x,af_y)
                                        sleep(2)
                                        l = clavier((decryptage(decorrect(question)),nb) ,ecran,af_x,af_x)
                                        if l == True:
                                            break
                            if l != True:
                                l = clavier('Entrez un nouveau mot de passe pour le gestionnaire: ',ecran,af_x,af_y,True, h = True)
                                if l != True:
                                    mdp2 = clavier('Entrez à nouveau mot de passe pour le gestionnaire: ',ecran,af_x,af_y,True, h = True) 
                                    if l != True:
                                        while l != mdp2:
                                            afficher("La seconde entrée n'est pas la même que la première, réessayer",ecran,af_x,af_y, h = True)
                                            sleep(2)
                                            mdp = clavier('Entrez un nouveau mot de passe pour le gestionnaire: ',ecran,af_x,af_y,True, h = True)
                                            l = clavier('Entrez à nouveau mot de passe pour le gestionnaire: ',ecran,af_x,af_y,True, h = True)
                                        mdp2 = correct(mdp2)
                                        donnee['mdp'] = cryptage(mdp2,nb)
                                        save(donnee,'Donnee')
                                        afficher("Mot de passe modifier avec succès",ecran,af_x,af_y)
                                        sleep(2)
                        menu(ecran)
                        break
                            
                    if grille_parametre[f[0]][f[1]] == 'question' :
                        l = clavier('Entrez le mot de passe actuel du gestionnaire : ',ecran,af_x,af_y,True, h = True)
                        if l == True:
                            pass
                        else:
                            while cryptage(correct(l),nb) != donnee['mdp']:
                                l = clavier('Mot de passe du gestionnaire erroné , veuiller réessayer : ' ,ecran,af_x,af_y,True, h = True)
                                if l == True:
                                    break
                            if l != True:
                                question = clavier('Entrez la nouvelle question, au cas où vous oublierez votre mot de passe  : ',ecran,af_x,af_y, h = True)
                                question = correct(question)
                                if question != True:
                                    reponse =  clavier('Entrez la réponse à cette question : ' , ecran,af_x,af_y, h = True)  
                                    if reponse != True:
                                        l = clavier('Entrez à nouveau  la réponse à cette question : ' , ecran,af_x,af_y, h = True)
                                        if l != True:
                                            while l != reponse:
                                                afficher("La seconde entrée n'est pas la même que la première, réessayer", ecran,af_x,af_y, h = True)
                                                sleep(2)
                                                reponse = clavier('Entrez la réponse à cette question : ' , ecran,af_x,af_y, h = True)
                                                l = clavier('Entrez à nouveau  la réponse à cette question : ' , ecran,af_x,af_y, h = True)
                                                if l == True:
                                                    break
                                        if l != True:
                                            reponse = correct(reponse)
                                            donnee['question'] = cryptage(question,nb)
                                            donnee['reponse'] = cryptage(reponse,nb)
                                            save(donnee,'Donnee')
                                            afficher("La question ainsi que sa réponse ont bien été sauvegarder",ecran,af_x,af_y)
                                            sleep(2)
                        menu(ecran)
                        break
                        
                    if grille_parametre[f[0]][f[1]] == 'donnee' :
                        l = clavier('Entrez le mot de passe actuel du gestionnaire : ',ecran,af_x,af_y,True, h = True)
                        if l == True:
                            pass
                        else:
                            while cryptage(correct(l),nb) != donnee['mdp']:
                                l = clavier('Mot de passe du gestionnaire erroné , veuiller réessayer : ' ,ecran,af_x,af_y,True, h = True)
                                if l == True:
                                    break
                            if l != True:
                                reponse = clavier("Toute les données vont être supprimé, si vous voulez quand même continuer taper 'SUPPRIMER'  : ",ecran,af_x,af_y,False,True)
                                reponse = correct(reponse)
                                if reponse == "SUPPRIMER":
                                    debloquer()
                                    
                                    try:
                                        os.remove("Donnee.json")
                                    
                                    except PermissionError:
                                        bloquer()
                                        debloquer()
                                        os.remove("Donnee.json")
                                    
                                    afficher("Toutes les données ont été supprimées ", ecran,af_x,af_y, h = True)
                                    sleep(4)
                                    pygame.quit()
                                    sys.exit()
                                
                                if reponse == True:
                                    pass
                
                                else:
                                    afficher("Procédure annulé ", ecran,af_x,af_y, h = True)
                                    sleep(2)
                        menu(ecran)
                        break
                        
                    if grille[f[0]][f[1]] == 'home': #or l == True or question == True or reponse == True:
                        menu(ecran)
                        break
                        
                        
            
                


# In[ ]:





# In[ ]:




