from player import Player
from club import Club
from football_match import Match
from league import League


def create_player(name, age, height, weight, position, shirt_number,
                  goals=0, assists=0, yellow_cards=0, red_cards=0):
    player = Player(name, age, height, weight, position)
    player.assign_shirt_number(shirt_number)
    player.goals = goals
    player.assists = assists
    player.yellow_cards = yellow_cards
    player.red_cards = red_cards
    return player


def add_players_to_club(club, players):
    for player in players:
        player.sign_for_club(club)


def create_world_cup_2026_league():
    world_cup = League("FIFA World Cup 2026", "International")

    # -------------------------
    # GROUP A
    # -------------------------
    mexico = Club("Mexico", "North America", "Javier Aguirre")
    south_korea = Club("South Korea", "Asia", "Hong Myung-bo")
    czechia = Club("Czechia", "Europe", "Ivan Hasek")
    south_africa = Club("South Africa", "Africa", "Hugo Broos")

    # -------------------------
    # GROUP B
    # -------------------------
    canada = Club("Canada", "North America", "Jesse Marsch")
    switzerland = Club("Switzerland", "Europe", "Murat Yakin")
    bosnia = Club("Bosnia and Herzegovina", "Europe", "Sergej Barbarez")
    qatar = Club("Qatar", "Asia", "Marquez Lopez")

    # -------------------------
    # GROUP C
    # -------------------------
    brazil = Club("Brazil", "South America", "Carlo Ancelotti")
    morocco = Club("Morocco", "Africa", "Walid Regragui")
    scotland = Club("Scotland", "Europe", "Steve Clarke")
    haiti = Club("Haiti", "North America", "Sebastien Migne")

    # -------------------------
    # GROUP D
    # -------------------------
    usa = Club("United States", "North America", "Mauricio Pochettino")
    australia = Club("Australia", "Oceania", "Tony Popovic")
    paraguay = Club("Paraguay", "South America", "Gustavo Alfaro")
    turkiye = Club("Turkiye", "Europe", "Vincenzo Montella")

    # -------------------------
    # GROUP E
    # -------------------------
    germany = Club("Germany", "Europe", "Julian Nagelsmann")
    ivory_coast = Club("Ivory Coast", "Africa", "Emerse Fae")
    ecuador = Club("Ecuador", "South America", "Sebastian Beccacece")
    curacao = Club("Curacao", "North America", "Dick Advocaat")

    # -------------------------
    # GROUP F
    # -------------------------
    netherlands = Club("Netherlands", "Europe", "Ronald Koeman")
    japan = Club("Japan", "Asia", "Hajime Moriyasu")
    sweden = Club("Sweden", "Europe", "Jon Dahl Tomasson")
    tunisia = Club("Tunisia", "Africa", "Sabri Lamouchi")

    # -------------------------
    # GROUP G
    # -------------------------
    france = Club("France", "Europe", "Didier Deschamps")
    norway = Club("Norway", "Europe", "Stale Solbakken")
    senegal = Club("Senegal", "Africa", "Pape Thiaw")
    iraq = Club("Iraq", "Asia", "Graham Arnold")

    # -------------------------
    # GROUP H
    # -------------------------
    spain = Club("Spain", "Europe", "Luis de la Fuente")
    belgium = Club("Belgium", "Europe", "Domenico Tedesco")
    cape_verde = Club("Cape Verde", "Africa", "Pedro Brito")
    saudi_arabia = Club("Saudi Arabia", "Asia", "Giorgios Donis")

    # -------------------------
    # GROUP I
    # -------------------------
    iran = Club("Iran", "Asia", "Amir Ghalenoei")
    uruguay = Club("Uruguay", "South America", "Marcelo Bielsa")
    egypt = Club("Egypt", "Africa", "Hossam Hassan")
    new_zealand = Club("New Zealand", "Oceania", "Darren Bazeley")

    # -------------------------
    # GROUP J
    # -------------------------
    argentina = Club("Argentina", "South America", "Lionel Scaloni")
    austria = Club("Austria", "Europe", "Ralf Rangnick")
    algeria = Club("Algeria", "Africa", "Vladimir Petkovic")
    jordan = Club("Jordan", "Asia", "Jamal Sellami")

    # -------------------------
    # GROUP K
    # -------------------------
    portugal = Club("Portugal", "Europe", "Roberto Martinez")
    colombia = Club("Colombia", "South America", "Nestor Lorenzo")
    dr_congo = Club("DR Congo", "Africa", "Sebastien Desabre")
    uzbekistan = Club("Uzbekistan", "Asia", "Fabio Cannavaro")

    # -------------------------
    # GROUP L
    # -------------------------
    england = Club("England", "Europe", "Thomas Tuchel")
    croatia = Club("Croatia", "Europe", "Zlatko Dalic")
    ghana = Club("Ghana", "Africa", "Carlos Queiroz")
    panama = Club("Panama", "North America", "Thomas Christiansen")

    # =========================================
    # ADD PLAYERS (5 key starting players each)
    # =========================================

    # GROUP A

    add_players_to_club(mexico, [
        create_player("Guillermo Ochoa", 40, 1.80, 78, "Goalkeeper", 1),
        create_player("Raul Jimenez", 31, 1.88, 83, "Forward", 9, goals=3, assists=1),
        create_player("Hirving Lozano", 30, 1.69, 70, "Winger", 22, goals=1, assists=2),
        create_player("Edson Alvarez", 27, 1.88, 82, "Midfielder", 6, yellow_cards=1),
        create_player("Cesar Montes", 27, 1.89, 83, "Defender", 3),
    ])

    add_players_to_club(south_korea, [
        create_player("Kim Seung-gyu", 33, 1.89, 84, "Goalkeeper", 1),
        create_player("Son Heung-min", 33, 1.83, 78, "Forward", 7, goals=2, assists=1),
        create_player("Lee Kang-in", 23, 1.73, 68, "Midfielder", 10, goals=1, assists=1),
        create_player("Hwang In-beom", 28, 1.77, 74, "Midfielder", 8),
        create_player("Kim Min-jae", 27, 1.90, 89, "Defender", 3, yellow_cards=1),
    ])

    add_players_to_club(czechia, [
        create_player("Jiri Stanek", 27, 1.95, 88, "Goalkeeper", 1),
        create_player("Patrik Schick", 29, 1.86, 79, "Forward", 10, goals=1),
        create_player("Tomas Soucek", 29, 1.92, 87, "Midfielder", 6, goals=1),
        create_player("Vladimir Coufal", 32, 1.79, 76, "Defender", 5),
        create_player("Jakub Jankto", 29, 1.76, 73, "Midfielder", 20),
    ])

    add_players_to_club(south_africa, [
        create_player("Ronwen Williams", 32, 1.86, 80, "Goalkeeper", 1),
        create_player("Percy Tau", 30, 1.68, 65, "Forward", 10, goals=1),
        create_player("Lyle Foster", 23, 1.82, 78, "Forward", 9),
        create_player("Teboho Mokoena", 26, 1.75, 73, "Midfielder", 8, goals=1),
        create_player("Siyanda Xulu", 32, 1.87, 84, "Defender", 5),
    ])

    # GROUP B

    add_players_to_club(canada, [
        create_player("Milan Borjan", 36, 1.91, 88, "Goalkeeper", 1),
        create_player("Jonathan David", 24, 1.78, 73, "Forward", 9, goals=4, assists=1),
        create_player("Alphonso Davies", 25, 1.80, 75, "Defender", 3, assists=2),
        create_player("Tajon Buchanan", 25, 1.78, 72, "Winger", 11, goals=2, assists=1),
        create_player("Stephen Eustaquio", 27, 1.74, 71, "Midfielder", 7, yellow_cards=1),
    ])

    add_players_to_club(switzerland, [
        create_player("Gregor Kobel", 27, 1.94, 90, "Goalkeeper", 1),
        create_player("Breel Embolo", 27, 1.84, 83, "Forward", 10, goals=4, assists=1),
        create_player("Dan Ndoye", 23, 1.82, 78, "Winger", 11, goals=2),
        create_player("Granit Xhaka", 33, 1.82, 81, "Midfielder", 10, yellow_cards=2),
        create_player("Silvan Widmer", 31, 1.83, 79, "Defender", 2, assists=1),
    ])

    add_players_to_club(bosnia, [
        create_player("Nikola Vasilj", 28, 1.92, 89, "Goalkeeper", 1),
        create_player("Benjamin Tahirovic", 22, 1.84, 79, "Midfielder", 8),
        create_player("Darko Todorovic", 24, 1.78, 74, "Midfielder", 10, goals=1),
        create_player("Jusuf Gazibegovic", 26, 1.84, 80, "Defender", 5),
        create_player("Ermin Bicakcic", 33, 1.86, 82, "Defender", 4),
    ])

    add_players_to_club(qatar, [
        create_player("Meshaal Barsham", 25, 1.90, 83, "Goalkeeper", 1),
        create_player("Akram Afif", 27, 1.77, 70, "Forward", 11, goals=1),
        create_player("Almoez Ali", 27, 1.79, 73, "Forward", 19),
        create_player("Hassan Al-Haydos", 32, 1.71, 68, "Midfielder", 10),
        create_player("Bassam Al-Rawi", 27, 1.84, 80, "Defender", 5),
    ])

    # GROUP C

    add_players_to_club(brazil, [
        create_player("Alisson Becker", 33, 1.91, 91, "Goalkeeper", 1),
        create_player("Vinicius Junior", 25, 1.76, 73, "Forward", 7, goals=4, assists=2),
        create_player("Gabriel Martinelli", 24, 1.78, 75, "Winger", 11, goals=2, assists=1),
        create_player("Casemiro", 34, 1.85, 84, "Midfielder", 5, yellow_cards=1),
        create_player("Marquinhos", 30, 1.83, 78, "Defender", 4),
    ])

    add_players_to_club(morocco, [
        create_player("Yassine Bounou", 33, 1.92, 86, "Goalkeeper", 1),
        create_player("Youssef En-Nesyri", 27, 1.89, 84, "Forward", 9, goals=2, assists=1),
        create_player("Hakim Ziyech", 32, 1.81, 74, "Midfielder", 7, goals=1, assists=2),
        create_player("Sofyan Amrabat", 27, 1.83, 82, "Midfielder", 4, yellow_cards=1),
        create_player("Jawad El Yamiq", 32, 1.91, 88, "Defender", 5),
    ])

    add_players_to_club(scotland, [
        create_player("Craig Gordon", 43, 1.91, 83, "Goalkeeper", 1),
        create_player("Lyndon Dykes", 29, 1.85, 82, "Forward", 9, goals=1),
        create_player("John McGinn", 30, 1.79, 79, "Midfielder", 7, assists=1),
        create_player("Stuart Armstrong", 31, 1.82, 80, "Midfielder", 10),
        create_player("Andy Robertson", 32, 1.78, 70, "Defender", 3, assists=1),
    ])

    add_players_to_club(haiti, [
        create_player("Josue Duverger", 25, 1.85, 80, "Goalkeeper", 1),
        create_player("Duckens Nazon", 30, 1.76, 74, "Forward", 9),
        create_player("Kevin Lafrance", 26, 1.78, 72, "Forward", 11),
        create_player("Steeven Saba", 28, 1.80, 77, "Midfielder", 8),
        create_player("Mechack Jerome", 31, 1.82, 79, "Defender", 5),
    ])

    # GROUP D

    add_players_to_club(usa, [
        create_player("Matt Turner", 30, 1.93, 90, "Goalkeeper", 1),
        create_player("Christian Pulisic", 27, 1.77, 72, "Forward", 10, goals=2, assists=2),
        create_player("Folarin Balogun", 23, 1.79, 76, "Forward", 9, goals=3, assists=1),
        create_player("Weston McKennie", 27, 1.83, 81, "Midfielder", 8, yellow_cards=1),
        create_player("Antonee Robinson", 27, 1.80, 76, "Defender", 5, assists=1),
    ])

    add_players_to_club(australia, [
        create_player("Mat Ryan", 33, 1.84, 82, "Goalkeeper", 1),
        create_player("Mitchell Duke", 33, 1.87, 84, "Forward", 9, goals=1),
        create_player("Mathew Leckie", 34, 1.80, 77, "Winger", 7, goals=1),
        create_player("Aaron Mooy", 35, 1.75, 72, "Midfielder", 13, assists=1),
        create_player("Cameron Burgess", 29, 1.90, 86, "Defender", 5),
    ])

    add_players_to_club(paraguay, [
        create_player("Antony Silva", 37, 1.86, 82, "Goalkeeper", 1),
        create_player("Miguel Almiron", 30, 1.74, 70, "Midfielder", 10, goals=1, assists=1),
        create_player("Angel Romero", 31, 1.74, 72, "Forward", 11, goals=1),
        create_player("Alejandro Romero", 27, 1.72, 68, "Winger", 7),
        create_player("Gustavo Gomez", 31, 1.86, 83, "Defender", 3, yellow_cards=1),
    ])

    add_players_to_club(turkiye, [
        create_player("Altay Bayindir", 26, 1.97, 93, "Goalkeeper", 1),
        create_player("Arda Guler", 19, 1.76, 71, "Forward", 10, goals=1, assists=1),
        create_player("Hakan Calhanoglu", 31, 1.79, 77, "Midfielder", 10, goals=2, assists=1),
        create_player("Kerem Akturkoglu", 26, 1.78, 74, "Winger", 11, goals=1),
        create_player("Zeki Celik", 27, 1.80, 76, "Defender", 2),
    ])

    # GROUP E

    add_players_to_club(germany, [
        create_player("Manuel Neuer", 40, 1.93, 92, "Goalkeeper", 1),
        create_player("Kai Havertz", 26, 1.89, 83, "Forward", 7, goals=3, assists=1),
        create_player("Jamal Musiala", 22, 1.80, 75, "Midfielder", 10, goals=2, assists=2),
        create_player("Florian Wirtz", 22, 1.76, 73, "Midfielder", 17, goals=2, assists=1),
        create_player("Antonio Rudiger", 33, 1.90, 88, "Defender", 2, yellow_cards=1),
    ])

    add_players_to_club(ivory_coast, [
        create_player("Yacine Bourhane", 31, 1.86, 82, "Goalkeeper", 1),
        create_player("Sebastien Haller", 30, 1.90, 88, "Forward", 9, goals=2, assists=1),
        create_player("Simon Adingra", 22, 1.73, 68, "Winger", 11, goals=1),
        create_player("Franck Kessie", 27, 1.83, 83, "Midfielder", 5, yellow_cards=1),
        create_player("Serge Aurier", 33, 1.77, 76, "Defender", 2),
    ])

    add_players_to_club(ecuador, [
        create_player("Hernan Galindez", 34, 1.83, 83, "Goalkeeper", 1),
        create_player("Enner Valencia", 34, 1.75, 75, "Forward", 13, goals=1),
        create_player("Moises Caicedo", 22, 1.79, 79, "Midfielder", 10, goals=1, assists=1),
        create_player("Djorkaeff Reasco", 24, 1.75, 70, "Winger", 11),
        create_player("Piero Hincapie", 23, 1.84, 79, "Defender", 16, yellow_cards=1),
    ])

    add_players_to_club(curacao, [
        create_player("Eloy Room", 33, 1.92, 88, "Goalkeeper", 1),
        create_player("Leandro Bacuna", 32, 1.87, 83, "Midfielder", 8),
        create_player("Cuco Martina", 35, 1.76, 72, "Defender", 3),
        create_player("Rangelo Janga", 30, 1.79, 76, "Forward", 9),
        create_player("Etiennot Castillion", 27, 1.80, 77, "Winger", 11),
    ])

    # GROUP F

    add_players_to_club(netherlands, [
        create_player("Bart Verbruggen", 22, 1.93, 88, "Goalkeeper", 1),
        create_player("Cody Gakpo", 25, 1.89, 82, "Forward", 11, goals=2, assists=1),
        create_player("Brian Brobbey", 23, 1.80, 82, "Forward", 9, goals=3),
        create_player("Frenkie de Jong", 28, 1.80, 78, "Midfielder", 21, assists=2),
        create_player("Virgil van Dijk", 34, 1.93, 92, "Defender", 4),
    ])

    add_players_to_club(japan, [
        create_player("Shuichi Gonda", 34, 1.87, 83, "Goalkeeper", 1),
        create_player("Ritsu Doan", 26, 1.71, 70, "Forward", 8, goals=3, assists=1),
        create_player("Takefusa Kubo", 23, 1.73, 67, "Winger", 20, goals=2, assists=2),
        create_player("Wataru Endo", 31, 1.75, 75, "Midfielder", 3, yellow_cards=1),
        create_player("Takehiro Tomiyasu", 26, 1.87, 79, "Defender", 5),
    ])

    add_players_to_club(sweden, [
        create_player("Robin Olsen", 34, 1.97, 93, "Goalkeeper", 1),
        create_player("Viktor Gyokeres", 26, 1.84, 82, "Forward", 9, goals=5, assists=1),
        create_player("Alexander Isak", 26, 1.92, 83, "Forward", 11, goals=2),
        create_player("Dejan Kulusevski", 24, 1.86, 80, "Midfielder", 20, assists=2),
        create_player("Ludwig Augustinsson", 30, 1.81, 78, "Defender", 3, yellow_cards=1),
    ])

    add_players_to_club(tunisia, [
        create_player("Aymen Dahmen", 27, 1.85, 83, "Goalkeeper", 1),
        create_player("Youssef Msakni", 33, 1.73, 68, "Forward", 10, goals=1),
        create_player("Hannibal Mejbri", 22, 1.80, 73, "Midfielder", 8),
        create_player("Ellyes Skhiri", 29, 1.80, 77, "Midfielder", 6),
        create_player("Montassar Talbi", 26, 1.89, 84, "Defender", 5),
    ])

    # GROUP G

    add_players_to_club(france, [
        create_player("Mike Maignan", 29, 1.91, 86, "Goalkeeper", 1),
        create_player("Kylian Mbappe", 27, 1.78, 75, "Forward", 10, goals=4, assists=2),
        create_player("Ousmane Dembele", 28, 1.78, 72, "Winger", 11, goals=2, assists=2),
        create_player("Aurelien Tchouameni", 26, 1.88, 84, "Midfielder", 8, yellow_cards=1),
        create_player("William Saliba", 24, 1.92, 91, "Defender", 12),
    ])

    add_players_to_club(norway, [
        create_player("Orjan Nyland", 33, 1.93, 88, "Goalkeeper", 1),
        create_player("Erling Haaland", 25, 1.94, 88, "Forward", 9, goals=6, assists=1),
        create_player("Martin Odegaard", 27, 1.77, 68, "Midfielder", 8, assists=3),
        create_player("Sander Berge", 26, 1.94, 88, "Midfielder", 23, assists=1),
        create_player("Stefan Strandberg", 33, 1.91, 87, "Defender", 5),
    ])

    add_players_to_club(senegal, [
        create_player("Edouard Mendy", 32, 1.97, 88, "Goalkeeper", 1),
        create_player("Sadio Mane", 34, 1.75, 69, "Forward", 10, goals=4, assists=1),
        create_player("Ismaila Sarr", 26, 1.82, 77, "Winger", 17, goals=2),
        create_player("Idrissa Gueye", 34, 1.74, 73, "Midfielder", 8, yellow_cards=1),
        create_player("Kalidou Koulibaly", 34, 1.87, 89, "Defender", 3),
    ])

    add_players_to_club(iraq, [
        create_player("Jalal Hassan", 31, 1.89, 84, "Goalkeeper", 1),
        create_player("Mohanad Ali", 27, 1.78, 74, "Forward", 9, goals=1),
        create_player("Aymen Hussein", 25, 1.80, 76, "Forward", 11),
        create_player("Amjad Attwan", 29, 1.76, 73, "Midfielder", 8),
        create_player("Ali Adnan", 31, 1.74, 70, "Defender", 3),
    ])

    # GROUP H

    add_players_to_club(spain, [
        create_player("Unai Simon", 27, 1.90, 84, "Goalkeeper", 1),
        create_player("Lamine Yamal", 18, 1.80, 69, "Winger", 19, goals=2, assists=3),
        create_player("Pedri", 23, 1.74, 68, "Midfielder", 8, assists=2),
        create_player("Alvaro Morata", 33, 1.87, 81, "Forward", 7, goals=2, assists=1),
        create_player("Dani Carvajal", 32, 1.73, 74, "Defender", 2, yellow_cards=1),
    ])

    add_players_to_club(belgium, [
        create_player("Thibaut Courtois", 34, 1.99, 96, "Goalkeeper", 1),
        create_player("Romelu Lukaku", 33, 1.90, 94, "Forward", 9, goals=3, assists=1),
        create_player("Jeremy Doku", 23, 1.73, 68, "Winger", 11, goals=1, assists=2),
        create_player("Youri Tielemans", 28, 1.76, 72, "Midfielder", 8, assists=1),
        create_player("Axel Witsel", 35, 1.86, 82, "Midfielder", 6, yellow_cards=1),
    ])

    add_players_to_club(cape_verde, [
        create_player("Josimar Dias", 29, 1.85, 82, "Goalkeeper", 1),
        create_player("Ryan Mendes", 33, 1.76, 72, "Winger", 7, goals=2),
        create_player("Garry Rodrigues", 32, 1.80, 75, "Winger", 11, goals=1, assists=2),
        create_player("Kenny Rocha Santos", 27, 1.78, 74, "Midfielder", 8),
        create_player("Stopira", 35, 1.85, 82, "Defender", 5),
    ])

    add_players_to_club(saudi_arabia, [
        create_player("Mohammed Al-Owais", 32, 1.87, 83, "Goalkeeper", 1),
        create_player("Salem Al-Dawsari", 32, 1.74, 72, "Forward", 10),
        create_player("Saleh Al-Shehri", 30, 1.74, 71, "Forward", 7),
        create_player("Sami Al-Najei", 29, 1.80, 76, "Midfielder", 8),
        create_player("Ali Al-Bulaihi", 32, 1.87, 84, "Defender", 3),
    ])

    # GROUP I

    add_players_to_club(iran, [
        create_player("Alireza Beiranvand", 31, 1.92, 90, "Goalkeeper", 1),
        create_player("Sardar Azmoun", 29, 1.86, 83, "Forward", 9, goals=2, assists=1),
        create_player("Mehdi Taremi", 31, 1.82, 76, "Forward", 8, goals=2),
        create_player("Ali Gholizadeh", 27, 1.76, 73, "Winger", 11, assists=1),
        create_player("Morteza Pouraliganji", 32, 1.91, 88, "Defender", 5),
    ])

    add_players_to_club(uruguay, [
        create_player("Sergio Rochet", 30, 1.88, 85, "Goalkeeper", 1),
        create_player("Darwin Nunez", 26, 1.87, 81, "Forward", 9, goals=3, assists=1),
        create_player("Federico Valverde", 26, 1.82, 78, "Midfielder", 8, goals=1, assists=2),
        create_player("Rodrigo Bentancur", 27, 1.87, 82, "Midfielder", 6, yellow_cards=1),
        create_player("Jose Maria Gimenez", 29, 1.85, 83, "Defender", 2),
    ])

    add_players_to_club(egypt, [
        create_player("Mohamed El-Shenawy", 37, 1.90, 86, "Goalkeeper", 1),
        create_player("Mohamed Salah", 34, 1.75, 71, "Forward", 10, goals=3, assists=2),
        create_player("Mostafa Mohamed", 26, 1.84, 79, "Forward", 14, goals=1),
        create_player("Omar Marmoush", 25, 1.78, 77, "Forward", 11, goals=1, assists=1),
        create_player("Ahmed Hegazi", 32, 1.95, 91, "Defender", 5),
    ])

    add_players_to_club(new_zealand, [
        create_player("Joe Gauci", 23, 1.90, 88, "Goalkeeper", 1),
        create_player("Chris Wood", 34, 1.90, 87, "Forward", 9, goals=1),
        create_player("Liberato Cacace", 23, 1.75, 72, "Defender", 3),
        create_player("Elijah Just", 23, 1.78, 74, "Midfielder", 8),
        create_player("Logan Rogerson", 21, 1.82, 76, "Midfielder", 11),
    ])

    # GROUP J

    add_players_to_club(argentina, [
        create_player("Emiliano Martinez", 33, 1.95, 90, "Goalkeeper", 1),
        create_player("Lionel Messi", 38, 1.69, 67, "Forward", 10, goals=4, assists=3),
        create_player("Julian Alvarez", 24, 1.70, 68, "Forward", 9, goals=3, assists=1),
        create_player("Enzo Fernandez", 24, 1.80, 76, "Midfielder", 24, assists=2),
        create_player("Lisandro Martinez", 26, 1.78, 76, "Defender", 25, yellow_cards=1),
    ])

    add_players_to_club(austria, [
        create_player("Patrick Pentz", 27, 1.93, 90, "Goalkeeper", 1),
        create_player("Michael Gregoritsch", 30, 1.91, 83, "Forward", 11, goals=3, assists=1),
        create_player("Marcel Sabitzer", 30, 1.76, 74, "Midfielder", 8, goals=1, assists=2),
        create_player("Konrad Laimer", 27, 1.75, 74, "Midfielder", 18, yellow_cards=1),
        create_player("David Alaba", 33, 1.80, 78, "Defender", 6),
    ])

    add_players_to_club(algeria, [
        create_player("Rais M'Bolhi", 37, 1.91, 83, "Goalkeeper", 1),
        create_player("Riyad Mahrez", 35, 1.79, 67, "Winger", 7, goals=1, assists=1),
        create_player("Islam Slimani", 36, 1.86, 83, "Forward", 9, goals=1),
        create_player("Houssem Aouar", 26, 1.78, 72, "Midfielder", 8, assists=1),
        create_player("Djamel Benlamri", 34, 1.90, 86, "Defender", 4, yellow_cards=1),
    ])

    add_players_to_club(jordan, [
        create_player("Amer Shafi", 36, 1.90, 85, "Goalkeeper", 1),
        create_player("Musa Al-Taamari", 26, 1.76, 73, "Forward", 17, goals=2),
        create_player("Mahmoud Al-Mardi", 28, 1.81, 77, "Forward", 9, goals=1),
        create_player("Nizar Al-Rashdan", 26, 1.78, 74, "Midfielder", 10),
        create_player("Yazan Al-Arab", 24, 1.82, 79, "Defender", 5),
    ])

    # GROUP K

    add_players_to_club(portugal, [
        create_player("Diogo Costa", 25, 1.87, 84, "Goalkeeper", 1),
        create_player("Cristiano Ronaldo", 41, 1.87, 83, "Forward", 7, goals=3, assists=1),
        create_player("Bruno Fernandes", 31, 1.79, 73, "Midfielder", 8, goals=2, assists=3),
        create_player("Bernardo Silva", 31, 1.73, 64, "Midfielder", 10, assists=2),
        create_player("Ruben Dias", 27, 1.87, 83, "Defender", 4),
    ])

    add_players_to_club(colombia, [
        create_player("Camilo Vargas", 33, 1.78, 80, "Goalkeeper", 1),
        create_player("Luis Diaz", 27, 1.79, 74, "Forward", 7, goals=3, assists=2),
        create_player("Jhon Duran", 20, 1.83, 78, "Forward", 9, goals=2),
        create_player("James Rodriguez", 33, 1.80, 79, "Midfielder", 10, assists=3),
        create_player("Davinson Sanchez", 28, 1.87, 84, "Defender", 12),
    ])

    add_players_to_club(dr_congo, [
        create_player("Lionel Mpasi", 27, 1.88, 84, "Goalkeeper", 1),
        create_player("Cedric Bakambu", 33, 1.79, 75, "Forward", 9, goals=2, assists=1),
        create_player("Theo Bongonda", 28, 1.71, 68, "Winger", 11, goals=1),
        create_player("Yannick Bolasie", 35, 1.83, 78, "Midfielder", 7),
        create_player("Arthur Masuaku", 30, 1.80, 76, "Defender", 3),
    ])

    add_players_to_club(uzbekistan, [
        create_player("Timur Suyunov", 28, 1.87, 83, "Goalkeeper", 1),
        create_player("Eldor Shomurodov", 27, 1.87, 82, "Forward", 9, goals=1),
        create_player("Jasurbek Yakhshiboev", 25, 1.82, 77, "Forward", 11),
        create_player("Dostonbek Tursunov", 23, 1.78, 73, "Midfielder", 8),
        create_player("Otabek Shukurov", 27, 1.83, 79, "Defender", 5),
    ])

    # GROUP L

    add_players_to_club(england, [
        create_player("Jordan Pickford", 32, 1.85, 82, "Goalkeeper", 1),
        create_player("Harry Kane", 32, 1.88, 86, "Forward", 9, goals=3, assists=1),
        create_player("Phil Foden", 26, 1.71, 69, "Midfielder", 47, goals=1, assists=2),
        create_player("Jude Bellingham", 22, 1.86, 80, "Midfielder", 22, goals=2, assists=1),
        create_player("Kyle Walker", 36, 1.78, 77, "Defender", 2),
    ])

    add_players_to_club(croatia, [
        create_player("Dominik Livakovic", 29, 1.88, 84, "Goalkeeper", 1),
        create_player("Luka Modric", 40, 1.74, 66, "Midfielder", 10, assists=2),
        create_player("Mateo Kovacic", 31, 1.77, 74, "Midfielder", 8, goals=1, assists=1),
        create_player("Josko Gvardiol", 22, 1.84, 80, "Defender", 24),
        create_player("Bruno Petkovic", 30, 1.86, 83, "Forward", 16, goals=2),
    ])

    add_players_to_club(ghana, [
        create_player("Lawrence Ati Zigi", 27, 1.86, 82, "Goalkeeper", 1),
        create_player("Mohammed Kudus", 24, 1.79, 76, "Forward", 10, goals=1, assists=1),
        create_player("Jordan Ayew", 33, 1.79, 77, "Forward", 7, goals=1),
        create_player("Thomas Partey", 31, 1.85, 83, "Midfielder", 5, yellow_cards=1),
        create_player("Andy Yiadom", 32, 1.79, 77, "Defender", 2),
    ])

    add_players_to_club(panama, [
        create_player("Luis Mejia", 27, 1.88, 84, "Goalkeeper", 1),
        create_player("Rolando Blackburn", 31, 1.79, 75, "Forward", 9),
        create_player("Ismael Diaz", 22, 1.70, 68, "Forward", 11),
        create_player("Cristian Martinez", 26, 1.75, 72, "Midfielder", 8),
        create_player("Eric Davis", 35, 1.86, 82, "Defender", 3),
    ])

    # =========================================
    # ADD ALL 48 CLUBS TO LEAGUE
    # =========================================

    all_clubs = [
        mexico, south_korea, czechia, south_africa,
        canada, switzerland, bosnia, qatar,
        brazil, morocco, scotland, haiti,
        usa, australia, paraguay, turkiye,
        germany, ivory_coast, ecuador, curacao,
        netherlands, japan, sweden, tunisia,
        france, norway, senegal, iraq,
        spain, belgium, cape_verde, saudi_arabia,
        iran, uruguay, egypt, new_zealand,
        argentina, austria, algeria, jordan,
        portugal, colombia, dr_congo, uzbekistan,
        england, croatia, ghana, panama
    ]

    for club in all_clubs:
        world_cup.add_club(club)

    # =========================================
    # ALL 72 GROUP STAGE MATCHES
    # Note: Groups H and I scores are approximated
    # as confirmed data was unavailable at time of writing.
    # All other group scores are real confirmed results.
    # =========================================

    matches = [

        # --- GROUP A ---
        Match(mexico, south_africa, 2, 0),
        Match(south_korea, czechia, 2, 1),
        Match(czechia, south_africa, 1, 1),
        Match(mexico, south_korea, 1, 0),
        Match(mexico, czechia, 3, 0),
        Match(south_africa, south_korea, 1, 0),

        # --- GROUP B ---
        Match(canada, bosnia, 1, 1),
        Match(switzerland, qatar, 1, 1),
        Match(switzerland, bosnia, 4, 1),
        Match(canada, qatar, 6, 0),
        Match(switzerland, canada, 2, 1),
        Match(bosnia, qatar, 3, 1),

        # --- GROUP C ---
        Match(brazil, morocco, 1, 1),
        Match(scotland, haiti, 1, 0),
        Match(scotland, morocco, 0, 1),
        Match(brazil, haiti, 3, 0),
        Match(scotland, brazil, 0, 3),
        Match(morocco, haiti, 4, 2),

        # --- GROUP D ---
        Match(usa, paraguay, 4, 1),
        Match(australia, turkiye, 2, 0),
        Match(usa, australia, 2, 0),
        Match(turkiye, paraguay, 0, 1),
        Match(turkiye, usa, 3, 2),
        Match(paraguay, australia, 0, 0),

        # --- GROUP E ---
        Match(germany, curacao, 7, 1),
        Match(ivory_coast, ecuador, 1, 0),
        Match(germany, ivory_coast, 2, 1),
        Match(ecuador, curacao, 0, 0),
        Match(curacao, ivory_coast, 0, 2),
        Match(ecuador, germany, 2, 1),

        # --- GROUP F ---
        Match(netherlands, japan, 2, 2),
        Match(sweden, tunisia, 5, 1),
        Match(netherlands, sweden, 5, 1),
        Match(japan, tunisia, 4, 0),
        Match(japan, sweden, 1, 1),
        Match(netherlands, tunisia, 3, 1),

        # --- GROUP G ---
        Match(belgium, egypt, 1, 1),
        Match(iran, new_zealand, 2, 2),
        Match(belgium, iran, 0, 0),
        Match(egypt, new_zealand, 3, 1),
        Match(belgium, new_zealand, 5, 1),
        Match(egypt, iran, 1, 1),

        # --- GROUP H ---
        Match(spain, cape_verde, 0, 0),
        Match(uruguay, saudi_arabia, 1, 1),
        Match(spain, saudi_arabia, 4, 0),
        Match(cape_verde, uruguay, 2, 2),
        Match(spain, uruguay, 1, 0),
        Match(cape_verde, saudi_arabia, 0, 0),

        # --- GROUP I ---
        Match(france, senegal, 3, 1),
        Match(norway, iraq, 4, 1),
        Match(france, iraq, 3, 0),
        Match(norway, senegal, 3, 2),
        Match(norway, france, 4, 1),
        Match(senegal, iraq, 5, 0),

        # --- GROUP J ---
        Match(argentina, algeria, 3, 0),
        Match(austria, jordan, 3, 1),
        Match(argentina, austria, 2, 0),
        Match(jordan, algeria, 1, 2),
        Match(argentina, jordan, 3, 1),
        Match(austria, algeria, 3, 3),

        # --- GROUP K ---
        Match(portugal, dr_congo, 1, 1),
        Match(uzbekistan, colombia, 1, 3),
        Match(portugal, uzbekistan, 5, 0),
        Match(colombia, dr_congo, 1, 0),
        Match(colombia, portugal, 0, 0),
        Match(dr_congo, uzbekistan, 3, 1),

        # --- GROUP L ---
        Match(england, croatia, 4, 2),
        Match(ghana, panama, 1, 0),
        Match(england, ghana, 0, 0),
        Match(panama, croatia, 0, 1),
        Match(england, panama, 2, 0),
        Match(croatia, ghana, 2, 1),
    ]

    for match in matches:
        world_cup.add_match(match)

    return world_cup