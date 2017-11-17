<?php 

    session_start();
    include 'head-header-menu.php';

    //A partir du pseudonyme, on trouve les choix faits par le joueur et la fin qu'il a obtenu.

    $csv = array_map("str_getcsv", file("comptes.csv"));
    $idCompte = 0; //on cherche à quelle ligne sont les données correspondant au pseudoyme
    foreach ($csv as $ligne) {
        if ($ligne[0] == $_SESSION["pseudo"]){
            $choixjoueur = $csv[$idCompte][5]; //On trouve les choix du joueur.
            $idFin = $csv[$idCompte][6]; //On trouve la fin qu'il a obtenu.
            break;
        }
        ++$idCompte;
    }


    if ($_SESSION['statutlogin'] != "OK" or !isset($_SESSION) or $idFin == "") {
?>

        <script>
            window.location.assign("formulaires.php")
        </script>

<?php
    }
?>

    <div id = "main" onclick = "FermeMenu()">
        
        <h2>Vos Choix</h2>

        <div class = 'conteneur' id = "C1">
            <h3>Qu'avez-vous proposé à la Reine pour l'aider à avoir des enfants ?</h3>        
              <div class = 'contenu premiereOption' id = 'C1O1'></div>
              <div class = 'contenu' id = 'C1O2'></div>
              <div class = 'contenu derniereOption' id = 'C1O3'></div>
            <p class = "stat" id = 'tC1O1'>Vous et <i id = 'nbC1O1'></i> des joueurs avez conseillé à la Reine d'aller prendre les eaux à l'étranger.</p>
            <p class = "stat" id = 'tC1O2'>Vous et <i id = 'nbC1O2'></i> des joueurs avez conseillé à la Reine un pélerinage.</p>
            <p class = "stat" id = 'tC1O3'>Vous et <i id = 'nbC1O3'></i> des joueurs avez recommandé la prière à la Reine.</p>
            <button class = "bouton" id = "000" onclick = "ChangeEtat('000');"> Revenir sur ce choix ? </button>
        </div>

        <div class = 'conteneur' id = "C2">
            <h3>Avez-vous invité la Fée Carabosse au festin ?</h3>
              <div class = 'contenu premiereOption' id = 'C2O1'></div>
              <div class = 'contenu derniereOption' id = 'C2O2'></div>
            <p class = "stat" id = 'tC2O1'>Vous et <i id = 'nbC2O1'></i> des joueurs n'avez pas invité la Fée Carabosse au baptême de la Princesse.</p>
            <p class = "stat" id = 'tC2O2'>Vous et <i id = 'nbC2O2'></i> des joueurs avez invité toutes les Fées malgré le manque de couverts.</p>
            <button class = "bouton" id = "062" onclick = "ChangeEtat('062');"> Revenir sur ce choix ? </button>
        </div>

        <div class = 'conteneur' id = "C3">
            <h3>Comment avez-vous tenté de contrer la malédiction ?</h3>
              <div class = 'contenu premiereOption' id = 'C3O1'></div>
              <div class = 'contenu' id = 'C3O2'></div>
              <div class = 'contenu derniereOption' id = 'C3O3'></div>
            <p class = "stat" id = 'tC3O1'>Vous et <i id = 'nbC3O1'></i> des joueurs avez ordonné de brûler tous les fuseaux du royaume.</p>
            <p class = "stat" id = 'tC3O2'>Vous et <i id = 'nbC3O2'></i> des joueurs avez caché la Pricesse dans la forêt.</p>
            <p class = "stat" id = 'tC3O3'>Vous et <i id = 'nbC3O3'></i> des joueurs avez décidé de surveiller la Princesse le jour de ses seize ans.</p>
            <button class = "bouton" id = "095" onclick = "ChangeEtat('095');"> Revenir sur ce choix ? </button>
        </div>

        <div class = 'conteneur' id = "C4">
            <h3>Le Prince Charmant a-t-il traversé la forêt de ronces ?</h3>
              <div class = 'contenu premiereOption' id = 'C4O1'></div>
              <div class = 'contenu derniereOption' id = 'C4O2'></div>
            <p class = "stat" id = 'tC4O1'>Vous et <i id = 'nbC4O1'></i> des joueurs avez mené le Prince Charmant à travers la forêt avec succès.</p>
            <p class = "stat" id = 'tC4O2'>Vous et <i id = 'nbC4O2'></i> des joueurs n'avez pas réussi à mener le Prince Charmant à travers la forêt.</p>
            <button class = "bouton" id = "14A" onclick = "ChangeEtat('14A');"> Revenir sur ce choix ? </button>
        </div>

        <div class = 'conteneur' id = "C5">
            <h3>Le Roi Fortuné est-il parvenu à traverser le labyrinthe d'épines ?</h3>
              <div class = 'contenu premiereOption' id = 'C5O1'></div>
              <div class = 'contenu derniereOption' id = 'C5O2'></div>
            <p class = "stat" id = 'tC5O1'>Vous et <i id = 'nbC5O1'></i> des joueurs êtes parvenus à guider le Roi Fortuné jusqu'au Château.</p>
            <p class = "stat" id = 'tC5O2'>Vous et <i id = 'nbC5O2'></i> des joueurs n'êtes pas parvenus à guider le Roi Fortuné jusqu'au Château.</p>
            <button class = "bouton" id = "16D" onclick = "ChangeEtat('16D');"> Revenir sur ce choix ? </button>
        </div>

        <div class = 'conteneur' id = "C6">
            <h3>Le Roi Fortuné a-t-il violé la Princesse pendant son sommeil ?</h3>
              <div class = 'contenu premiereOption' id = 'C6O1'></div>
              <div class = 'contenu derniereOption' id = 'C6O2'></div>
            <p class = "stat" id = 'tC6O1'>Vous et <i id = 'nbC6O1'></i> des joueurs avez choisi que le Roi "cueille d'elle les fruits de l'amour".</p>
            <p class = "stat" id = 'tC6O2'>Vous et <i id = 'nbC6O2'></i> des joueurs avez décidé que le Roi devait laisser la Princesse endormie.</p>
            <button class = "bouton" id = "17E" onclick = "ChangeEtat('17E');"> Revenir sur ce choix ? </button>
        </div>

        <div class = 'conteneur' id = "C7">
            <h3>Qu'avez-vous fait pour que la Princesse ait un sommeil tranquille ?</h3>
              <div class = 'contenu premiereOption' id = 'C7O1'></div>
              <div class = 'contenu derniereOption' id = 'C7O2'></div>
            <p class = "stat" id = 'tC7O1'>Vous et <i id = 'nbC7O1'></i> des joueurs avez endormi tout le Château pour que la Princesse ne se réveille pas seule.</p>
            <p class = "stat" id = 'tC7O2'>Vous et <i id = 'nbC7O2'></i> des joueurs avez fait pousser une forêt de ronces pour la protéger.</p>
            <button class = "bouton" id = "229" onclick = "ChangeEtat('229');"> Revenir sur ce choix ? </button>
        </div>

        <div class = 'conteneur' id = "C8">
            <h3>Le Roi Fortuné est-il parvenu à traverser le labyrinthe d'épines ?</h3>
              <div class = 'contenu premiereOption' id = 'C8O1'></div>
              <div class = 'contenu derniereOption' id = 'C8O2'></div>
            <p class = "stat" id = 'tC8O1'>Vous et <i id = 'nbC8O1'></i> des joueurs êtes parvenus à guider le Roi Fortuné jusqu'au Château.</p>
            <p class = "stat" id = 'tC8O2'>Vous et <i id = 'nbC8O2'></i> des joueurs n'êtes pas parvenus à guider le Roi Fortuné jusqu'au Château.</p>
            <button class = "bouton" id = "25A" onclick = "ChangeEtat('25A');"> Revenir sur ce choix ? </button>
        </div>

        <div class = 'conteneur' id = "C9">
            <h3>Le Roi Fortuné a-t-il violé la Princesse pendant son sommeil ?</h3>
              <div class = 'contenu premiereOption' id = 'C9O1'></div>
              <div class = 'contenu derniereOption' id = 'C9O2'></div>
            <p class = "stat" id = 'tC9O1'>Vous et <i id = 'nbC9O1'></i> des joueurs avez choisi que le Roi "cueille d'elle les fruits de l'amour".</p>
            <p class = "stat" id = 'tC9O2'>Vous et <i id = 'nbC9O2'></i> des joueurs avez décidé que le Roi devait laisser la Princesse endormie.</p>
            <button class = "bouton" id = "26E" onclick = "ChangeEtat('26E');"> Revenir sur ce choix ? </button>
        </div>

        <div class = 'conteneur' id = "CA">
            <h3>Le Cuisinier a-t-il tué les enfants ?</h3>
              <div class = 'contenu premiereOption' id = 'CAO1'></div>
              <div class = 'contenu derniereOption' id = 'CAO2'></div>
            <p class = "stat" id = 'tCAO1'>Vous et <i id = 'nbCAO1'></i> des joueurs avez eut pitié des enfants.</p>
            <p class = "stat" id = 'tCAO2'>Vous et <i id = 'nbCAO2'></i> des joueurs avez obéi à la Reine.</p>
            <button class = "bouton" id = "29H" onclick = "ChangeEtat('29H');"> Revenir sur ce choix ? </button>
        </div>        

        <div class = 'conteneur' id = "CB">
            <h3>Après leur mariage, où sont allé vivre le Prince Chéri et la Princesse ?</h3>
              <div class = 'contenu premiereOption' id = 'CBO1'></div>
              <div class = 'contenu derniereOption' id = 'CBO2'></div>
            <p class = "stat" id = 'tCBO1'>Vous et <i id = 'nbCBO1'></i> des joueurs avez décidé qu'ils vivraient dans le Château de la Princesse.</p>
            <p class = "stat" id = 'tCBO2'>Vous et <i id = 'nbCBO2'></i> des joueurs avez décidé qu'ils vivraient dans le Royaume du Prince.</p>
            <button class = "bouton" id = "36M" onclick = "ChangeEtat('36M');"> Revenir sur ce choix ? </button>
        </div>

        <div class = 'conteneur' id = "CC">
            <h3>L'Ogresse a-t-elle mangé les enfants ?</h3>
              <div class = 'contenu premiereOption' id = 'CCO1'></div>
              <div class = 'contenu derniereOption' id = 'CCO2'></div>
            <p class = "stat" id = 'tCCO1'>Vous et <i id = 'nbCCO1'></i> des joueurs avez eut pitié des enfants.</p>
            <p class = "stat" id = 'tCCO2'>Vous et <i id = 'nbCCO2'></i> des joueurs avez obéi à la Reine.</p>
            <button class = "bouton" id = "39P" onclick = "ChangeEtat('39P');"> Revenir sur ce choix ? </button>
        </div>

    </div>

    <?php

    //Cette partie du code définit la taille des div en fonction des infos de statistiques.csv

        // La fonction file transforme chaque ligne d'un fichier en élément d'un array.
        // La fonction array_map exécute la fonction str_csv sur chacun des élément de l'array créé grâce à file.
        // La fonction str_getcsv sépare les éléments de chaque ligne en éléments d'un array.
        $csv = array_map("str_getcsv", file("statistiques.csv"));


        $n = 0;
        //On augmente $n pour avancer dans le tableau tant que $n ne désigne pas une case vide.
        while ($csv[0][$n] != null) {
            //Cette condition sert à vérifier si le choix traité comporte 2 ou 3 options.
            //La fonction substr() retourne ici la partie de la chaîne de caractères comprise entre les indices 0 et 2, pour "C1O1" elle retourne "C1", par exemple.
            if (substr($csv[0][$n], 0, 2) == substr($csv[0][$n + 2], 0, 2)) {
                //On transforme les cases de la première ligne du tableau en chaînes de caractères correspondant aux identifiants des options de ce choix.
                $idO1 = $csv[0][$n];
                $idO2 = $csv[0][$n + 1]; 
                $idO3 = $csv[0][$n + 2];
                //On calcule les pourcentages. La fonction intval() transforme une chaîne de caractères en nombre entier.
                $O1 =  round(intval($csv[1][$n]) * 100 / (intval($csv[1][$n]) + intval($csv[1][$n + 1]) + intval($csv[1][$n + 2])));
                $O2 =  round(intval($csv[1][$n + 1]) * 100 / (intval($csv[1][$n]) + intval($csv[1][$n + 1]) + intval($csv[1][$n + 2])));
                $O3 =  100 - $O1 - $O2;
                $n += 3;
            } else {
                $idO1 = $csv[0][$n];
                $idO2 = $csv[0][$n + 1]; 
                $O1 =  round(intval($csv[1][$n]) * 100 / (intval($csv[1][$n]) + intval($csv[1][$n + 1])));
                $O2 =  100 - $O1;
                $n += 2;
            }
            //On insère des lignes de javascript qui modifient le texte et la taille des divs colorées pour les faire correspondre aux poucentages issus du csv.
            echo "<script>document.getElementById('$idO1').style.width = '$O1%';</script>";
            echo "<script>document.getElementById('$idO2').style.width = '$O2%';</script>";
            echo "<script>document.getElementById('$idO3').style.width = '$O3%';</script>";
            echo "<script>document.getElementById('$idO1').innerHTML = '$O1%';</script>";
            echo "<script>document.getElementById('$idO2').innerHTML = '$O2%';</script>";
            echo "<script>document.getElementById('$idO3').innerHTML = '$O3%';</script>";
            echo "<script>document.getElementById('nb$idO1').innerHTML = '$O1%';</script>";
            echo "<script>document.getElementById('nb$idO2').innerHTML = '$O2%';</script>";
            echo "<script>document.getElementById('nb$idO3').innerHTML = '$O3%';</script>";
        }

    //Cette partie du code parcourt la variable contenant les choix du joueurs pour afficher seulement les choix qu'il a fait.

        for($i = 0; $i <= strlen($choixjoueur) - 4; $i = $i + 4) {
            $idChoix = substr($choixjoueur, $i, 2);
            $idOption = substr($choixjoueur, $i, 4);
?>
            <script>
                document.getElementById("<?php echo $idChoix ?>").style.display = "block"; 
                document.getElementById("<?php echo "t" . $idOption ?>").style.display = "inline-block"; 
            </script>
<?php   }
        
?>

<script>
    function ChangeEtat(idEtat) {
        var requeteTraiteEtat = CreeRequete();
        requeteTraiteEtat.open("GET", "traiteetat.php?idEtat=" + idEtat + "&pseudo=<?php echo $_SESSION['pseudo'] ?>", true);
        requeteTraiteEtat.send();
        document.getElementById(idEtat).innerHTML = "Allons-y !";
        document.getElementById(idEtat).onclick = function() {location.href='jeu.php'} ;
    }
</script>


</body>
<html>
