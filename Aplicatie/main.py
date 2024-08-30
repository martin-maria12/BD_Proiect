import sys
import oracledb
import datetime

# GUI
from Interfata import Ui_SearaDeFilm
from dialog_Actor_Regizor import Ui_DialogEAR
from dialog_Film import Ui_DialogEM

# PyQt5 imports
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, \
	QMessageBox, QSizePolicy, QDialog
from PyQt5.QtCore import QRect

oracledb.init_oracle_client()

connection = oracledb.connect(
	user="maria",
	password="2008Mm1206D!",
	dsn="localhost:1521/xe")

print("Successfully connected to Oracle Database")

#Pentru executia instructiunilor sql, al doilea auxiliar pentru eventuale comparatii
cursor = connection.cursor()
cursor2 = connection.cursor()


class Window(QMainWindow, Ui_SearaDeFilm):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)

		self.setupUi(self)

		self.init_buttons()
		self.init_home()
		self.init_news()
		self.initDate()

		# Save containers: widgeturi specifice fiecarui gen pentru continutul lor
		self.containerByGenre = {
			'Action': 		self.topWidgetAction,
			'Adventure': 	self.topWidgetAdventure,
			'Animated': 	self.topWidgetAnimated,
			'Comedy': 		self.topWidgetComedy,
			'Drama': 		self.topWidgetDrama,
			'Fantasy': 		self.topWidgetFantasy,
			'Horror': 		self.topWidgetHorror,
			'Musical': 		self.topWidgetMusical,
			'Mystery': 		self.topWidgetMystery,
			'Romance': 		self.topWidgetRomance,
			'SuperHero': 	self.topWidgetSuperHero,
			'Thriller': 	self.topWidgetThriller
		}
		# Save containers
		self.scrollAreaByGenre = {
			'Action': 		self.Container_ActionMovieList,
			'Adventure': 	self.Container_AdventureMovieList,
			'Animated': 	self.Container_AnimatedMovieList,
			'Comedy': 		self.Container_ComedyMovieList,
			'Drama': 		self.Container_DramaMovieList,
			'Fantasy': 		self.Container_FantasyMovieList,
			'Horror': 		self.Container_HorrorMovieList,
			'Musical': 		self.Container_MusicalMovieList,
			'Mystery': 		self.Container_MysteryMovieList,
			'Romance': 		self.Container_RomanceMovieList,
			'SuperHero': 	self.Container_SuperHeroMovieList,
			'Thriller': 	self.Container_ThrillerMovieList
		}

		# For storing data about actors, movie directors and movies for editing them
		self.confirmUpdate = False

		#Retinem date pentru edit-uri
		self.actorData = {
			'Nume': None,
			'Prenume': None,
			'DataNasterii': None
		}
		self.regizorData = {
			'Nume': None,
			'Prenume': None,
			'DataNasterii': None
		}
		self.movieData = {
			'Titlu': None,
			'AnAparitie': None,
			'Gen': None,
		}

	#############################
	# 		INITIALIZATION		#
	#############################
	def init_buttons(self):
		# Click the dropdown box
		self.CB_minimize.clicked.connect(self.minimize)
		self.CB_maximize.clicked.connect(self.maximize)
		self.CB_restoreWindow.clicked.connect(self.restore)
		self.CB_close.clicked.connect(self.closeApp)

		# Menu CBs
		self.CB_1_Home.clicked.connect(lambda: self.pages.setCurrentIndex(0))
		self.CB_2_Favorites.clicked.connect(lambda: self.pages.setCurrentIndex(1))
		self.CB_2_Favorites.clicked.connect(self.refresh_fav)
		self.CB_3_NewMovies.clicked.connect(lambda: self.pages.setCurrentIndex(2))
		self.CB_4_Movies.clicked.connect(lambda: self.pages.setCurrentIndex(3))
		self.CB_4_Movies.clicked.connect(self.refresh_movies)
		self.CB_5_Actors.clicked.connect(lambda: self.pages.setCurrentIndex(4))
		self.CB_5_Actors.clicked.connect(self.refresh_actors)
		self.CB_6_MovieDirector.clicked.connect(lambda: self.pages.setCurrentIndex(5))
		self.CB_6_MovieDirector.clicked.connect(self.refresh_movieDirectors)

		# HomePage
		self.CB_HomeMore.clicked.connect(lambda: self.pages.setCurrentIndex(2))

		# FavoritePage
		self.CB_AddFav.clicked.connect(self.initComboBoxsFav)
		self.CB_AddFav.clicked.connect(lambda: self.pages.setCurrentIndex(22))

		# NewsPage

		# MoviesPage
		# self.CB_BActor.clicked.connect(lambda: self.pages.setCurrentIndex(DECOMPLETAT))
		self.CB_BGenre.clicked.connect(lambda: self.pages.setCurrentIndex(6))
		# self.CB_BMDirector.clicked.connect(lambda: self.pages.setCurrentIndex(DECOMPLETAT))
		self.CB_AddMovie.clicked.connect(self.initComboBoxsMovies)
		self.CB_AddMovie.clicked.connect(lambda: self.pages.setCurrentIndex(19))

		# ActorsPage
		self.CB_AddActor.clicked.connect(lambda: self.pages.setCurrentIndex(20))

		# MovieDirectorsPage
		self.CB_AddMovieDirectors.clicked.connect(lambda: self.pages.setCurrentIndex(21))

		# MovieGenrePage
		self.CB_Action.clicked.connect(lambda: self.pages.setCurrentIndex(7))
		self.CB_Action.clicked.connect(lambda: self.refresh_genrePage('Action'))
		self.CB_Animated.clicked.connect(lambda: self.pages.setCurrentIndex(8))
		self.CB_Animated.clicked.connect(lambda: self.refresh_genrePage('Animated'))
		self.CB_Comedy.clicked.connect(lambda: self.pages.setCurrentIndex(9))
		self.CB_Comedy.clicked.connect(lambda: self.refresh_genrePage('Comedy'))
		self.CB_Drama.clicked.connect(lambda: self.pages.setCurrentIndex(10))
		self.CB_Drama.clicked.connect(lambda: self.refresh_genrePage('Drama'))
		self.CB_Fantasy.clicked.connect(lambda: self.pages.setCurrentIndex(11))
		self.CB_Fantasy.clicked.connect(lambda: self.refresh_genrePage('Fantasy'))
		self.CB_Horror.clicked.connect(lambda: self.pages.setCurrentIndex(12))
		self.CB_Horror.clicked.connect(lambda: self.refresh_genrePage('Horror'))
		self.CB_Mystery.clicked.connect(lambda: self.pages.setCurrentIndex(13))
		self.CB_Mystery.clicked.connect(lambda: self.refresh_genrePage('Mystery'))
		self.CB_Romance.clicked.connect(lambda: self.pages.setCurrentIndex(14))
		self.CB_Romance.clicked.connect(lambda: self.refresh_genrePage('Romance'))
		self.CB_Thriller.clicked.connect(lambda: self.pages.setCurrentIndex(15))
		self.CB_Thriller.clicked.connect(lambda: self.refresh_genrePage('Thriller'))
		self.CB_Adventure.clicked.connect(lambda: self.pages.setCurrentIndex(18))
		self.CB_Adventure.clicked.connect(lambda: self.refresh_genrePage('Adventure'))
		self.CB_Musical.clicked.connect(lambda: self.pages.setCurrentIndex(16))
		self.CB_Musical.clicked.connect(lambda: self.refresh_genrePage('Musical'))
		self.CB_SuperHero.clicked.connect(lambda: self.pages.setCurrentIndex(17))
		self.CB_SuperHero.clicked.connect(lambda: self.refresh_genrePage('SuperHero'))

		# ActionPage
		self.CB_ActionBack.clicked.connect(lambda: self.pages.setCurrentIndex(6))

		# AdventurePage
		self.CB_AdventureBack.clicked.connect(lambda: self.pages.setCurrentIndex(6))

		# AnimatedPage
		self.CB_AnimatedBack.clicked.connect(lambda: self.pages.setCurrentIndex(6))

		# ComedyPage
		self.CB_ComedyBack.clicked.connect(lambda: self.pages.setCurrentIndex(6))

		# DramaPage
		self.CB_DramaBack.clicked.connect(lambda: self.pages.setCurrentIndex(6))

		# FantasyPage
		self.CB_FantasyBack.clicked.connect(lambda: self.pages.setCurrentIndex(6))

		# HorrorPage
		self.CB_HorrorBack.clicked.connect(lambda: self.pages.setCurrentIndex(6))

		# MusicalPage
		self.CB_MusicalBack.clicked.connect(lambda: self.pages.setCurrentIndex(6))

		# MysteryPage
		self.CB_MysteryBack.clicked.connect(lambda: self.pages.setCurrentIndex(6))

		# RomancePage
		self.CB_RomanceBack.clicked.connect(lambda: self.pages.setCurrentIndex(6))

		# SuperHeroPage
		self.CB_SuperHeroBack.clicked.connect(lambda: self.pages.setCurrentIndex(6))

		# ThrillerPage
		self.CB_ThrillerBack.clicked.connect(lambda: self.pages.setCurrentIndex(6))

		# AddNewMoviePage
		self.CB_ANM_Add.clicked.connect(self.add_film)

		# AddNewActorPage
		self.CB_ANA_Add.clicked.connect(self.add_actor)

		# AddNewMovieDirectorPage
		self.CB_ANMD_Add.clicked.connect(self.add_regizor)

		# AddNewFavoriteMoviePage
		self.CB_ANF_Add.clicked.connect(self.add_favorite)

	def init_home(self):
		cursor.execute(
			"SELECT (r.nume||' '||r.prenume), f.an_aparitie, f.titlu " +
			"FROM Filme f, Regizori r " +
			"WHERE isTop = 1 AND r.ID_Regizor=f.Regizori_ID_Regizor"
		)
		topVLayout = QVBoxLayout() #Layout-uri cu fiecare valoare
		topVLayout.addLayout(self.makeRow(False, False, 'title', [-1, 100, 0], "Nume Regizor", "An", "Titlu"))
		for text in cursor:
			topVLayout.addLayout(self.makeRow(False, False, 'home', [-1, 100, 0], *text))
		topVLayout.addStretch(1) #Spatiere
		self.topWidgetHome.setLayout(topVLayout) #Setam in Scroll area

	def init_news(self):
		cursor.execute(
			"SELECT f.titlu, f.an_aparitie, (r.nume||' '||r.prenume) " +
			"FROM Filme f, Regizori r " +
			"WHERE an_aparitie=2022 AND r.ID_Regizor=f.Regizori_ID_Regizor"
		)
		topVLayout = QVBoxLayout()
		topVLayout.addLayout(self.makeRow(False, False, 'title', [0, 100, -1], "Titlu", "An", "Nume Regizor"))
		for text in cursor:
			topVLayout.addLayout(self.makeRow(False, False, 'news', [0, 100, -1], *text))
		topVLayout.addStretch(1)
		self.topWidgetNew.setLayout(topVLayout)

	#Pentru adaugare filme
	def initComboBoxsMovies(self):
		# Add all actors to combobox
		cursor.execute("select nume, prenume from actori")
		for element in cursor:
			self.comboBoxAdd_Actor.addItem(str(element[0]) + ' ' + str(element[1]))

		# Add all movie directors to combobox
		cursor.execute("select nume, prenume from regizori")
		for element in cursor:
			self.comboBoxAdd_Regizor.addItem(str(element[0]) + ' ' + str(element[1]))

	#Pentru adaugare favorite
	def initComboBoxsFav(self):
		# Add all movies to combobox
		cursor.execute("select titlu from filme")
		for element in cursor:
			self.comboBoxAdd_Fav.addItem(str(element[0]))

	#Adauga an si zi in combobox pentru data nasterii actor si regizor
	def initDate(self):
		for i in range(1920, 2020):
			self.comboBoxA_an.addItem(str(i))
			self.comboBoxR_an.addItem(str(i))
		for i in range(1, 31):
			self.comboBoxA_zi.addItem(str(i).zfill(2))
			self.comboBoxR_zi.addItem(str(i).zfill(2))

	#############################
	# 		REFRESH PAGES		#
	#############################
	def refresh_genrePage(self, genre: str):
		self.containerByGenre[genre].deleteLater()
		cursor.execute(
			"SELECT f.ID_Film, f.titlu, f.an_aparitie, (r.nume||' '||r.prenume) " +
			"FROM Filme f, Regizori r " +
			"WHERE gen=:1 AND r.ID_Regizor=f.Regizori_ID_Regizor",
			(genre,)
		)
		self.topWidget = QWidget()
		self.scrollAreaByGenre[genre].setWidget(self.topWidget)
		self.containerByGenre[genre] = self.topWidget
		self.containerByGenre[genre].setGeometry(QRect(0, 0, 100, 30))
		self.containerByGenre[genre].setObjectName(f"topWidget{genre}")
		topVLayout = QVBoxLayout()
		topVLayout.addLayout(self.makeRow(True, True, 'title', [100, -1, 100, 0], "ID_Film", "Titlu", "An", "Nume Regizor"))
		for text in cursor:
			topVLayout.addLayout(self.makeRow(True, True, 'movie', [100, -1, 100, 0], *text))
		topVLayout.addStretch(1)
		self.containerByGenre[genre].setLayout(topVLayout)

	def refresh_fav(self):
		self.topWidgetFav.deleteLater()
		self.topWidgetFav = QWidget()
		self.Container_FavMovies.setWidget(self.topWidgetFav)
		self.topWidgetFav.setGeometry(QRect(0, 0, 100, 30))
		self.topWidgetFav.setObjectName("topWidgetFav")
		topVLayout = QVBoxLayout()

		cursor.execute("select * from favorite")
		contor = 0
		for el in cursor:
			if el:
				contor += 1
		if contor == 0:
			topVLayout.addLayout(self.makeRow(False, False, 'title', [-1], "Nu ai niciun film favorit in lista ta!"))
			topVLayout.addLayout(self.makeRow(False, False, 'title', [-1], "Apasa pe Add pentru a adauga unul!"))
		else:
			cursor.execute(
				"SELECT f.id_film, f.titlu, f.an_aparitie, f.gen " +
				"FROM Filme f, Favorite ff " +
				"WHERE f.id_film = ff.filme_id_film"
			)
			topVLayout.addLayout(self.makeRow(False, True, 'title', [100, -1, 200, 300], "ID Film", "Titlu", "An", "Gen"))
			for text in cursor:
				topVLayout.addLayout(self.makeRow(False, True, 'fav', [100, -1, 200, 300], *text))

		topVLayout.addStretch(1)
		self.topWidgetFav.setLayout(topVLayout)

	def refresh_actors(self):
		self.topWidgetActor.deleteLater()
		self.topWidgetActor = QWidget()
		self.ContainerScroll_Actor.setWidget(self.topWidgetActor)
		self.topWidgetActor.setGeometry(QRect(0, 0, 100, 30))
		self.topWidgetActor.setObjectName("topWidgetActor")
		topVLayout = QVBoxLayout()

		cursor.execute(
			"SELECT a.id_actor, (a.nume||' '||a.prenume), NVL(TO_CHAR(a.data_nasterii), 'Indisponibil'), COUNT(f.id_film) " +
			"FROM Filme f " +
			"RIGHT JOIN Actori a ON f.ACTORI_ID_Actor=a.ID_Actor " +
			"GROUP BY a.id_actor, (a.nume||' '||a.prenume), a.data_nasterii " +
			"ORDER BY id_actor"
		)
		topVLayout.addLayout(self.makeRow(True, True, 'title', [100, -1, 300, 100], "ID Actor", "Nume", "Data nasterii", "Numar Filme"))
		for text in cursor:
			topVLayout.addLayout(self.makeRow(True, True, 'actor', [100, -1, 300, 100], *text))
		topVLayout.addStretch(1)
		self.topWidgetActor.setLayout(topVLayout)

	def refresh_movieDirectors(self):
		self.topWidgetMovieDirectors.deleteLater()
		self.topWidgetMovieDirectors = QWidget()
		self.Container_MovieDirectors.setWidget(self.topWidgetMovieDirectors)
		self.topWidgetMovieDirectors.setGeometry(QRect(0, 0, 100, 30))
		self.topWidgetMovieDirectors.setObjectName("topWidgetActor")
		topVLayout = QVBoxLayout()

		cursor.execute(
			"SELECT r.ID_Regizor, (r.nume||' '||r.prenume), NVL(TO_CHAR(r.data_nasterii), 'Indisponibil'), COUNT(f.id_film) " +
			"FROM Filme f " +
			"RIGHT JOIN Regizori r ON f.REGIZORI_ID_Regizor=r.ID_Regizor " +
			"GROUP BY r.ID_Regizor, (r.nume||' '||r.prenume), r.data_nasterii " +
			"ORDER BY r.ID_Regizor"
		)
		topVLayout.addLayout(self.makeRow(True, True, 'title', [100, -1, 300, 100], "ID Regizor", "Nume", "Data nasterii", "Numar Filme"))
		for text in cursor:
			topVLayout.addLayout(self.makeRow(True, True, 'moviedirector', [100, -1, 300, 100], *text))
		topVLayout.addStretch(1)
		self.topWidgetMovieDirectors.setLayout(topVLayout)

	def refresh_movies(self):
		self.topWidgetMovies.deleteLater()
		self.topWidgetMovies = QWidget()
		self.Container_MovieListRandom.setWidget(self.topWidgetMovies)
		self.topWidgetMovies.setGeometry(QRect(0, 0, 100, 30))
		self.topWidgetMovies.setObjectName("topWidgetMovies")
		topVLayout = QVBoxLayout()

		cursor.execute(
			"SELECT f.id_film, f.titlu, f.an_aparitie, f.gen, (a.nume || ' ' || a.prenume), (r.nume || ' ' || r.prenume) " +
			"FROM Filme f, Actori a, Regizori r " +
			"WHERE f.actori_id_actor = a.id_actor AND f.regizori_id_regizor = r.id_regizor"
		)
		topVLayout.addLayout(self.makeRow(False, False, 'title', [100, -1, 100, 300, -1, -1], "ID Film", "Titlu", "An aparitie", "Gen", "Actor", "Regizor"))
		for text in cursor:
			topVLayout.addLayout(self.makeRow(False, False, 'movie', [100, -1, 100, 300, -1, -1], *text))
		topVLayout.addStretch(1)
		self.topWidgetMovies.setLayout(topVLayout)

	def refreshAllGenres(self):
		self.refresh_genrePage('Action')
		self.refresh_genrePage('Adventure')
		self.refresh_genrePage('Animated')
		self.refresh_genrePage('Comedy')
		self.refresh_genrePage('Drama')
		self.refresh_genrePage('Fantasy')
		self.refresh_genrePage('Horror')
		self.refresh_genrePage('Musical')
		self.refresh_genrePage('Mystery')
		self.refresh_genrePage('Romance')
		self.refresh_genrePage('SuperHero')
		self.refresh_genrePage('Thriller')

	#############################
	# 			INSERT			#
	#############################
	def add_film(self):
		titlu_film = self.LE_ANM_Titlu.text()
		# NULL Test
		if titlu_film == "":
			self.openDialogBox('Titlul este invalid! Trebuie sa fie diferit de NULL!', 'warning')
			return

		an_ap_film = self.LE_ANM_AnAparitie.text()
		if not an_ap_film.isdigit():
			self.openDialogBox('Introdu un an valid!')
			return
		an_ap_film = int(an_ap_film)

		gen_film = self.comboBoxAdd_Gen.currentText()

		nume_actor = self.comboBoxAdd_Actor.currentText()
		cursor.execute("select id_actor, nume, prenume from actori")
		for elem in cursor:
			if str(elem[1]) + ' ' + str(elem[2]) == nume_actor:
				id_actor_film = int(elem[0])
				break

		nume_regizor = self.comboBoxAdd_Regizor.currentText()
		cursor.execute("select id_regizor, nume, prenume from regizori")
		for elem in cursor:
			if str(elem[1]) + ' ' + str(elem[2]) == nume_regizor:
				id_regizor_film = int(elem[0])
				break

		cursor.execute(
			"INSERT INTO filme(titlu, an_aparitie, gen, actori_id_actor, regizori_id_regizor, isTop) " +
			"VALUES(:1, :2, :3, :4, :5, :6)",
			(titlu_film, an_ap_film, gen_film, id_actor_film, id_regizor_film, 0)
		)
		connection.commit()

		self.openDialogBox('Film adaugat!')
		self.LE_ANM_Titlu.setText("")
		self.LE_ANM_AnAparitie.setText("")

	def add_actor(self):
		nume_actor = self.LE_ANA_Nume.text()
		# NULL Test
		if nume_actor == "":
			self.openDialogBox('Numele este invalid! Trebuie sa fie diferit de NULL!', 'warning')
			return

		if len(nume_actor) < 2:
			windowVar.openDialogBox('Numele este prea scurt! Trebuie sa aiba cel putin 2 litere.', 'warning')
			return

		for char in nume_actor:
			if char.isdigit():
				self.openDialogBox('Numele este invalid! Nu ar trebui sa contina cifre!', 'warning')
				return
			if not char.isalpha() and not char.isdigit():
				self.openDialogBox('Numele este invalid! Nu ar trebui sa contina simboluri!', 'warning')

		prenume_actor = self.LE_ANA_Prenume.text()
		if prenume_actor != "":
			for char in prenume_actor:
				if char.isdigit():
					self.openDialogBox('Prenumele este invalid! Nu ar trebui sa contina cifre!', 'warning')
					return
				if not char.isalpha() and not char.isdigit():
					self.openDialogBox('Prenumele este invalid! Nu ar trebui sa contina simboluri!', 'warning')

		an = self.comboBoxA_an.currentText()
		luna = self.comboBoxA_luna.currentText()
		zi = self.comboBoxA_zi.currentText()
		data_nasterii_actor = an + '-' + luna[1:3] + '-' + zi

		try:
			datetime.datetime(int(an), int(luna[1:3]), int(zi))
		except ValueError:
			self.openDialogBox('Data de nastere nu este valida! Verifica ziua!', 'warning')
			return

		cursor.execute(
			"INSERT INTO actori(nume, prenume, data_nasterii) VALUES(:1, :2, TO_DATE(:3, 'YYYY-MM-DD'))",
			(nume_actor, prenume_actor, data_nasterii_actor)
		)
		connection.commit()

		self.openDialogBox('Actor adaugat!')
		self.LE_ANA_Nume.setText("")
		self.LE_ANA_Prenume.setText("")

	def add_regizor(self):
		nume_regizor = self.LE_ANMD_Nume.text()
		# NULL Test
		if nume_regizor == "":
			self.openDialogBox('Numele este invalid! Trebuie sa fie diferit de NULL!', 'warning')
			return

		if len(nume_regizor) < 2:
			windowVar.openDialogBox('Numele este prea scurt! Trebuie sa aiba cel putin 2 litere.', 'warning')
			return

		for char in nume_regizor:
			if char.isdigit():
				self.openDialogBox('Numele este invalid! Nu ar trebui sa contina cifre!', 'warning')
				return
			if not char.isalpha() and not char.isdigit():
				self.openDialogBox('Numele este invalid! Nu ar trebui sa contina simboluri!', 'warning')

		prenume_regizor = self.LE_ANMD_Prenume.text()
		if prenume_regizor != "":
			for char in prenume_regizor:
				if char.isdigit():
					self.openDialogBox('Prenumele este invalid! Nu ar trebui sa contina cifre!', 'warning')
					return
				if not char.isalpha() and not char.isdigit():
					self.openDialogBox('Prenumele este invalid! Nu ar trebui sa contina simboluri!', 'warning')

		an = self.comboBoxR_an.currentText()
		luna = self.comboBoxR_luna.currentText()
		zi = self.comboBoxR_zi.currentText()
		data_nasterii_regizor = an + '-' + luna[1:3] + '-' + zi

		try:
			datetime.datetime(int(an), int(luna[1:3]), int(zi))
		except ValueError:
			self.openDialogBox('Data de nastere nu este valida! Verifica ziua!', 'warning')
			return

		cursor.execute(
			"INSERT INTO regizori(nume, prenume, data_nasterii) VALUES(:1, :2, TO_DATE(:3, 'YYYY-MM-DD'))",
			(nume_regizor, prenume_regizor, data_nasterii_regizor)
		)
		connection.commit()

		self.openDialogBox('Regizor adaugat!')
		self.LE_ANMD_Nume.setText("")
		self.LE_ANMD_Prenume.setText("")

	def add_favorite(self):
		nume_film = self.comboBoxAdd_Fav.currentText()

		cursor.execute("select id_film, titlu from filme")
		for elem in cursor:
			if str(elem[1]) == nume_film:
				cursor2.execute("select filme_id_film from favorite")
				for elem2 in cursor2:
					if int(elem2[0]) == int(elem[0]):
						self.openDialogBox('Film deja existent in lista ta de favorite!', 'warning')
						return

		cursor.execute("select id_film, titlu from filme")
		for elem in cursor:
			if str(elem[1]) == nume_film:
				id_favMovie = int(elem[0])
				break

		# Adauga filmul in lista de favorite
		cursor.execute(f"INSERT INTO favorite SELECT f.id_film FROM filme f WHERE f.id_film = {id_favMovie}")
		connection.commit()

		self.openDialogBox('Film adaugat in lista de favorite!')

	#############################
	# 			WINDOW			#
	#############################
	def minimize(self):
		self.showMinimized()

	def maximize(self):
		self.showFullScreen()

	def restore(self):
		if self.isFullScreen():
			self.resize(1000, 600)

	def closeApp(self):
		self.close()
		exit()

	#############################
	# 			MODIFY			#
	#############################
	def editEntry(self, rowType: str, *args):
		print(rowType)
		print(args)
		self.openDialogInput(rowType, args)
		if not self.confirmUpdate:
			return
		if rowType == 'movie':
			cursor.execute(
				"UPDATE filme SET titlu = :1, an_aparitie = :2, gen = :3 WHERE id_film = :4",
				(self.movieData['Titlu'], self.movieData['AnAparitie'], self.movieData['Gen'], args[0])
			)
			connection.commit()
			self.refreshAllGenres()
		elif rowType == 'actor':
			cursor.execute(
				"UPDATE actori SET nume = :1, prenume = :2, data_nasterii = TO_DATE(:3, 'YYYY-MM-DD') WHERE id_actor = :4",
				(self.actorData['Nume'], self.actorData['Prenume'], self.actorData['DataNasterii'], args[0])
			)
			connection.commit()
			self.refresh_actors()
		elif rowType == 'moviedirector':
			cursor.execute(
				"UPDATE regizori SET nume = :1, prenume = :2, data_nasterii = TO_DATE(:3, 'YYYY-MM-DD') WHERE id_regizor = :4",
				(self.regizorData['Nume'], self.regizorData['Prenume'], self.regizorData['DataNasterii'], args[0])
			)
			connection.commit()
			self.refresh_movieDirectors()
		self.confirmUpdate = False
		print('am trecut de confirm')

	def deleteEntry(self, rowType: str, *args):
		print(rowType)
		print(args)
		if rowType == 'movie':
			cursor.execute("select gen from filme where id_film = :1", (args[0],))
			for e in cursor:
				gen = e[0]
			cursor.execute("DELETE FROM filme WHERE :1 = id_film", (args[0],))
			connection.commit()
			self.refresh_genrePage(gen)
		elif rowType == 'actor':
			if args[3] > 0:
				self.openDialogBox('Nu se poate sterge actorul! El joaca intr-ul film din baza de date!', 'warning')
				return
			cursor.execute("DELETE FROM actori WHERE :1 = id_actor", (args[0],))
			connection.commit()
			self.refresh_actors()
		elif rowType == 'moviedirector':
			if args[3] > 0:
				self.openDialogBox('Nu se poate sterge regizorul! El a facut un film care se afla in baza de date!', 'warning')
				return
			cursor.execute("DELETE FROM regizori WHERE :1 = id_regizor", (args[0],))
			connection.commit()
			self.refresh_movieDirectors()
		elif rowType == 'fav':
			cursor.execute("DELETE FROM favorite WHERE :1 = filme_id_film", (args[0],))
			connection.commit()
			self.refresh_fav()

	#############################
	# 			STATIC			#
	#############################
	@staticmethod
	def makeRow(edit: bool, delete: bool, rowType: str, sizes: list, *args):
		hlayout = QHBoxLayout()
		sizei = 0
		for arg in args:
			label = QLabel()
			label.setText(str(arg))
			label.setStyleSheet("color:white; font: 10pt 'Imprint MT Shadow';")
			if sizes[sizei] > 0:
				label.setMaximumSize(sizes[sizei], 40)
				label.setMinimumSize(sizes[sizei], 40)
			elif sizes[sizei] == 0:
				label.setMinimumSize(200, 40)
				label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
			elif sizes[sizei] == -1:
				label.setMinimumSize(400, 40)
				label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
			hlayout.addWidget(label)
			sizei += 1

		if edit:
			if not rowType == 'title':
				editB = QPushButton()
				editB.setText("Edit")
				editB.setStyleSheet(
					"""
					QPushButton {
						background-color:rgb(170, 85, 255); 
						border-radius: 3px;	
						font: 8pt "Imprint MT Shadow";
					}
					QPushButton:hover {
						border: 5px solid rgb(170, 85, 255); 
						background-color: rgb(185, 134, 255);
						font: 8pt "Imprint MT Shadow";
					}"""
				)
				editB.setMinimumSize(50, 30)
				editB.setMaximumSize(50, 30)
				editB.clicked.connect(lambda: windowVar.editEntry(rowType, *args))

				hlayout.addWidget(editB)
			else:
				w = QWidget()
				w.setMinimumSize(50, 30)
				w.setMaximumSize(50, 30)
				hlayout.addWidget(w)

		if delete:
			if not rowType == 'title':
				deleteB = QPushButton()
				deleteB.setText("Delete")
				deleteB.setStyleSheet(
					"""
					QPushButton {
						background-color:rgb(170, 85, 255); 
						border-radius: 3px;	
						font: 8pt "Imprint MT Shadow";
					}
					QPushButton:hover {
						border: 5px solid rgb(170, 85, 255); 
						background-color: rgb(185, 134, 255);
						font: 8pt "Imprint MT Shadow";
					}"""
				)
				deleteB.setMinimumSize(50, 30)
				deleteB.setMaximumSize(50, 30)
				deleteB.clicked.connect(lambda: windowVar.deleteEntry(rowType, *args))
				hlayout.addWidget(deleteB)
			else:
				w = QWidget()
				w.setMinimumSize(50, 30)
				w.setMaximumSize(50, 30)
				hlayout.addWidget(w)

		return hlayout

	@staticmethod
	def openDialogBox(mesaj: str, severity: str = "info"):
		msg = QMessageBox()
		msg.setText(mesaj)
		msg.setStandardButtons(QMessageBox.Ok)
		if severity == "info":
			msg.setIcon(QMessageBox.Information)
			msg.setWindowTitle("Informatie")
		elif severity == "warning":
			msg.setIcon(QMessageBox.Warning)
			msg.setWindowTitle("Atentie!")
		elif severity == "error":
			msg.setIcon(QMessageBox.Critical)
			msg.setWindowTitle("Eroare!")

		msg.exec_()

	def openDialogInput(self, rowType: str, data):
		if rowType == 'movie':
			dialog = DialogMovie(rowType, data, self)
			dialog.exec_()
		else:
			dialog = DialogAR(rowType, data, self)
			dialog.exec_()

#Clasa Dialog pentru actori si regizori
class DialogAR(QDialog, Ui_DialogEAR):
	def __init__(self, typeDialog: str, data: list, parent=None):
		super(DialogAR, self).__init__(parent)
		self.setupUi(self)
		for i in range(1920, 2020):
			self.comboBoxDA_an.addItem(str(i))
		self.convertDate = {
			1: '(01) Ianuarie',
			2: '(02) Februarie',
			3: '(03) Martie',
			4: '(04) Aprilie',
			5: '(05) Mai',
			6: '(06) Iunie',
			7: '(07) Iulie',
			8: '(08) August',
			9: '(09) Septembrie',
			10: '(10) Octombrie',
			11: '(11) Noiembrie',
			12: '(12) Decembrie'
		}
		self.CBD_OK.clicked.connect(self.pressedOk)
		self.CBD_Cancel.clicked.connect(self.pressedCancel)
		self.typeDialog = typeDialog  # Is actor or movie director
		self.data = data

		self.initFirstData()

#Copiaza datele trimise in campuri
	def initFirstData(self):
		# Convert the data from the row we are trying to edit
		self.name = self.data[1].split()  # Nume si prenume

		if self.data[2] != 'Indisponibil':
			self.date = datetime.datetime.strptime(self.data[2], '%d-%b-%y')
			if self.date.year > datetime.datetime.today().year:
				self.date = self.date.replace(year=self.date.year - 100)
			self.comboBoxDA_an.setCurrentIndex(self.comboBoxDA_an.findText(str(self.date.year)))
			self.comboBoxDA_zi.setCurrentIndex(self.comboBoxDA_zi.findText(str(self.date.day).zfill(2)))
			self.comboBoxDA_luna.setCurrentIndex(self.comboBoxDA_luna.findText(self.convertDate[self.date.month]))
		self.LE_nume.setText(self.name[0])
		self.LE_prenume.setText(self.name[1])

	def pressedOk(self):
		windowVar.confirmUpdate = True
		nume = self.LE_nume.text()
		if nume == "":
			windowVar.openDialogBox('Numele este invalid! Trebuie sa fie diferit de NULL!', 'warning')
			return
		if len(nume) < 2:
			windowVar.openDialogBox('Numele este prea scurt! Trebuie sa aiba cel putin 2 litere.', 'warning')
			return
		for char in nume:
			if char.isdigit():
				windowVar.openDialogBox('Numele este invalid! Nu ar trebui sa contina cifre!', 'warning')
				return
			if not char.isalpha() and not char.isdigit():
				windowVar.openDialogBox('Numele este invalid! Nu ar trebui sa contina simboluri!', 'warning')
				return

		prenume = self.LE_prenume.text()
		if prenume != "":
			for char in prenume:
				if char.isdigit():
					windowVar.openDialogBox('Prenumele este invalid! Nu ar trebui sa contina cifre!', 'warning')
					return
				if not char.isalpha() and not char.isdigit():
					windowVar.openDialogBox('Prenumele este invalid! Nu ar trebui sa contina simboluri!', 'warning')

		an = self.comboBoxDA_an.currentText()
		luna = self.comboBoxDA_luna.currentText()
		zi = self.comboBoxDA_zi.currentText()

		try:
			datetime.datetime(int(an), int(luna[1:3]), int(zi))
		except ValueError:
			windowVar.openDialogBox('Data de nastere nu este valida! Verifica ziua!', 'warning')
			return

		if self.checkBoxDN.isChecked():
			data_nasterii = an + '-' + luna[1:3] + '-' + zi
		else:
			if self.data[2] == 'Indisponibil':
				data_nasterii = None
			else:
				data_nasterii = str(self.date.year) + '-' + str(self.date.month).zfill(2) + '-' + str(self.date.day).zfill(2)

		if self.typeDialog == 'actor':
			windowVar.actorData['Nume'] = nume
			windowVar.actorData['Prenume'] = prenume
			windowVar.actorData['DataNasterii'] = data_nasterii
		elif self.typeDialog == 'moviedirector':
			windowVar.regizorData['Nume'] = nume
			windowVar.regizorData['Prenume'] = prenume
			windowVar.regizorData['DataNasterii'] = data_nasterii

		self.close()

	def pressedCancel(self):
		windowVar.confirmUpdate = False
		self.close()

class DialogMovie(QDialog, Ui_DialogEM):
	def __init__(self, typeDialog: str, data: list, parent=None):
		super(DialogMovie, self).__init__(parent)
		self.setupUi(self)

		self.CBD_OK.clicked.connect(self.pressedOk)
		self.CBD_Cancel.clicked.connect(self.pressedCancel)

		self.typeDialog = typeDialog
		self.data = data

		self.LE_titlu.setText(self.data[1])
		self.LE_anAp.setText(str(self.data[2]))

	def pressedOk(self):
		windowVar.confirmUpdate = True
		titlu = self.LE_titlu.text()
		if titlu == "":
			windowVar.openDialogBox('Titlul este invalid!', 'warning')
			return

		anAp = self.LE_anAp.text()
		if anAp == "" or not anAp.isdigit():
			windowVar.openDialogBox('Anul este invalid!', 'warning')
			return

		gen = self.comboBox.currentText()
		windowVar.movieData['Titlu'] = titlu
		windowVar.movieData['AnAparitie'] = anAp
		windowVar.movieData['Gen'] = gen

		self.close()

	def pressedCancel(self):
		windowVar.confirmUpdate = False
		self.close()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	windowVar = Window()
	windowVar.show()
	app.exec_()
