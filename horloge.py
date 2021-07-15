from datetime import datetime
import time
import os

separation = """
       
██╗    
╚═╝    
██╗    
╚═╝    
       """

zero = """
 ██████╗      ██████╗     
██╔═████╗    ██╔═████╗    
██║██╔██║    ██║██╔██║    
████╔╝██║    ████╔╝██║    
╚██████╔╝    ╚██████╔╝    
 ╚═════╝      ╚═════╝     """

un = """
 ██████╗      ██╗    
██╔═████╗    ███║    
██║██╔██║    ╚██║    
████╔╝██║     ██║    
╚██████╔╝     ██║    
 ╚═════╝      ╚═╝    """

deux = """
 ██████╗     ██████╗     
██╔═████╗    ╚════██╗    
██║██╔██║     █████╔╝    
████╔╝██║    ██╔═══╝     
╚██████╔╝    ███████╗    
 ╚═════╝     ╚══════╝    """

trois = """
 ██████╗     ██████╗     
██╔═████╗    ╚════██╗    
██║██╔██║     █████╔╝    
████╔╝██║     ╚═══██╗    
╚██████╔╝    ██████╔╝    
 ╚═════╝     ╚═════╝     """

quatre = """
 ██████╗     ██╗  ██╗    
██╔═████╗    ██║  ██║    
██║██╔██║    ███████║    
████╔╝██║    ╚════██║    
╚██████╔╝         ██║    
 ╚═════╝          ╚═╝    """

cinq = """
 ██████╗     ███████╗    
██╔═████╗    ██╔════╝    
██║██╔██║    ███████╗    
████╔╝██║    ╚════██║    
╚██████╔╝    ███████║    
 ╚═════╝     ╚══════╝    """

six = """
 ██████╗      ██████╗     
██╔═████╗    ██╔════╝     
██║██╔██║    ███████╗     
████╔╝██║    ██╔═══██╗    
╚██████╔╝    ╚██████╔╝    
 ╚═════╝      ╚═════╝     """

sept = """
 ██████╗     ███████╗    
██╔═████╗    ╚════██║    
██║██╔██║        ██╔╝    
████╔╝██║       ██╔╝     
╚██████╔╝       ██║      
 ╚═════╝        ╚═╝      """

huit = """
 ██████╗      █████╗     
██╔═████╗    ██╔══██╗    
██║██╔██║    ╚█████╔╝    
████╔╝██║    ██╔══██╗    
╚██████╔╝    ╚█████╔╝    
 ╚═════╝      ╚════╝     """

neuf = """
 ██████╗      █████╗     
██╔═████╗    ██╔══██╗    
██║██╔██║    ╚██████║    
████╔╝██║     ╚═══██║    
╚██████╔╝     █████╔╝    
 ╚═════╝      ╚════╝     """

dix = """
 ██╗     ██████╗     
███║    ██╔═████╗    
╚██║    ██║██╔██║    
 ██║    ████╔╝██║    
 ██║    ╚██████╔╝    
 ╚═╝     ╚═════╝     """

onze = """
 ██╗     ██╗    
███║    ███║    
╚██║    ╚██║    
 ██║     ██║    
 ██║     ██║    
 ╚═╝     ╚═╝    """

douze = """
 ██╗    ██████╗     
███║    ╚════██╗    
╚██║     █████╔╝    
 ██║    ██╔═══╝     
 ██║    ███████╗    
 ╚═╝    ╚══════╝    """

treize = """
 ██╗    ██████╗     
███║    ╚════██╗    
╚██║     █████╔╝    
 ██║     ╚═══██╗    
 ██║    ██████╔╝    
 ╚═╝    ╚═════╝     """

quatorze = """
 ██╗    ██╗  ██╗    
███║    ██║  ██║    
╚██║    ███████║    
 ██║    ╚════██║    
 ██║         ██║    
 ╚═╝         ╚═╝    """

quinze = """
 ██╗    ███████╗    
███║    ██╔════╝    
╚██║    ███████╗    
 ██║    ╚════██║    
 ██║    ███████║    
 ╚═╝    ╚══════╝    """

seize = """
 ██╗     ██████╗     
███║    ██╔════╝     
╚██║    ███████╗     
 ██║    ██╔═══██╗    
 ██║    ╚██████╔╝    
 ╚═╝     ╚═════╝     """

dix_sept = """
 ██╗    ███████╗    
███║    ╚════██║    
╚██║        ██╔╝    
 ██║       ██╔╝     
 ██║       ██║      
 ╚═╝       ╚═╝      """

dix_huit = """
 ██╗     █████╗     
███║    ██╔══██╗    
╚██║    ╚█████╔╝    
 ██║    ██╔══██╗    
 ██║    ╚█████╔╝    
 ╚═╝     ╚════╝     """

dix_neuf = """
 ██╗     █████╗     
███║    ██╔══██╗    
╚██║    ╚██████║    
 ██║     ╚═══██║    
 ██║     █████╔╝    
 ╚═╝     ╚════╝     """

vingt = """
██████╗      ██████╗     
╚════██╗    ██╔═████╗    
 █████╔╝    ██║██╔██║    
██╔═══╝     ████╔╝██║    
███████╗    ╚██████╔╝    
╚══════╝     ╚═════╝     """

vingt_et_un = """
██████╗      ██╗    
╚════██╗    ███║    
 █████╔╝    ╚██║    
██╔═══╝      ██║    
███████╗     ██║    
╚══════╝     ╚═╝    """

vingt_deux = """
██████╗     ██████╗     
╚════██╗    ╚════██╗    
 █████╔╝     █████╔╝    
██╔═══╝     ██╔═══╝     
███████╗    ███████╗    
╚══════╝    ╚══════╝    """

vingt_trois = """
██████╗     ██████╗     
╚════██╗    ╚════██╗    
 █████╔╝     █████╔╝    
██╔═══╝      ╚═══██╗    
███████╗    ██████╔╝    
╚══════╝    ╚═════╝     """

vingt_quatre = """
██████╗     ██╗  ██╗    
╚════██╗    ██║  ██║    
 █████╔╝    ███████║    
██╔═══╝     ╚════██║    
███████╗         ██║    
╚══════╝         ╚═╝    """

vingt_cinq = """
██████╗     ███████╗    
╚════██╗    ██╔════╝    
 █████╔╝    ███████╗    
██╔═══╝     ╚════██║    
███████╗    ███████║    
╚══════╝    ╚══════╝    """

vingt_six = """
██████╗      ██████╗     
╚════██╗    ██╔════╝     
 █████╔╝    ███████╗     
██╔═══╝     ██╔═══██╗    
███████╗    ╚██████╔╝    
╚══════╝     ╚═════╝     """

vingt_sept = """
██████╗     ███████╗    
╚════██╗    ╚════██║    
 █████╔╝        ██╔╝    
██╔═══╝        ██╔╝     
███████╗       ██║      
╚══════╝       ╚═╝      """

vingt_huit = """
██████╗      █████╗     
╚════██╗    ██╔══██╗    
 █████╔╝    ╚█████╔╝    
██╔═══╝     ██╔══██╗    
███████╗    ╚█████╔╝    
╚══════╝     ╚════╝     """

vingt_neuf = """
██████╗      █████╗     
╚════██╗    ██╔══██╗    
 █████╔╝    ╚██████║    
██╔═══╝      ╚═══██║    
███████╗     █████╔╝    
╚══════╝     ╚════╝     """

trente = """
██████╗      ██████╗     
╚════██╗    ██╔═████╗    
 █████╔╝    ██║██╔██║    
 ╚═══██╗    ████╔╝██║    
██████╔╝    ╚██████╔╝    
╚═════╝      ╚═════╝     """

trente_et_un = """
██████╗      ██╗    
╚════██╗    ███║    
 █████╔╝    ╚██║    
 ╚═══██╗     ██║    
██████╔╝     ██║    
╚═════╝      ╚═╝    
"""

trente_deux = """
██████╗     ██████╗     
╚════██╗    ╚════██╗    
 █████╔╝     █████╔╝    
 ╚═══██╗    ██╔═══╝     
██████╔╝    ███████╗    
╚═════╝     ╚══════╝    """

trente_trois = """
██████╗     ██████╗     
╚════██╗    ╚════██╗    
 █████╔╝     █████╔╝    
 ╚═══██╗     ╚═══██╗    
██████╔╝    ██████╔╝    
╚═════╝     ╚═════╝     """

trente_quatre = """
██████╗     ██╗  ██╗    
╚════██╗    ██║  ██║    
 █████╔╝    ███████║    
 ╚═══██╗    ╚════██║    
██████╔╝         ██║    
╚═════╝          ╚═╝    """

trente_cinq = """
██████╗     ███████╗    
╚════██╗    ██╔════╝    
 █████╔╝    ███████╗    
 ╚═══██╗    ╚════██║    
██████╔╝    ███████║    
╚═════╝     ╚══════╝    """

trente_six = """
██████╗      ██████╗     
╚════██╗    ██╔════╝     
 █████╔╝    ███████╗     
 ╚═══██╗    ██╔═══██╗    
██████╔╝    ╚██████╔╝    
╚═════╝      ╚═════╝     """

trente_sept = """
██████╗     ███████╗    
╚════██╗    ╚════██║    
 █████╔╝        ██╔╝    
 ╚═══██╗       ██╔╝     
██████╔╝       ██║      
╚═════╝        ╚═╝      """

trente_huit = """
██████╗      █████╗     
╚════██╗    ██╔══██╗    
 █████╔╝    ╚█████╔╝    
 ╚═══██╗    ██╔══██╗    
██████╔╝    ╚█████╔╝    
╚═════╝      ╚════╝     """

trente_neuf = """
██████╗      █████╗     
╚════██╗    ██╔══██╗    
 █████╔╝    ╚██████║    
 ╚═══██╗     ╚═══██║    
██████╔╝     █████╔╝    
╚═════╝      ╚════╝     """

quarente = """
██╗  ██╗     ██████╗     
██║  ██║    ██╔═████╗    
███████║    ██║██╔██║    
╚════██║    ████╔╝██║    
     ██║    ╚██████╔╝    
     ╚═╝     ╚═════╝     """

quarente_et_un = """
██╗  ██╗     ██╗    
██║  ██║    ███║    
███████║    ╚██║    
╚════██║     ██║    
     ██║     ██║    
     ╚═╝     ╚═╝    """

quarente_deux = """
██╗  ██╗    ██████╗     
██║  ██║    ╚════██╗    
███████║     █████╔╝    
╚════██║    ██╔═══╝     
     ██║    ███████╗    
     ╚═╝    ╚══════╝    """

quarente_trois = """
██╗  ██╗    ██████╗     
██║  ██║    ╚════██╗    
███████║     █████╔╝    
╚════██║     ╚═══██╗    
     ██║    ██████╔╝    
     ╚═╝    ╚═════╝     """

quarente_quatre = """
██╗  ██╗    ██╗  ██╗    
██║  ██║    ██║  ██║    
███████║    ███████║    
╚════██║    ╚════██║    
     ██║         ██║    
     ╚═╝         ╚═╝    """

quarente_cinq = """
██╗  ██╗    ███████╗    
██║  ██║    ██╔════╝    
███████║    ███████╗    
╚════██║    ╚════██║    
     ██║    ███████║    
     ╚═╝    ╚══════╝    """

quarente_six = """
██╗  ██╗     ██████╗     
██║  ██║    ██╔════╝     
███████║    ███████╗     
╚════██║    ██╔═══██╗    
     ██║    ╚██████╔╝    
     ╚═╝     ╚═════╝     """

quarente_sept = """
██╗  ██╗    ███████╗    
██║  ██║    ╚════██║    
███████║        ██╔╝    
╚════██║       ██╔╝     
     ██║       ██║      
     ╚═╝       ╚═╝      """

quarente_huit = """
██╗  ██╗     █████╗     
██║  ██║    ██╔══██╗    
███████║    ╚█████╔╝    
╚════██║    ██╔══██╗    
     ██║    ╚█████╔╝    
     ╚═╝     ╚════╝     """

quarente_neuf = """
██╗  ██╗     █████╗     
██║  ██║    ██╔══██╗    
███████║    ╚██████║    
╚════██║     ╚═══██║    
     ██║     █████╔╝    
     ╚═╝     ╚════╝     """

cinquante = """
███████╗     ██████╗     
██╔════╝    ██╔═████╗    
███████╗    ██║██╔██║    
╚════██║    ████╔╝██║    
███████║    ╚██████╔╝    
╚══════╝     ╚═════╝     """

cinquante_et_un = """
███████╗     ██╗    
██╔════╝    ███║    
███████╗    ╚██║    
╚════██║     ██║    
███████║     ██║    
╚══════╝     ╚═╝    """

cinquante_deux = """
███████╗    ██████╗     
██╔════╝    ╚════██╗    
███████╗     █████╔╝    
╚════██║    ██╔═══╝     
███████║    ███████╗    
╚══════╝    ╚══════╝    """

cinquante_trois = """
███████╗    ██████╗     
██╔════╝    ╚════██╗    
███████╗     █████╔╝    
╚════██║     ╚═══██╗    
███████║    ██████╔╝    
╚══════╝    ╚═════╝     """

cinquante_quatre = """
███████╗    ██╗  ██╗    
██╔════╝    ██║  ██║    
███████╗    ███████║    
╚════██║    ╚════██║    
███████║         ██║    
╚══════╝         ╚═╝    """

cinquante_cinq = """
███████╗    ███████╗    
██╔════╝    ██╔════╝    
███████╗    ███████╗    
╚════██║    ╚════██║    
███████║    ███████║    
╚══════╝    ╚══════╝    """

cinquante_six = """
███████╗     ██████╗     
██╔════╝    ██╔════╝     
███████╗    ███████╗     
╚════██║    ██╔═══██╗    
███████║    ╚██████╔╝    
╚══════╝     ╚═════╝     """

cinquante_sept = """
███████╗    ███████╗    
██╔════╝    ╚════██║    
███████╗        ██╔╝    
╚════██║       ██╔╝     
███████║       ██║      
╚══════╝       ╚═╝      """

cinquante_huit = """
███████╗     █████╗     
██╔════╝    ██╔══██╗    
███████╗    ╚█████╔╝    
╚════██║    ██╔══██╗    
███████║    ╚█████╔╝    
╚══════╝     ╚════╝     """

cinquante_neuf = """
███████╗     █████╗     
██╔════╝    ██╔══██╗    
███████╗    ╚██████║    
╚════██║     ╚═══██║    
███████║     █████╔╝    
╚══════╝     ╚════╝     """

soixante = """
 ██████╗      ██████╗     
██╔════╝     ██╔═████╗    
███████╗     ██║██╔██║    
██╔═══██╗    ████╔╝██║    
╚██████╔╝    ╚██████╔╝    
 ╚═════╝      ╚═════╝     """


nombres = [un, deux, trois, quatre, cinq, six, sept, huit, neuf, dix, onze, douze, treize, quatorze, quinze, seize, dix_sept, dix_huit, dix_neuf, vingt, vingt_et_un, vingt_deux, vingt_trois, vingt_quatre, vingt_cinq, vingt_six, vingt_sept, vingt_huit, vingt_neuf, trente, trente_et_un, trente_deux, trente_trois, trente_quatre, trente_cinq, trente_six, trente_sept, trente_huit, trente_neuf, quarente, quarente_et_un, quarente_deux, quarente_trois, quarente_quatre, quarente_cinq, quarente_six, quarente_sept, quarente_huit, quarente_neuf, cinquante, cinquante_et_un, cinquante_deux, cinquante_trois, cinquante_quatre, cinquante_cinq, cinquante_six, cinquante_sept, cinquante_huit, cinquante_neuf, soixante]

minutes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60"]

secondes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60"]

heures = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]

while True:
	temps = datetime.now()
	heure = temps.strftime("%H")
	minute = temps.strftime("%M")
	seconde = temps.strftime("%S")
	s = []
	m = []
	h = []

	if seconde == "00":
		s.append(zero)
	if seconde == "01":
		s.append(un)
	if seconde == "02":
		s.append(deux)
	if seconde == "03":
		s.append(trois)
	if seconde == "04":
		s.append(quatre)
	if seconde == "05":
		s.append(cinq)
	if seconde == "06":
		s.append(six)
	if seconde == "07":
		s.append(sept)
	if seconde == "08":
		s.append(huit)
	if seconde == "09":
		s.append(neuf)
	if seconde == "10":
		s.append(dix)
	if seconde == "11":
		s.append(onze)
	if seconde == "12":
		s.append(douze)
	if seconde == "13":
		s.append(treize)
	if seconde == "14":
		s.append(quatorze)
	if seconde == "15":
		s.append(quinze)
	if seconde == "16":
		s.append(seize)
	if seconde == "17":
		s.append(dix_sept)
	if seconde == "18":
		s.append(dix_huit)
	if seconde == "19":
		s.append(dix_neuf)
	if seconde == "20":
		s.append(vingt)
	if seconde == "21":
		s.append(vingt_et_un)
	if seconde == "22":
		s.append(vingt_deux)
	if seconde == "23":
		s.append(vingt_trois)
	if seconde == "24":
		s.append(vingt_quatre)
	if seconde == "25":
		s.append(vingt_cinq)
	if seconde == "26":
		s.append(vingt_six)
	if seconde == "27":
		s.append(vingt_sept)
	if seconde == "28":
		s.append(vingt_huit)
	if seconde == "29":
		s.append(vingt_neuf)
	if seconde == "30":
		s.append(trente)
	if seconde == "31":
		s.append(trente_et_un)
	if seconde == "32":
		s.append(trente_deux)
	if seconde == "33":
		s.append(trente_trois)
	if seconde == "34":
		s.append(trente_quatre)
	if seconde == "35":
		s.append(trente_cinq)
	if seconde == "36":
		s.append(trente_six)
	if seconde == "37":
		s.append(trente_sept)
	if seconde == "38":
		s.append(trente_huit)
	if seconde == "39":
		s.append(trente_neuf)
	if seconde == "40":
		s.append(quarente)
	if seconde == "41":
		s.append(quarente_et_un)
	if seconde == "42":
		s.append(quarente_deux)
	if seconde == "43":
		s.append(quarente_trois)
	if seconde == "44":
		s.append(quarente_quatre)
	if seconde == "45":
		s.append(quarente_cinq)
	if seconde == "46":
		s.append(quarente_six)
	if seconde == "47":
		s.append(quarente_sept)
	if seconde == "48":
		s.append(quarente_huit)
	if seconde == "49":
		s.append(quarente_neuf)
	if seconde == "50":
		s.append(cinquante)
	if seconde == "51":
		s.append(cinquante_et_un)
	if seconde == "52":
		s.append(cinquante_deux)
	if seconde == "53":
		s.append(cinquante_trois)
	if seconde == "54":
		s.append(cinquante_quatre)
	if seconde == "55":
		s.append(cinquante_cinq)
	if seconde == "56":
		s.append(cinquante_six)
	if seconde == "57":
		s.append(cinquante_sept)
	if seconde == "58":
		s.append(cinquante_huit)
	if seconde == "59":
		s.append(cinquante_neuf)
	if seconde == "60":
		s.append(soixante)

	s = "\n".join(s)

	if minute == "00":
		m.append(zero)
	if minute == "01":
		m.append(un)
	if minute == "02":
		m.append(deux)
	if minute == "03":
		m.append(trois)
	if minute == "04":
		m.append(quatre)
	if minute == "05":
		m.append(cinq)
	if minute == "06":
		m.append(six)
	if minute == "07":
		m.append(sept)
	if minute == "08":
		m.append(huit)
	if minute == "09":
		m.append(neuf)
	if minute == "10":
		m.append(dix)
	if minute == "11":
		m.append(onze)
	if minute == "12":
		m.append(douze)
	if minute == "13":
		m.append(treize)
	if minute == "14":
		m.append(quatorze)
	if minute == "15":
		m.append(quinze)
	if minute == "16":
		m.append(seize)
	if minute == "17":
		m.append(dix_sept)
	if minute == "18":
		m.append(dix_huit)
	if minute == "19":
		m.append(dix_neuf)
	if minute == "20":
		m.append(vingt)
	if minute == "21":
		m.append(vingt_et_un)
	if minute == "22":
		m.append(vingt_deux)
	if minute == "23":
		m.append(vingt_trois)
	if minute == "24":
		m.append(vingt_quatre)
	if minute == "25":
		m.append(vingt_cinq)
	if minute == "26":
		m.append(vingt_six)
	if minute == "27":
		m.append(vingt_sept)
	if minute == "28":
		m.append(vingt_huit)
	if minute == "29":
		m.append(vingt_neuf)
	if minute == "30":
		m.append(trente)
	if minute == "31":
		m.append(trente_et_un)
	if minute == "32":
		m.append(trente_deux)
	if minute == "33":
		m.append(trente_trois)
	if minute == "34":
		m.append(trente_quatre)
	if minute == "35":
		m.append(trente_cinq)
	if minute == "36":
		m.append(trente_six)
	if minute == "37":
		m.append(trente_sept)
	if minute == "38":
		m.append(trente_huit)
	if minute == "39":
		m.append(trente_neuf)
	if minute == "40":
		m.append(quarente)
	if minute == "41":
		m.append(quarente_et_un)
	if minute == "42":
		m.append(quarente_deux)
	if minute == "43":
		m.append(quarente_trois)
	if minute == "44":
		m.append(quarente_quatre)
	if minute == "45":
		m.append(quarente_cinq)
	if minute == "46":
		m.append(quarente_six)
	if minute == "47":
		m.append(quarente_sept)
	if minute == "48":
		m.append(quarente_huit)
	if minute == "49":
		m.append(quarente_neuf)
	if minute == "50":
		m.append(cinquante)
	if minute == "51":
		m.append(cinquante_et_un)
	if minute == "52":
		m.append(cinquante_deux)
	if minute == "53":
		m.append(cinquante_trois)
	if minute == "54":
		m.append(cinquante_quatre)
	if minute == "55":
		m.append(cinquante_cinq)
	if minute == "56":
		m.append(cinquante_six)
	if minute == "57":
		m.append(cinquante_sept)
	if minute == "58":
		m.append(cinquante_huit)
	if minute == "59":
		m.append(cinquante_neuf)
	if minute == "60":
		m.append(soixante)
	
	m = "\n".join(m)

	if heure == "00":
		h.append(zero)
	if heure == "01":
		h.append(un)
	if heure == "02":
		h.append(deux)
	if heure == "03":
		h.append(trois)
	if heure == "04":
		h.append(quatre)
	if heure == "05":
		h.append(cinq)
	if heure == "06":
		h.append(six)
	if heure == "07":
		h.append(sept)
	if heure == "08":
		h.append(huit)
	if heure == "09":
		h.append(neuf)
	if heure == "10":
		h.append(dix)
	if heure == "11":
		h.append(onze)
	if heure == "12":
		h.append(douze)
	if heure == "13":
		h.append(treize)
	if heure == "14":
		h.append(quatorze)
	if heure == "15":
		h.append(quinze)
	if heure == "16":
		h.append(seize)
	if heure == "17":
		h.append(dix_sept)
	if heure == "18":
		h.append(dix_huit)
	if heure == "19":
		h.append(dix_neuf)
	if heure == "20":
		h.append(vingt)
	if heure == "21":
		h.append(vingt_et_un)
	if heure == "22":
		h.append(vingt_deux)
	if heure == "23":
		h.append(vingt_trois)

	h = "\n".join(h)

	fetch_time = ''
	for el1, el2, el3, el4 in zip(h.split('\n'), m.split('\n'), separation.split('\n'), s.split('\n')):
		fetch_time += el1 + el3 + el2 + el3 + el4 + "\n"
	
	split = fetch_time.splitlines()
	
	cal = 255 // len(split)
	
	valeur = 0

	for line in split:
		fetch_time = f"\033[38;2;0;{valeur};255m{line}"
		print(fetch_time)
		valeur += cal
	time.sleep(1)
	os.system("cls")
