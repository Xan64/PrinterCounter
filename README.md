# PrinterCounter
Designed to generate a pdf file with all the data from Konica Minolta Printers

Pour faire fonctionner printer_counter
**************************************

* Créer un dossier

* Créer deux dossiers (le nom doit être exactement celui là sinon, ça ne fonctionnera pas) :
- fichier_input
- fichier_output

* Dans le dossier fichier_input, mettre les fichiers récupérés sur le copieur

* Les PDFs sont générés dans le dossier fichier_output


********************
* Pour modifier/recompiler, il faut installer
- Python 3.7 au minimum
- Atom (IDE) ou un autre IDE

* Avec le module pip de Python, il faut installer :
- la bibliothèque FPDF2 (https://pypi.org/project/fpdf2/) pour la génération de PDF
- la bibliothèque auto-py-to-exe (https://pypi.org/project/auto-py-to-exe/) optionnel pour générer le fichier exécutable
