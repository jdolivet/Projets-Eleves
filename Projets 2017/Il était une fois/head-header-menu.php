<!DOCTYPE HTML>

<html lang = 'fr'>

<head>

    <meta charset = "UTF-8">
    <meta name = "description" content  = "La Belle au bois dormant">
    <meta name = "keywords" content = "Belle au bois dormant, Contes de fées, versions, jeu, Grimm, Perrault">
    <meta name = "auteur" content = "Coraline et Lina">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">


    <title>Le Bois dormant</title>
    <link rel = "stylesheet" type = "text/css" href = "stylejeu.css" media = "screen">
    <link href="https://fonts.googleapis.com/css?family=Astloch" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Vollkorn" rel="stylesheet"> 
    <link href="https://fonts.googleapis.com/css?family=Nunito+Sans:300,300i,400,600" rel="stylesheet">
    <link rel="icon" href="images/icon.png" type="image/png">

    <script src="./jquery/lib/jquery.js"></script>
	<script src="./jquery/dist/jquery.validate.js"></script>
	<script src="./jquery/dist/additional-methods.js"></script>


</head>



<body id = "body" onload = "TrouveEtat()">

    <header>   
        <button id = "hamburguer" onclick = "OuvreMenu()">&#9776;</button>

        <h1>Le Bois dormant</h1>

        <a id = "deconnexion" href = "formulaires.php">Déconnexion</a>
    </header>

    <div id = "menu">
        <a href = "jeu.php" id = "link">Jeu</a>
        <a href = "presentation.php">Présentation</a>
        <a href = "galerie.php" id = "lienGalerie">Galerie d'images</a>
        <a href = "statistiques.php" id = "lienStat">Vos Choix</a>
    </div>

<!--  -->

<?php

    //Les liens vers "Mes Choix" et "Galerie d'images" ne s'affichent que si le joueur a fini le jeu.

    $csv = array_map("str_getcsv", file("comptes.csv"));
    $idCompte = 0; //on cherche à quelle ligne sont les données correspondant au pseudoyme
    foreach ($csv as $ligne) {
        if ($ligne[0] == $_SESSION["pseudo"]){
            $idFin = $csv[$idCompte][6]; //On trouve la fin qu'il a obtenu.
            break;
        }
        ++$idCompte;
    }

    if ($_SESSION['statutlogin'] != "OK" or !isset($_SESSION)) {
?>

        <script>
            document.getElementById("deconnexion").innerHTML = "Connexion";
        </script>

<?php
    } 

    if ($_SESSION['statutlogin'] != "OK" or !isset($_SESSION) or $idFin == "") {
?>

        <script>
            document.getElementById("lienStat").style.display = "none";
            document.getElementById("lienGalerie").style.display = "none";
        </script>

<?php
    } else {
?>

        <script>
            document.getElementById("lienStat").style.display = "";
            document.getElementById("lienGalerie").style.display = "";
        </script>

<?php
    }
?>

<script>
        
    function OuvreMenu() {
        document.getElementById("menu").style.width = "250px";
        document.getElementById("hamburguer").onclick = Function("FermeMenu()");
        document.getElementById("hamburguer").innerHTML = "&#10005";
    }

    function FermeMenu() {
        document.getElementById("menu").style.width = "0";
        document.getElementById("hamburguer").onclick = Function("OuvreMenu()");
        document.getElementById("hamburguer").innerHTML = "&#9776;";
    }

    //Cette fonction crée un objet requête qui permet de dialoguer avec le serveur grâce à AJAX.
    //Elle sera utilisée plusieurs fois par la suite.
    function CreeRequete() {
        //On crée un objet XMLHttpRequest, qui sert à dialoguer avec le serveur.
        if (window.XMLHttpRequest) {
            //Code pour naviageturs modernes
            var requete = new XMLHttpRequest();
        } else {
            //Code pour anciennes versions d'IE
            var requete = new ActiveXObject("Microsoft.XMLHTTP");
        }
        return requete;
    }


</script>
