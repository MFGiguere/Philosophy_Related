import re, pprint, os, pyperclip, json

#SECTION 1: There are different compile depending on citation styles. Right now, only french APA style is done. It might be useful for other style, but will need to be tweaked. 
#This is years and author. It can scan organisations, multiple author and collaborators.
#It requires author name to be at least 3 characters to prevent false positive (for ex. a sentence starting with 'In 1999,'. 
S = '(?:\s|\n|\(|;|,)+'
author = '(?:[A-Z][A-Za-z\'\`-][A-Za-z\'\`-]+)'
etal = '(?:[\s\n](?:et|and|&)[\s\n](?:al.|coll.|'+author+'))?'
annee = '(?:[0-9]{4}[a-z]*)'
page = '(?:p.\s[0-9]+(?:-[0-9])?)?'
year = '(?:'+S+annee+page+')+'
NewReg = '('+author+etal+year+')'


#Section 2: This part splits authors and dates. 
#Here, authors are separated from dates for 2 reasons. First, to handle some keywords like ''Ibid'' which means ''last author''.
#Second, to make it possible to group data by authors (if needed). 
#This Regex are, in order, for dates, exceptions and authors. 
DateReg = re.compile(annee)
AuthorReg = re.compile(author+etal)

#Section 3: Now is time to group everything into a single table. 
Tableau = {}    #table that will contain final product
def scane():
    for i in range(len(Texte)): #this splits authors and dates for when there are one author with multiple dates
        author = re.match(AuthorReg, Texte[i]).group()
        date = DateReg.findall(str(Texte[i]))
        z=1
        
    #This part is for exceptions, like Ibid.  more could be added if needed. 
        while str(author) == 'Ibid': #This go scan the last name that isn't ibid which will be the author. 
            author = re.match(AuthorReg, Texte[i-z]).group()
            z=z+1

    #   quand plusieurs dates à ajouter
        for annee in date:
            duo = str(author)+', '+str(annee)

    #pour insérer au tableau
            if str(duo) not in Tableau.keys(): #si pas dans le tableau, nouvelle entrée
                Tableau.setdefault(str(duo), 0)
            Tableau[str(duo)] = Tableau[str(duo)] + 1 #rajoute un à l'entrée crée avant 

#section 5
#QOL commands. It makes the script easy and fun to use!
count = 1
print('Enjoy this script! Be aware that some exceptions are not handled. See script for more details.')
while True:
    print('Copy (CTRL+C) the text you want to compile references for. The program will read your copied text automatically. Type OK when you are ready to scan.')
    x = input()
    #Typing ok will start the scan. If something else is typed, intro message will just restart. 
    if x == str('OK'):
        copie = pyperclip.paste()
        Texte = re.findall(NewReg, copie)
        scane()
        pprint.pprint(Tableau)
    print('Do you want to save text? Press Y to save or N to skip this step')

    #Typing Y will save using first Author as name. 
    xy = input()
    if xy == str('Y'):
        name = 'save_'+str(Texte[0:1])+str(count)+'.txt'
        with open(name, 'w') as savefile:
            for key, value in Tableau.items():
                savefile.write('%s:%s\n'%(key, value))
        print('Datas as been saved as '+name)
        savefile.close
    if xy == str('N'):
        print('Restarting loop!')
    #this clear table for multiple uses of the script and also add a number for next save file. 
    Tableau.clear()
    count = count + 1
          
