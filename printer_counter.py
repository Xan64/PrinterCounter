from os import system
from ansi_colors import colors

import os, time
import traceback
import sys

from fpdf import FPDF



# Classe User, contenant toutes les données d'impression
class compte_user():
    """__init__() functions as the class constructor"""
    def __init__(self):
        self.account_name = ''
        self.total_recto_verso = ''
        self.total_cout_recto_verso = ''
        self.total_compteur_papier = ''
        self.total_nb_feuilles_impr = ''
        self.compteur_total_2_en_1 = ''
        self.compteur_total_4_en_1 = ''
        self.compteur_total_autre = ''
        self.cout_total_impression = ''
        # CC = Compteur Copie ; CI = Compteur Impression ; CT = Compteur Total ; CS = Compteur Scanner
        # N = Noir ; FC = Full Color ; 1C = Single Color ; 2C = 2-Color ; MB = Monochromie + Bichromie
        # T = Total ; GF = Grand Format ; CP = Compteur Papier
        # COMPTEUR COPIES
        self.CC_T_T = ''
        self.CC_T_GF = ''
        self.CC_T_CP = ''
        self.CC_N_T = ''
        self.CC_N_GF = ''
        self.CC_N_CP = ''
        self.CC_FC_T = ''
        self.CC_FC_GF = ''
        self.CC_FC_CP = ''
        self.CC_1C_T = ''
        self.CC_1C_GF = ''
        self.CC_2C_T = ''
        self.CC_2C_GF = ''
        self.CC_MB_CP = ''
        # COMPTEUR IMPRESSIONS
        self.CI_T_T = ''
        self.CI_T_GF = ''
        self.CI_T_CP = ''
        self.CI_N_T = ''
        self.CI_N_GF = ''
        self.CI_N_CP = ''
        self.CI_FC_T = ''
        self.CI_FC_GF = ''
        self.CI_FC_CP = ''
        self.CI_2C_T = ''
        self.CI_2C_GF = ''
        self.CI_2C_CP = ''
        self.CI_MB_T = ''
        self.CI_MB_GF = ''
        self.CI_MB_CP = ''
        # COMPTEUR TOTAL
        self.CT_T_T = ''
        self.CT_T_GF = ''
        self.CT_T_CP = ''
        self.CT_N_T = ''
        self.CT_N_GF = ''
        self.CT_N_CP = ''
        self.CT_FC_T = ''
        self.CT_FC_GF = ''
        self.CT_FC_CP = ''
        self.CT_1C_T = ''
        self.CT_1C_GF = ''
        self.CT_1C_CP = ''
        self.CT_2C_T = ''
        self.CT_2C_GF = ''
        self.CT_2C_CP = ''
        self.CT_MB_T = ''
        self.CT_MB_GF = ''
        self.CT_MB_CP = ''
        # COMPTEUR SCANNER
        # N = Numérisations ; IT = Impression Total ; IC = Impression Couleur ; IN = Impression Noir
        self.CS_N_T = ''
        self.CS_N_GF = ''
        self.CS_IT_T = ''
        self.CS_IT_GF = ''
        self.CS_IT_CP = ''
        self.CS_IC_T = ''
        self.CS_IC_GF = ''
        self.CS_IC_CP = ''
        self.CS_IN_T = ''
        self.CS_IN_GF = ''
        self.CS_IN_CP = ''

    def print_Compteur_Global(self):
        print(colors.reset +"Compte " + colors.fg.yellow + self.account_name )
        print(colors.reset +"Total Recto Verso : " + colors.fg.lightcyan + self.total_recto_verso)
        print(colors.reset +"Coût impression recto verso : " + colors.fg.lightcyan + self.total_cout_recto_verso)
        print(colors.reset +"Compteur Papier : " + colors.fg.lightcyan + self.total_compteur_papier)
        print(colors.reset +"Compteur Nbre. feuilles imprim. : " + colors.fg.lightcyan + self.total_nb_feuilles_impr)
        print(colors.reset +"Compteur total 2 en 1 : " + colors.fg.lightcyan + self.compteur_total_2_en_1)
        print(colors.reset +"Compteur total 4 en 1 : " + colors.fg.lightcyan + self.compteur_total_4_en_1)
        print(colors.reset +"Compteur total Autre : " + colors.fg.lightcyan + self.compteur_total_autre)
        print(colors.reset +"Coût d'impression total : " + colors.fg.lightcyan + self.cout_total_impression)
        print(colors.reset)

    def print_compteur_copies(self):
        print ("Compteur de copies")
        print("+--------------------+----------+----------+----------+")
        print("+  TOTAL             + {0}{2:8d}{1} + {0}{3:8d}{1} + {0}{4:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CC_T_T),int(self.CC_T_GF),int(self.CC_T_CP)))
        print("+--------------------+----------+----------+----------+")
        print("+  Noir              + {0}{2:8d}{1} + {0}{3:8d}{1} + {0}{4:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CC_N_T),int(self.CC_N_GF),int(self.CC_N_CP)))
        print("+--------------------+----------+----------+----------+")
        print("+  Full Color        + {0}{2:8d}{1} + {0}{3:8d}{1} + {0}{4:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CC_FC_T),int(self.CC_FC_GF),int(self.CC_FC_CP)))
        print("+--------------------+----------+----------+----------+")
        print("+  Single Color      + {0}{2:8d}{1} + {0}{3:8d}{1} +        - +".format(colors.fg.lightcyan,colors.reset,int(self.CC_1C_T),int(self.CC_1C_GF)))
        print("+--------------------+----------+----------+----------+")
        print("+  2 Color           + {0}{2:8d}{1} + {0}{3:8d}{1} +        - +".format(colors.fg.lightcyan,colors.reset,int(self.CC_2C_T),int(self.CC_2C_GF)))
        print("+--------------------+----------+----------+----------+")
        print("+  Mono+Bichromie    +        - +        - + {0}{2:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CC_MB_CP)))
        print("+--------------------+----------+----------+----------+")

    def print_compteur_impression(self):
        print ("Compteur d'impression")
        print("+--------------------+----------+----------+----------+")
        print("+  TOTAL             + {0}{2:8d}{1} + {0}{3:8d}{1} + {0}{4:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CI_T_T),int(self.CI_T_GF),int(self.CI_T_CP)))
        print("+--------------------+----------+----------+----------+")
        print("+  Noir              + {0}{2:8d}{1} + {0}{3:8d}{1} + {0}{4:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CI_N_T),int(self.CI_N_GF),int(self.CI_N_CP)))
        print("+--------------------+----------+----------+----------+")
        print("+  Full Color        + {0}{2:8d}{1} + {0}{3:8d}{1} + {0}{4:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CI_FC_T),int(self.CI_FC_GF),int(self.CI_FC_CP)))
        print("+--------------------+----------+----------+----------+")
        print("+  2 Color           + {0}{2:8d}{1} + {0}{3:8d}{1} +        - +".format(colors.fg.lightcyan,colors.reset,int(self.CI_2C_T),int(self.CI_2C_GF)))
        print("+--------------------+----------+----------+----------+")
        print("+  Mono+Bichromie    +        - +        - + {0}{2:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CI_MB_CP)))
        print("+--------------------+----------+----------+----------+")

    def print_compteur_total(self):
        print ("Compteur Total")
        print("+--------------------+----------+----------+----------+")
        print("+  TOTAL             + {0}{2:8d}{1} + {0}{3:8d}{1} +        - +".format(colors.fg.lightcyan,colors.reset,int(self.CT_T_T),int(self.CT_T_GF)))
        print("+--------------------+----------+----------+----------+")
        print("+  Noir              + {0}{2:8d}{1} + {0}{3:8d}{1} + {0}{4:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CT_N_T),int(self.CT_N_GF),int(self.CT_N_CP)))
        print("+--------------------+----------+----------+----------+")
        print("+  Full Color        + {0}{2:8d}{1} + {0}{3:8d}{1} + {0}{4:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CT_FC_T),int(self.CT_FC_GF),int(self.CT_FC_CP)))
        print("+--------------------+----------+----------+----------+")
        print("+  2 Color           + {0}{2:8d}{1} + {0}{3:8d}{1} +        - +".format(colors.fg.lightcyan,colors.reset,int(self.CT_2C_T),int(self.CT_2C_GF)))
        print("+--------------------+----------+----------+----------+")
        print("+  Mono+Bichromie    +        - +        - + {0}{2:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CT_MB_CP)))
        print("+--------------------+----------+----------+----------+")

    def print_compteur_scanner(self):
        print ("Compteur Scanner")
        print("+---------------------+----------+----------+----------+")
        print("+  Numérisations      + {0}{2:8d}{1} + {0}{3:8d}{1} +        - +".format(colors.fg.lightcyan,colors.reset,int(self.CS_N_T),int(self.CS_N_GF)))
        print("+---------------------+----------+----------+----------+")
        print("+  Impression Total   + {0}{2:8d}{1} + {0}{3:8d}{1} + {0}{4:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CS_IT_T),int(self.CS_IT_GF),int(self.CS_IT_CP)))
        print("+---------------------+----------+----------+----------+")
        print("+  Impression Couleur + {0}{2:8d}{1} + {0}{3:8d}{1} + {0}{4:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CS_IC_T),int(self.CS_IC_GF),int(self.CS_IC_CP)))
        print("+---------------------+----------+----------+----------+")
        print("+  Impression Noir    + {0}{2:8d}{1} + {0}{3:8d}{1} + {0}{4:8d}{1} +".format(colors.fg.lightcyan,colors.reset,int(self.CS_IN_T),int(self.CS_IN_GF),int(self.CS_IN_CP)))
        print("+---------------------+----------+----------+----------+")


    def print_everything(self):
        '''Output des données de l'user dans la console'''
        self.print_Compteur_Global()
        print(" ")
        self.print_compteur_copies()
        print(" ")
        self.print_compteur_impression()
        print(" ")
        self.print_compteur_total()
        print(" ")
        self.print_compteur_scanner()

    def csv_output(self):
        '''retourne toutes les données de l'user en CSV'''
        csv_output_tmp = ''
        csv_output_tmp = self.account_name + ";" + self.total_recto_verso + ";" + self.total_cout_recto_verso + ";" + self.total_compteur_papier + ";" + self.total_nb_feuilles_impr + ";"
        csv_output_tmp = csv_output_tmp + self.compteur_total_2_en_1 + ";" + self.compteur_total_4_en_1 + ";" + self.compteur_total_autre + ";" + self.cout_total_impression + ";"
        csv_output_tmp = csv_output_tmp + self.CC_T_T + ";" + self.CC_T_GF + ";" + self.CC_T_CP + ";" + self.CC_N_T + ";" + self.CC_N_GF + ";" + self.CC_N_CP+ ";" + self.CC_FC_T+ ";" + self.CC_FC_GF+ ";" + self.CC_FC_CP+ ";" + self.CC_1C_T+ ";" + self.CC_1C_GF + ";" + self.CC_2C_T+ ";" + self.CC_2C_GF + ";" + self.CC_MB_CP + ";"
        csv_output_tmp = csv_output_tmp + self.CI_T_T + ";" + self.CI_T_GF + ";" + self.CI_T_CP + ";" + self.CI_N_T + ";" + self.CI_N_GF + ";" + self.CI_N_CP + ";" + self.CI_FC_T + ";" + self.CI_FC_GF + ";" + self.CI_FC_CP + ";" + self.CI_2C_T + ";" + self.CI_2C_GF + ";" + self.CI_MB_CP + ";"
        csv_output_tmp = csv_output_tmp + self.CT_T_T + ";" + self.CT_T_GF + ";" + self.CT_N_T + ";" + self.CT_N_GF + ";" + self.CT_N_CP + ";" + self.CT_FC_T + ";" + self.CT_FC_GF + ";" + self.CT_FC_CP + ";" + self.CT_1C_T + ";" + self.CT_1C_GF + ";" + self.CT_2C_T + ";" + self.CT_2C_GF + ";" + self.CT_MB_CP  + ";"
        csv_output_tmp = csv_output_tmp + self.CS_N_T + ";" + self.CS_N_GF + ";" + self.CS_IT_T + ";" + self.CS_IT_GF + ";" + self.CS_IT_CP + ";" + self.CS_IC_T + ";" + self.CS_IC_GF + ";" + self.CS_IC_CP + ";" + self.CS_IN_T + ";" + self.CS_IN_GF + ";" + self.CS_IN_CP + ";\n"
        return csv_output_tmp


    def make_pdf(self):
        ''' Créée une page PDF avec les données représentées en tableau'''
        pdf.add_page(orientation = 'L', format = 'A4')
        # Compteur d'impression global
        pdf.set_xy(20,10)
        pdf.set_fill_color(245, 235, 162)
        pdf.set_font('Arial', 'B', 15)
        pdf.cell(75,8,"Compteur d'impression", border = 0, ln = 2, align = 'C', fill = False)
        pdf.set_font('Times', 'B', 8)
        pdf.cell(50,8,"Total Recto Verso", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,8,"Cout des impression recto verso", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,8,"Compteur Papier", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,8,"Compteur Nb Feuilles imprim.", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(25,32,"Compteur Total", border = 1, ln = 0, align = 'C', fill = True)
        pdf.cell(25,8,"2 en 1", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(25,8,"4 en 1", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(25,8,"Autre", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(25,8,"Cout total", border = 1, ln = 2, align = 'C', fill = True)
        pdf.set_xy(70,18)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25,8,self.total_recto_verso, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,8,self.total_cout_recto_verso, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,8,self.total_compteur_papier, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,8,self.total_nb_feuilles_impr, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,8,self.compteur_total_2_en_1, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,8,self.compteur_total_4_en_1, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,8,self.compteur_total_autre, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,8,self.cout_total_impression, border = 1, ln = 2, align = 'C', fill = False)

        # Compteur de copies
        pdf.set_font('Arial', 'B', 15)
        pdf.set_xy(20,90)
        pdf.set_fill_color(245, 235, 162)
        pdf.cell(125,8,"Compteur de copies", border = 0, ln = 2, align = 'C', fill = False)
        pdf.cell(50,8, border = 1, ln =2,fill = True)
        pdf.set_font('Times', 'B', 8)
        pdf.cell(50,5,"Total", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Noir", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Full Color", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Single Color", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"2 Color", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Monochrome + Bichromie ", border = 1, ln = 2, align = 'C', fill = True)
        pdf.set_xy(70,98)
        pdf.cell(25,8, "Total", border = 1, ln = 2, align = 'C', fill = True)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25,5,self.CC_T_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CC_N_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CC_FC_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CC_1C_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CC_2C_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,"-", border = 1, ln = 2, align = 'C', fill = False)
        pdf.set_font('Times', 'B', 8)
        pdf.set_xy(95,98)
        pdf.cell(25,8, "Grand Format", border = 1, ln = 2,align = 'C', fill = True)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25,5,self.CC_T_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CC_N_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CC_FC_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CC_1C_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CC_2C_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,"-", border = 1, ln = 2, align = 'C', fill = False)
        pdf.set_font('Times', 'B', 8)
        pdf.set_xy(120,98)
        pdf.cell(25,8, "Compteur Papier", border = 1, ln = 2,align = 'C', fill = True)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25,5,self.CC_T_CP, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CC_N_CP, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CC_FC_CP, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,"-", border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,"-", border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CC_MB_CP, border = 1, ln = 2, align = 'C', fill = False)

        # Compteur d'impression'
        pdf.set_font('Arial', 'B', 15)
        pdf.set_xy(20,142)
        pdf.set_fill_color(245, 235, 162)
        pdf.cell(125,8,"Compteur d'impression", border = 0, ln = 2, align = 'C', fill = False)
        pdf.cell(50,8, border = 1, ln =2,fill = True)
        pdf.set_font('Times', 'B', 8)
        pdf.cell(50,5,"Total", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Noir", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Full Color", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"2 Color", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Monochrome + Bichromie ", border = 1, ln = 2, align = 'C', fill = True)
        pdf.set_xy(70,150)
        pdf.cell(25,8, "Total", border = 1, ln = 2, align = 'C', fill = True)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25,5,self.CI_T_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CI_N_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CI_FC_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CI_2C_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,"-", border = 1, ln = 2, align = 'C', fill = False)
        pdf.set_font('Times', 'B', 8)
        pdf.set_xy(95,150)
        pdf.cell(25,8, "Grand Format", border = 1, ln = 2,align = 'C', fill = True)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25,5,self.CI_T_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CI_N_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CI_FC_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CI_2C_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,"-", border = 1, ln = 2, align = 'C', fill = False)
        pdf.set_font('Times', 'B', 8)
        pdf.set_xy(120,150)
        pdf.cell(25,8, "Compteur Papier", border = 1, ln = 2,align = 'C', fill = True)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25,5,self.CI_T_CP, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CI_N_CP, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CI_FC_CP, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,"-", border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CI_MB_CP, border = 1, ln = 2, align = 'C', fill = False)

        # Total
        pdf.set_font('Arial', 'B', 15)
        pdf.set_xy(160,142)
        pdf.set_fill_color(245, 235, 162)
        pdf.cell(125,8,"Total", border = 0, ln = 2, align = 'C', fill = False)
        pdf.cell(50,8, border = 1, ln =2,fill = True)
        pdf.set_font('Times', 'B', 8)
        pdf.cell(50,5,"Total", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Noir", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Full Color", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Single Color", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"2 Color", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Monochrome + Bichromie ", border = 1, ln = 2, align = 'C', fill = True)
        pdf.set_xy(210,150)
        pdf.cell(25,8, "Total", border = 1, ln = 2, align = 'C', fill = True)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25,5,self.CT_T_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CT_N_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CT_FC_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CT_1C_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CT_2C_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,"-", border = 1, ln = 2, align = 'C', fill = False)
        pdf.set_font('Times', 'B', 8)
        pdf.set_xy(235,150)
        pdf.cell(25,8, "Grand Format", border = 1, ln = 2,align = 'C', fill = True)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25,5,self.CT_T_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CT_N_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CT_FC_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CT_1C_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CT_2C_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,"-", border = 1, ln = 2, align = 'C', fill = False)
        pdf.set_font('Times', 'B', 8)
        pdf.set_xy(260,150)
        pdf.cell(25,8, "Compteur Papier", border = 1, ln = 2,align = 'C', fill = True)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25,5,"-", border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CT_N_CP, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CT_FC_CP, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,"-", border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,"-", border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CT_MB_CP, border = 1, ln = 2, align = 'C', fill = False)


        # Compteur Scanner
        pdf.set_font('Arial', 'B', 15)
        pdf.set_xy(160,90)
        pdf.cell(125,8,"Compteur Scanner", border = 0, ln = 2, align = 'C', fill = False)
        pdf.set_fill_color(245, 235, 162)
        pdf.cell(50,8, border = 1, ln =2,fill = True)
        pdf.set_font('Times', 'B', 8)
        pdf.cell(50,5,"Numérisations", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Impression Total", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Impression Couleur", border = 1, ln = 2, align = 'C', fill = True)
        pdf.cell(50,5,"Impression Noir", border = 1, ln = 2, align = 'C', fill = True)
        pdf.set_xy(210,98)
        pdf.cell(25,8, "Total", border = 1, ln = 2, align = 'C', fill = True)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25,5,self.CS_N_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CS_IT_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CS_IC_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CS_IN_T, border = 1, ln = 2, align = 'C', fill = False)
        pdf.set_font('Times', 'B', 8)
        pdf.set_xy(235,98)
        pdf.cell(25,8, "Grand Format", border = 1, ln = 2,align = 'C', fill = True)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25,5,self.CS_N_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CS_IT_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CS_IC_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CS_IN_GF, border = 1, ln = 2, align = 'C', fill = False)
        pdf.set_font('Times', 'B', 8)
        pdf.set_xy(260,98)
        pdf.cell(25,8, "Compteur Papier", border = 1, ln = 2,align = 'C', fill = True)
        pdf.set_font('Arial', '', 8)
        pdf.cell(25,5,"-", border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CS_IT_CP, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CS_IC_CP, border = 1, ln = 2, align = 'C', fill = False)
        pdf.cell(25,5,self.CS_IN_CP , border = 1, ln = 2, align = 'C', fill = False)


        # Info compte et école
        pdf.set_font('Arial', 'B', 20)
        pdf.text(160,15, NOM_ECOLE + " - " + self.account_name)
        date_tmp = translate_time(time.ctime(os.path.getctime("./fichier_input/"+file)))
        pdf.set_font('Arial', '', 10)
        pdf.text(160,20,date_tmp)


# INITIALISATION DES TABLEAUX ET VARIABLES
# Tableau de lignes pour lire le fichier
lines = []
# on crée un tableau vide
users = []
# initialisation du compteur
count = 0

# on efface l'écran
system("cls")


# Récupérer le nom du compte
def get_account_name(line_number):
    '''Retourne le nom du compte.
    Il faut passer le numéro de ligne ou on trouve <td>Nom</td> en paramètre'''
    line_tmp = lines[line_number+1]
    line_tmp = line_tmp.replace('<td>','')
    line_tmp = line_tmp.replace('</td>','')
    # on supprime le dernier caractère (retour chariot)
    line_tmp = line_tmp[:-1]
    return line_tmp

# Récupérer la donnée quand la ligne est de la forme : <td width="130px"><div align="right">donnée<br>
def get_special_line_type_1(line_number):
    '''Retourne la données contenue dans la ligne passée en paramètre.
    <td width="130px"><div align="right">donnée<br>'''
    line_tmp = lines[line_number]
    line_tmp = line_tmp.replace('<td width="130px"><div align="right">','')
    line_tmp = line_tmp.replace('<br>','')
    # on supprime le dernier caractère (retour chariot)
    line_tmp = line_tmp[:-1]
    return line_tmp

# Récupérer la donnée quand la ligne est de la forme : <td><div align="right">donnée<br>
def get_special_line_type_2(line_number):
    '''Retourne la données contenue dans la ligne passée en paramètre.
    <td><div align="right">donnée<br>'''
    line_tmp = lines[line_number]
    line_tmp = line_tmp.replace('<td><div align="right">','')
    line_tmp = line_tmp.replace('<br>','')
    # on supprime le dernier caractère (retour chariot)
    line_tmp = line_tmp[:-1]
    return line_tmp

# boucle dans le fichier, on compte les instances de "Nom" (=nb de comptes)
# puis on va chercher la valeur dans les lignes suivantes
# c'est toujours la même structure
# cf fichier annexe_compte_ligne.txt
# il faut récupérer la donnée suivant le type de format de ligne
def get_user_data_from_file():
    '''Récupère toutes les données d'un compte
    et les rajouter à un user dans la liste'''
    for i in range (0,len(lines)):
        if '<th>Nom</th>' in lines[i]:
            user_tmp = compte_user()
            user_tmp.account_name=(get_account_name(i))
            # print(user_tmp.account_name)
            user_tmp.total_recto_verso=(get_special_line_type_1(i+17))
            user_tmp.total_cout_recto_verso=(get_special_line_type_1(i+22))
            user_tmp.total_compteur_papier=(get_special_line_type_1(i+27))
            user_tmp.total_nb_feuilles_impr=(get_special_line_type_1(i+32))

            user_tmp.compteur_total_2_en_1 = (get_special_line_type_1(i+40))
            user_tmp.compteur_total_4_en_1 = (get_special_line_type_1(i+45))
            user_tmp.compteur_total_autre = (get_special_line_type_1(i+50))
            user_tmp.cout_total_impression = (get_special_line_type_1(i+55))

            # COMPTEUR COPIES
            user_tmp.CC_T_T = (get_special_line_type_2(i+69))
            user_tmp.CC_T_GF = (get_special_line_type_2(i+71))
            user_tmp.CC_T_CP = (get_special_line_type_2(i+73))
            user_tmp.CC_N_T = (get_special_line_type_2(i+78))
            user_tmp.CC_N_GF = (get_special_line_type_2(i+80))
            user_tmp.CC_N_CP = (get_special_line_type_2(i+82))
            user_tmp.CC_FC_T = (get_special_line_type_2(i+87))
            user_tmp.CC_FC_GF = (get_special_line_type_2(i+89))
            user_tmp.CC_FC_CP = (get_special_line_type_2(i+91))
            user_tmp.CC_1C_T = (get_special_line_type_2(i+96))
            user_tmp.CC_1C_GF = (get_special_line_type_2(i+98))
            user_tmp.CC_2C_T = (get_special_line_type_2(i+104))
            user_tmp.CC_2C_GF = (get_special_line_type_2(i+106))
            user_tmp.CC_MB_CP = (get_special_line_type_2(i+114))

            # COMPTEUR
            user_tmp.CI_T_T = (get_special_line_type_2(i+128))
            user_tmp.CI_T_GF = (get_special_line_type_2(i+130))
            user_tmp.CI_T_CP = (get_special_line_type_2(i+132))
            user_tmp.CI_N_T = (get_special_line_type_2(i+137))
            user_tmp.CI_N_GF = (get_special_line_type_2(i+139))
            user_tmp.CI_N_CP = (get_special_line_type_2(i+141))
            user_tmp.CI_FC_T = (get_special_line_type_2(i+146))
            user_tmp.CI_FC_GF = (get_special_line_type_2(i+148))
            user_tmp.CI_FC_CP = (get_special_line_type_2(i+150))
            user_tmp.CI_2C_T = (get_special_line_type_2(i+155))
            user_tmp.CI_2C_GF = (get_special_line_type_2(i+157))
            user_tmp.CI_MB_CP = (get_special_line_type_2(i+165))

            # COMPTEUR TOTAL
            user_tmp.CT_T_T = (get_special_line_type_2(i+179))
            user_tmp.CT_T_GF = (get_special_line_type_2(i+181))
            user_tmp.CT_N_T = (get_special_line_type_2(i+187))
            user_tmp.CT_N_GF = (get_special_line_type_2(i+189))
            user_tmp.CT_N_CP = (get_special_line_type_2(i+191))
            user_tmp.CT_FC_T = (get_special_line_type_2(i+196))
            user_tmp.CT_FC_GF = (get_special_line_type_2(i+198))
            user_tmp.CT_FC_CP = (get_special_line_type_2(i+200))
            user_tmp.CT_1C_T = (get_special_line_type_2(i+205))
            user_tmp.CT_1C_GF = (get_special_line_type_2(i+207))
            user_tmp.CT_2C_T = (get_special_line_type_2(i+213))
            user_tmp.CT_2C_GF = (get_special_line_type_2(i+215))
            user_tmp.CT_MB_CP = (get_special_line_type_2(i+223))

            # COMPTEUR SCANNER
            user_tmp.CS_N_T = (get_special_line_type_2(i+237))
            user_tmp.CS_N_GF = (get_special_line_type_2(i+239))
            user_tmp.CS_IT_T = (get_special_line_type_2(i+245))
            user_tmp.CS_IT_GF = (get_special_line_type_2(i+247))
            user_tmp.CS_IT_CP = (get_special_line_type_2(i+249))
            user_tmp.CS_IC_T = (get_special_line_type_2(i+254))
            user_tmp.CS_IC_GF = (get_special_line_type_2(i+256))
            user_tmp.CS_IC_CP = (get_special_line_type_2(i+258))
            user_tmp.CS_IN_T = (get_special_line_type_2(i+263))
            user_tmp.CS_IN_GF = (get_special_line_type_2(i+265))
            user_tmp.CS_IN_CP = (get_special_line_type_2(i+267))

            users.append(user_tmp) #ajout d'un élement au tableau

# Traduction du temps de ctime
def translate_time(time_tmp):
    ''' Traduit un ctime passé en paramètre
    en date en français Jour, Numéro du jour, Mois, Année, Heure
    '''
    time_element = time_tmp.split(" ")
    # Traduction du jour
    if time_element[0] == "Mon":
        time_element[0] = "Lundi"
    if time_element[0] == "Tue":
        time_element[0] = "Mardi"
    if time_element[0] == "Wed":
        time_element[0] = "Mercredi"
    if time_element[0] == "Thu":
        time_element[0] = "Jeudi"
    if time_element[0] == "Fri":
        time_element[0] = "Vendredi"
    if time_element[0] == "Sat":
        time_element[0] = "Samedi"
    if time_element[0] == "Sun":
        time_element[0] = "Dimanche"
    # Traduction du mois
    if time_element[1] == "Jan":
        time_element[1] = "Janvier"
    if time_element[1] == "Feb":
        time_element[1] = "Février"
    if time_element[1] == "Mar":
        time_element[1] = "Mars"
    if time_element[1] == "Apr":
        time_element[1] = "Avril"
    if time_element[1] == "May":
        time_element[1] = "Mai"
    if time_element[1] == "Jun":
        time_element[1] = "Juin"
    if time_element[1] == "Jul":
        time_element[1] = "Juillet"
    if time_element[1] == "Aug":
        time_element[1] = "Août"
    if time_element[1] == "Sep":
        time_element[1] = "Septembre"
    if time_element[1] == "Oct":
        time_element[1] = "Octobre"
    if time_element[1] == "Nov":
        time_element[1] = "Novembre"
    if time_element[1] == "Dec":
        time_element[1] = "Décembre"


    #mise en forme de la date
    time_to_print = time_element[3] + " " + time_element[1] + " " + time_element[5]
    return time_to_print



# DEBUT DU PROGRAMME

# On parcourt les fichiers dans le dossier input
for file in os.listdir("./fichier_input"):
    '''Lecture de tous les fichiers dans le dossier /fichier_input'''
    # On réinitialise les tableaux users et lines
    users.clear()
    lines.clear()
    system("cls")
    NOM_ECOLE = os.path.splitext(file)[0]
    print("Traitement de " + NOM_ECOLE + "...")

    # Ouverture et lecture du fichier
    try:
        f = open("./fichier_input/"+file, "r")
        lines = f.readlines()
        f.close()
    except IOError:
        print("Erreur sur {1}: {0}" + format(IOError,NOM_ECOLE))

    # Récupération des données des utilisateurs dans la liste users
    get_user_data_from_file()

    # initialisation du fichier PDF
    pdf = FPDF()

    # Ecriture dans le fichier pour chaque utilisateur du tableau
    for user in users:
        print("Traitement de " + user.account_name)
        if len(sys.argv) > 1:
            if sys.argv[1] == '-c':
                user.print_everything()
                system("pause")
                system("cls")
        try:
            user.make_pdf()
        except ValueError:
            print("Erreur sur {1}: {0}" + format(ValueError,NOM_ECOLE))

    #Vérification de l'existence du dossier de sortie
    if not os.path.exists('./fichier_output/'):
        os.makedirs('./fichier_output/')

    # On écrit le PDF
    try:
        pdf.output('./fichier_output/' + NOM_ECOLE + '.pdf', 'F')
    except Exception:
        print(traceback.format_exc())
        # or
        print(sys.exc_info()[2])


#

#
#
#
