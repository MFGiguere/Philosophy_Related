#This is one of the first script I did while learning Python.
#Its goal is to search all files in a folder for a specific concept.
#In my case, I used it to look in all Szasz' monography for references to Virchow.
#I found that Szasz started citing Virchow in 1976 but it's between 2000 and 2010 that we find the highest number of references to Virchow. 

#This is all the imports I used while learning and working of this script.
import re
import os
import pprint
import webbrowser
import PyPDF2 
import pikepdf
import pytesseract
import tempfile
from pdf2image import convert_from_path

#This makes a path to folder. This implies that (1) all files are PDFs and (2) that year date is written in filename. 
path = 'PATH\\FOLDER'
os.chdir(path)
Tableau = {}

#1 This function was a try to convert empty PDF files to text using OCR. It didn't work and I used Acrobat Reader for my project instead. 
def ocrdoc(somePDF):
    #test pdf 5 pages

    pdfFileObj = open(somePDF, 'rb')#article to test
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

    # Store all the pages of the PDF in a variable
    pages = convert_from_path(somePDF, int(pdfReader.numPages))

    for page in pages:
        # Increment the counter to update filename
        with tempfile.TemporaryDirectory() as path:
            images = convert_from_path(somepage, poppler_path = SOME_PATH)
        Contenu+str(page) == str(pytesseract.image_to_string(images))
        image_counter = image_counter + 1
        print(Contenu+strpage)

#2 Second step is to look in the files if the concept is used. 
#Two regex are needed. For first one, any concept could be used. 
VirchowReg = re.compile('[V-v]irchow') #This is the concept I was looking for. 
AnneeReg = re.compile('\d\d\d\d') #This is to get year in file names. 


#This was an attempt to read files implying I was able to webscrapt them. I wasn't able to webscrapt and didn't use this function. 
def lecture():
   for i in (1, 2):
       #To read doc using Szasz#.txt
       Texte = (path + '\\' + 'Szasz' + str(i) + '.txt') 
       Text = open(Texte)
       TC = Text.read()
    print(TC)

#This read PDF files which I got manually during my 3 years research on the subject. 
def lecturePDF():

    #Defines variable and creates a list of all files in folder. 
    global date
    global Tableau
    listof = []
    for root, dirs, files in os.walk(path):
        for file in files:
            listof.append(os.path.join(root, file))

    #this loop trough all fil;es
    for filename in listof:
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

        #This 'for' loop search the number of 'concept' in each page of each file. 
        for pageNum in range(0, int(pdfReader.numPages)):
            pageObj = pdfReader.getPage(int(pageNum))
            try: 
                Contenu = pageObj.extractText()
            except ValueError:
                print('an error occured in '+filename+'on page'+str(pageNum))
            #script for empty pages I wanted to add in case there were no text in the PDF file, to ocr it. Didn't work so I abandoned it. 
            #if len(Contenu)==0:
                #ocrpage(Contenu)
            VirchowFind = VirchowReg.findall(Contenu)
            Annee = AnneeReg.findall(filename)

        #For each concept, add one to table. 
            if str(Annee) not in Tableau.keys(): #new entry when not already in table
                Tableau.setdefault(str(Annee), 0)
            for i in range(len(VirchowFind)):
                Tableau[str(Annee)] = Tableau[str(Annee)] + 1 #add one to newly created entry
        print(filename)

#This function is to calculate the number of texts written in a single year. So, if there were 5 texts written in 1995, it'll output a dict with 1995:5. 
def nbannee(): #for nb of texts by year
    global date
    global Tableau #this actually the same variable but it's not a problem when both functions aren't used at the same time. 
    listof = []
    for root, dirs, files in os.walk(path):
        for file in files:
            listof.append(os.path.join(root, file))
            
    for filename in listof:
        Annee = AnneeReg.findall(filename)
        if str(Annee) not in Tableau.keys(): #if not in dict already, it will create new entry. 
            Tableau.setdefault(str(Annee), 0)
        Tableau[str(Annee)] = Tableau[str(Annee)] + 1
    

#5 This part is to use functions I need. 
#lecturePDF()
#nbannee()
#pprint.pprint(Tableau)

