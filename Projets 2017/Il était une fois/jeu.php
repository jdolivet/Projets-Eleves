<?php 

    session_start();

    if (isset($_POST['pseudo'])) {
        //Session est une variable superglobale, ce qui permettra d'utiliser le pseudo de l'utilisateur dans toutes les pages du site tant que sa session est ouverte.
        $_SESSION['statutlogin'] = "OK";
        $_SESSION['pseudo'] = htmlspecialchars($_POST['pseudo']);  
    }

    include 'head-header-menu.php'; 

    if ($_SESSION['statutlogin'] != "OK" or !isset($_SESSION)) {
?>

        <script>
            window.location.assign("formulaires.php");
        </script>

<?php
    }
?>

<!-- HTML avec les éléments qui s'afficherons -->

    <div id = "main" onclick = "FermeMenu()">
        <div id = "loader"></div>
        <h3 id = "horloge"></h3>
        <img id = "imageAffiche" onload="TestLoad('image')" src = "">
        <div id = "texteAffiche">
        </div>
    </div>

	
<!-- Partie du code en PHP qui est exécutée lorsque l'utilisateur s'inscrit ou réinitialise son mot de passe -->
    <?php
	
		//on récupère les variables envoyées par les fomulaires grâce à la méthode post
		//la fonction htmlspecialchars() empêche les utilisateurs d'insérer du code
        $pseudo = htmlspecialchars($_POST["pseudo"]);
        $mdp = htmlspecialchars($_POST["mdp"]);
        $question = htmlspecialchars($_POST["question"]);
        $reponse = htmlspecialchars($_POST["reponse"]);
        $nouv_mdp = htmlspecialchars($_POST["nouv_mdp"]);

		//Après inscription	
        //on ajoute le nouveau compte au csv des comptes si les variables sont toutes remplies
        if (($_SERVER["REQUEST_METHOD"] == "POST")&&(isset($_POST["pseudo"],$_POST["mdp"],$_POST["question"],$_POST["reponse"]))) {
            // La fonction file transforme chaque ligne d'un fichier en élément d'un array
            // La fonction array_map exécute la fonction str_csv sur chacun des élément de l'array créé grâce à file
            // La fonction str_getcsv sépare les éléments de chaque ligne en éléments d'un array
            $csv = array_map("str_getcsv", file("comptes.csv"));
            //array avec les données du compte (pseudonyme, mdp, id de question de securite, réponse de quest, état présent dans le jeu, liste de tous les choix faits)
            $nouveau_compte = array($pseudo,$mdp,$question,$reponse,"000","");
            // On rajoutte l'array du nouveau compte au csv
            array_push($csv,$nouveau_compte);
            // On transforme le $csv format array d'arrays en chaîne de caractères en format csv
            $nouveau_contenu = "";
            foreach ($csv as $ligne) {
                $nouveau_contenu .= implode(",", $ligne)."\r\n";
            };
            // On remplace le contenu du fichier comptes par le contenu modifié
            $fichier = fopen("comptes.csv", "w");
            fputs($fichier, $nouveau_contenu);
            fclose($fichier);
        }

        //Après réinitialisation mdp
        //si les variables de reinitialisation de mdp sont remplies, on modifie le mdp
        if (($_SERVER["REQUEST_METHOD"] == "POST") && (isset($_POST["pseudo"], $_POST["nouv_mdp"]))) { 
            // La fonction file transforme chaque ligne d'un fichier en élément d'un array
            // La fonction array_map exécute la fonction str_csv sur chacun des élément de l'array créé grâce à file
            // La fonction str_getcsv sépare les éléments de chaque ligne en éléments d'un array
            $csv = array_map("str_getcsv", file("comptes.csv"));
            $idCompte = 0; //on cherche à quelle ligne sont les données correspondant au pseudoyme
            foreach ($csv as $ligne) {
                if ($ligne[0] == $pseudo){
                    $csv[$idCompte][1] = $nouv_mdp; //On modifie le mdp
                    break;
                }
                ++$idCompte;
            }
            //On transforme le $csv format array d'arrays en chaîne de caractères en format csv
            $nouveau_contenu = "";
            foreach ($csv as $ligne) {
                $nouveau_contenu .= implode(",", $ligne)."\r\n";
            }
            //On remplace le contenu du fichier comptes par le contenu modifié
            $fichier = fopen("comptes.csv", "w");
            fputs($fichier, $nouveau_contenu);
            fclose($fichier);
        }
        
    ?>

<!-- Javascript du programme -->
<script>

    //Cette fonction vérifie si l'image et le texte sont tous les deux chargés avant de les afficher.
    //Cela est nécessaire car AJAX étant asynchrone les deux ne chargent pas au même moment.
    var textediff = "blabla"; 
    var imagechargee = false;
    var textecharge = false;

    function TestLoad(element) {
        if (element == "image") {
            imagechargee = true;
        } 
        //Il n'y a pas de onload pour les textes, donc on teste si le texte a déjà été modifié.
        if (textediff != document.getElementById('texteAffiche').innerHTML) { 
            textecharge = true;
        }
        if (textecharge && imagechargee) {
            document.getElementById('loader').style.display = "none";
            document.getElementById('imageAffiche').style.display = "block";
            document.getElementById('texteAffiche').style.display = "block";
        }
    }

    //Cette fonction trouve l'état actuel correspondant au pseudo de l'utilisateur sur comptes.csv
	//Cela permet de reprendre le jeu à partir de la sauvegarde
    <?php
		//On transforme le csv des comptes en array d'arrays pour le lire plus tard.
		$csv = array_map("str_getcsv", file("comptes.csv")); 
	?>

    //On transforme le array des comptes de php en array de javascript.
	JScsv = <?php echo json_encode($csv) ?>;

    function TrouveEtat() {
		//on cherche idCompte: le numéro de la ligne correspondant au pseudo
		var idCompte = 1;
		while ((JScsv[idCompte][0] != "<?php echo $_SESSION['pseudo'] ?>")&&(idCompte<JScsv.length)) {
			idCompte +=1;
		}
		//on trouve idE: l'identifiant de létat actuel avec les identifiants de texte et d'image
        var idE = JScsv[idCompte][4];
		//on récupère dans idT l'identifiant du texte
        idT = idE.slice(0,2);
		//on récupère dans idI l'identifiant de l'image
        idI = idE.slice(2);
		//on utilise la fonction ModifieEtat() pour envoyer l'utilisateur au bon état
        ModifieEtat(idT, idI);
    }

    //Cette fonction demande au serveur la prochaine image et prochain texte.
    function ModifieEtat(idTexte, idImage) {

        document.getElementById('loader').style.display = "block";
        imagechargee = false;
        textecharge = false;
        document.getElementById('imageAffiche').style.display = "none";
        document.getElementById('texteAffiche').style.display = "none";

        //On modifie l'image.
        var prochaineImage = 'images/imageX.jpg'.replace("X", idImage);
        if (document.getElementById('imageAffiche').src !== prochaineImage) {
            document.getElementById('imageAffiche').src = prochaineImage;
        }

        //On crée l'URL à demander au serveur à partir de l'état.
        prochainTexte = 'textes/texteX.txt'.replace("X", idTexte);

        var requeteTexte = CreeRequete();
        //Cette fontion anonyme va traiter le résultat à chaque fois que l'état de la requête change.
        requeteTexte.onreadystatechange = function() {
            //Si l'état de la requête vaut 4, cela veut dire que la réponse du serveur a été reçue dans son intégralité (après les étapes 0, 1, 2 et 3).
            //On vérifie ensuite le code d'état de la réponse du serveur. Le code 200 veut dire OK. 
            if (requeteTexte.readyState == 4 && requeteTexte.status == 200) {
                //responseText de la requête nous renvoie la réponse du serveur sous la forme du chaîne de texte, qu'on place dans la div "texteAffiche".
                document.getElementById("texteAffiche").innerHTML = requeteTexte.responseText;
            }
        }
        //On lance la requête avec la méthode open de l'objet XMLHttpRequest. Les paramètres correspondent, respectivement, à la méthode de requête, 
        //à l'URL de la page demandée et à true si la requête est asynchrone.
        requeteTexte.open("POST", prochainTexte, true);
        requeteTexte.send();

        var requeteTraiteEtat = CreeRequete();
        requeteTraiteEtat.open("GET", "traiteetat.php?idEtat=" + idTexte + idImage + "&pseudo=<?php echo $_SESSION['pseudo'] ?>", true);
        requeteTraiteEtat.send();

    }

    //Chaque fois que le joueur fait un choix, cette fonction l'envoie pour actualiser les statistiques et aussi ses paramètres dans comptes.csv
    function EnvoieChoix(choix) {

        var requeteSondage = CreeRequete();
        requeteSondage.open("GET", "sondage.php?choix="+choix, true);
        requeteSondage.send();

        var requeteTraiteChoix = CreeRequete();
        requeteTraiteChoix.open("GET", "traitechoix.php?choix=" + choix + "&pseudo=<?php echo $_SESSION['pseudo'] ?>", true);
        requeteTraiteChoix.send();

    }

	
    //Cette fonction crée et contrôle le mini-jeu labyrinthe.
    function Labyrinthe(idLabyrinthe) {

        document.getElementById("texteAffiche").innerHTML = "<p id = 'instructions'>À vous de jouer : utilisez les flèches du clavier pour aider notre héros à traverser la forêt d'épines. Attention au temps !</p>";
        document.getElementById("imageAffiche").src = "";

        var espaceJeu = new Object();

        espaceJeu.canvas = document.createElement("canvas");

        espaceJeu.start = function() {
            this.canvas.width = 484;
            this.canvas.height = 374;
            this.context = this.canvas.getContext("2d");
            document.getElementById("horloge").style.display = "inline-block";
            document.getElementById("main").insertBefore(espaceJeu.canvas, document.getElementById("imageAffiche"));
            this.interval = setInterval(updateEspaceJeu, 150); //l'actualisation de l'espace se fait toutes les 150 ms
            window.addEventListener('keydown', function (e) { 
                if([37, 38, 39, 40].indexOf(e.keyCode) > -1) { //37, 38, 39, 40 correspondent aux flèches du clavier.
                        e.preventDefault(); //On empêche les flèches de réaliser leur fonction par défaut, celle de scroll la page.
                    }
                    espaceJeu.key = e.keyCode;
            })
            window.addEventListener('keyup', function (e) {
                    espaceJeu.key = false;
            })
        }

        espaceJeu.clear = function() {
            this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
        }

        espaceJeu.stop = function(resultat) {
            clearInterval(this.interval);
            if (resultat == "succes") {
                document.getElementById("texteAffiche").innerHTML = "<ul><li class = 'boutonProchain' onclick = 'SuccesLabyrinthe(" + idLabyrinthe + ")'> Continuer </li></ul>";
            } else {
                document.getElementById("texteAffiche").innerHTML = "<p>Les épines se tenaient entre elles, comme par des mains. Le brave héros qui essaya de passer y resta accroché, sans pouvoir se détacher, et mourut là, d'une mort cruelle. </p><ul><li class = 'boutonProchain' onclick = 'EchecLabyrinthe(" + idLabyrinthe + ")'> Continuer </li></ul>";
            }
        }
		
		//cette fonction permet de créer les éléments du labyrinthe
        function component(largeur, hauteur, source, posx, posy) {
            this.image = new Image();
            this.image.src = source;
            this.width = largeur;
            this.height = hauteur;
            this.x = posx;
            this.y = posy;
            this.update = function() {
                ctx = espaceJeu.context;
                ctx.drawImage(this.image, 
                    this.x, 
                    this.y,
                    this.width,
                    this.height);
            }
        }
		
		espaceJeu.start();
        
		//on utilise la fonction pour créer les éléments du labyrinthe
        var murs = new component(484, 374, "images/labyrinthe.gif", 0, 0);
        var prince = new component(20, 20, "images/prince.gif", 22, 44);
        var porte = new component(20, 20, "images/fin.gif", 440 , 330);
        var temps = 150001;

        var coordonnees =[ //pour chaque case du labyrinthe, définit si le joueur peut passer (1) ou s'il y a un mur (0) (gauche, droite, haut, bas)
        [[0,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,1],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,0,0,0],[0,1,0,1],[1,1,0,0],[1,1,0,1],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,0,0,1]],
        [[0,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,1],[1,1,0,1],[1,1,0,0],[1,0,1,0],[0,0,0,1],[0,1,0,1],[1,1,0,0],[1,1,0,1],[1,1,0,0],[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,1,0,0],[1,0,0,1],[0,0,1,1]],
        [[0,1,0,1],[1,1,0,0],[1,1,0,0],[1,0,0,0],[0,0,1,1],[0,0,1,1],[0,1,0,0],[1,1,0,0],[1,0,1,1],[0,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,1,0,0],[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,0],[1,0,1,0],[0,0,1,1]],
        [[0,1,1,1],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,0,1,0],[0,1,1,0],[1,1,0,0],[1,0,0,0],[0,1,1,1],[1,1,0,0],[1,0,1,0],[0,1,0,1],[1,1,1,0],[1,1,0,0],[1,1,0,0],[1,0,1,0],[0,1,0,0],[1,1,0,0],[1,1,0,0],[1,0,1,1]],
        [[0,0,1,1],[0,1,0,1],[1,1,0,1],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,1,0],[1,1,0,0],[1,0,0,1],[0,0,1,1],[0,1,0,1],[1,1,0,0],[1,1,0,1],[1,0,0,0],[0,1,0,1],[1,1,0,0],[1,0,0,0],[0,0,1,0]],
        [[0,0,1,1],[0,0,1,1],[0,0,1,0],[0,1,0,1],[1,1,0,0],[1,1,0,0],[1,0,0,0],[0,1,0,1],[1,1,0,1],[1,0,0,0],[0,0,1,0],[0,0,1,1],[0,0,1,1],[0,0,0,1],[0,1,1,0],[1,0,0,1],[0,0,1,1],[0,1,0,1],[1,1,0,0],[1,0,0,1]],
        [[0,1,1,1],[1,1,1,0],[1,1,0,0],[1,0,1,0],[0,1,0,1],[1,1,0,1],[1,0,0,1],[0,0,1,1],[0,0,1,0],[0,1,0,1],[1,1,0,0],[1,1,1,0],[1,0,1,0],[0,1,1,1],[1,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,1,0],[1,0,0,1],[0,0,1,1]],
        [[0,1,1,0],[1,0,0,0],[0,1,0,1],[1,1,0,0],[1,0,1,1],[0,0,1,1],[0,1,1,0],[1,1,1,0],[1,1,0,0],[1,0,1,0],[0,0,0,1],[0,1,0,1],[1,1,0,0],[1,0,1,1],[0,1,1,1],[1,1,0,0],[1,1,1,0],[1,0,0,0],[0,0,1,1],[0,0,1,1]],
        [[0,1,0,1],[1,1,0,0],[1,0,1,0],[0,0,0,1],[0,0,1,1],[0,1,1,0],[1,0,0,0],[0,1,0,1],[1,1,0,0],[1,1,0,0],[1,0,1,0],[0,0,1,0],[0,1,0,1],[1,0,1,0],[0,0,1,1],[0,1,0,1],[1,1,0,0],[1,1,0,0],[1,0,1,0],[0,0,1,1]],
        [[0,0,1,1],[0,1,0,0],[1,1,0,0],[1,0,1,1],[0,1,1,0],[1,1,0,0],[1,0,0,0],[0,0,1,1],[0,1,0,1],[1,1,0,0],[1,1,0,0],[1,0,0,1],[0,0,1,1],[0,1,0,1],[1,0,1,0],[0,1,1,1],[1,1,0,0],[1,1,0,0],[1,0,0,1],[0,0,1,1]],
        [[0,1,1,0],[1,1,0,1],[1,1,0,0],[1,1,1,0],[1,1,0,0],[1,1,0,1],[1,0,0,0],[0,1,1,1],[1,1,1,0],[1,1,0,0],[1,0,0,1],[0,1,1,0],[1,0,1,0],[0,1,1,0],[1,1,0,0],[1,0,1,0],[0,1,0,0],[1,0,0,1],[0,0,1,0],[0,0,1,1]],
        [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,0,0],[0,1,0,1],[1,1,1,0],[1,1,0,0],[1,0,1,0],[0,1,0,1],[1,0,0,1],[0,1,1,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,0,0,0],[0,1,0,1],[1,1,1,0],[1,1,0,0],[1,0,1,1]],
        [[0,0,1,1],[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,1,0,0],[1,0,0,0],[0,0,1,1],[0,1,1,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,0,1,0],[0,1,0,1],[1,0,0,0],[0,0,1,1]],
        [[0,0,1,1],[0,1,1,0],[1,1,0,0],[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,1,0,0],[1,0,1,0],[0,1,0,1],[1,1,0,1],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,1],[1,1,0,0],[1,1,0,0],[1,0,1,0],[0,1,0,0],[1,0,1,0]],
        [[0,1,1,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,0,1,0],[0,1,0,0],[1,1,1,0],[1,1,0,0],[1,1,0,0],[1,0,1,0],[0,1,1,0],[1,1,0,0],[1,1,0,0],[1,0,0,0],[0,1,1,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[0,0,0,0]]
        ]

        function updateEspaceJeu() { //arrête le jeu si le prince arrive sur la porte, sinon réactualise l'espace et la position des objets
        if (prince.x==porte.x && prince.y==porte.y) {
                espaceJeu.stop("succes"); //jeu gagné
            }
			
            else {
                espaceJeu.clear();
				//on remet le mur et la porte au même endroit
                murs.update();
                porte.update();
				//si le joueur donne une commande et s'il n'y a pas de mur dans la direction donnée (coordonnées), on modifie la position du prince
                if ((espaceJeu.key && espaceJeu.key == 37) && coordonnees[prince.y/22-1][prince.x/22-1][0] == 1) {prince.x += -22;} //gauche
                if ((espaceJeu.key && espaceJeu.key == 39) && coordonnees[prince.y/22-1][prince.x/22-1][1] == 1) {prince.x += 22; } //droite
                if ((espaceJeu.key && espaceJeu.key == 38) && coordonnees[prince.y/22-1][prince.x/22-1][2] == 1) {prince.y += -22; } //haut
                if ((espaceJeu.key && espaceJeu.key == 40) && coordonnees[prince.y/22-1][prince.x/22-1][3] == 1) {prince.y += 22; } //bas
                prince.update();
            }
            
			//on réduit le temps de 150 ms à chaque actualisation car les actualisations se font toutes les 150ms
            temps -= 150;
            if (temps <= 0) {
                espaceJeu.stop("echec"); //jeu perdu si le temps est écoulé
                document.getElementById("horloge").innerHTML = "Perdu";
            } else {
                minutes = Math.floor(temps/60000); //on divise le temps en ms par 60000 pour trouver les minutes
                secondes = Math.floor((temps % 60000) / 1000); //on cherche alors le reste et le convertit en secondes
                document.getElementById("horloge").innerHTML = minutes + ":" + secondes; //on affiche le temps
            }
        }

    }

    //Fonction qui sort du labyrinthe si l'utilisateur est vainqueur.
    function SuccesLabyrinthe(idLabyrinthe) {
        
        document.getElementById("horloge").style.display = "none";

        var c = document.getElementsByTagName("canvas");
        document.getElementById("main").removeChild(c[0]);

		//en dépendant de l'emplacement dans l'histoire du labyrinthe, le joueur est envoyé au bon prochain état
        if (idLabyrinthe == "1") {
            EnvoieChoix('C4O1');
            EnvoieChoix('Fin1');
            ModifieEtat('15', 'B');
        } else if (idLabyrinthe == "2") {
            EnvoieChoix('C5O1');
            ModifieEtat('17', 'E');
        } else {
            EnvoieChoix('C8O1');
            ModifieEtat('26', 'E');
        }
        
    }

    //Fonction qui sort du labyrinthe s'il est perdant.
    function EchecLabyrinthe(idLabyrinthe) {
        
        document.getElementById("horloge").style.display = "none";

        var c = document.getElementsByTagName("canvas");
        document.getElementById("main").removeChild(c[0]);

		//en dépendant de l'emplacement dans l'histoire du labyrinthe, le joueur est envoyé au bon prochain état
        if (idLabyrinthe == "1") {
            EnvoieChoix('C4O2');
            ModifieEtat('16', 'D');
        } else if (idLabyrinthe == "2") {
            EnvoieChoix('C5O2');
            EnvoieChoix('Fin2');
            ModifieEtat('18', '9');
        } else {
            ModifieEtat('35', 'L');
            EnvoieChoix('C8O2')
        }
        
    }

</script>

</body>

</html>