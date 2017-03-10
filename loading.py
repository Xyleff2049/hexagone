# ╔════════════════════════════════════════════════════════════════╗ #
# ║ Module affichant une barre de chargement dans le shell Python  ║ #
# ╚════════════════════════════════════════════════════════════════╝ #

import time

# ┌──────────────────────────────────────────────────────────────────┐ #
# │ La class loadingBar permet la creation d'une barre de chargement │ #
# └──────────────────────────────────────────────────────────────────┘ #

class loadingBar:

	idBar = 1 # Identifiant de l'objet

	def __init__(self, start, end, prefix="", suffix="", lenght=20, sprite="■", sep="-", endMessage=""):

		"""
			Creer l'objet avant de commencer les taches

			@Parametres
				start.......-Required : Valeur de depart (0)
				end.........-Required : Valeur de fin (nb de tache)
				prefix......-Optional : Texte affiche à gauche de la barre
				suffix......-Optional : Texte affiche à droite de la barre
				lenght......-Optional : Taille de la barre (20)
				sprite......-Optional : Caractere utilise pour le chargement
				sep.........-Optional : Caractere utilise pour combler
				endMessage..-Optional : Texte affiche à la fin du chargement

		"""

		self.id = loadingBar.idBar
		self.start = abs(start)
		self.step = self.start
		self.end = abs(end)
		self.prefix = prefix
		self.suffix = suffix
		self.lenght = lenght
		self.sprite = sprite
		self.sep = sep
		self.endMessage = endMessage + "\n"

		loadingBar.idBar += 1

	def displayBar(self, step):

		"""
			Affichage de l'etat actuel du chargement

			@Parametre:
				step........-Required : Etape actuel

		"""

		if step > self.end or step < self.start:
			print("loadingBar n°"+str(self.id)+" > Invalide step number")
			quit()

		self.step = step

		filled = (step * self.lenght) // self.end
		bar = self.sprite * filled + self.sep * (self.lenght - filled)
		percent = (step * 100) // self.end
		display = '{prefix} |{bar}| {percent}% {suffix}'.format(prefix=self.prefix,bar=bar,percent=percent,suffix=self.suffix)
		if step != self.end:
			print(display, end="\r")
		if step == self.end: 
			print(display)
			if self.endMessage != "": print(self.endMessage)

	def reset(self): self.step = self.start

# { Exemples } #

if __name__ == '__main__':

	print('Loading Bar by Louis Gasnault'.center(50))

	myLoadingBar = loadingBar(0, 20, prefix="Loading", suffix="Complete", endMessage="Task complete !")

	for i in range(0, 21):
		myLoadingBar.displayBar(i)
		time.sleep(0.3)

	mySecondLB = loadingBar(0, 3, prefix="En cours")
	mySecondLB.displayBar(1)
	time.sleep(0.5)# Des etapes pouvant prendre du temps
	mySecondLB.displayBar(2)
	time.sleep(1) # Le dernier chargement
	mySecondLB.displayBar(3)

# By Louis Gasnault, 2017