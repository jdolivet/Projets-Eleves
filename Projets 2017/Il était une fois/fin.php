<?php 

    session_start();
    include 'head-header-menu.php';

    $csv = array_map("str_getcsv", file("comptes.csv"));
            $idCompte = 0; //on cherche à quelle ligne sont les données correspondant au pseudoyme
            foreach ($csv as $ligne) {
                if ($ligne[0] == $_SESSION["pseudo"]){
                    $idFin = $csv[$idCompte][6]; //On trouve la fin obtenue par le joueur.
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
        <div id = "texteAffiche">
            <h2 style = "font-family: 'Astloch', cursive; font-size: 400%; margin: 40px auto 20px auto;">Fin</h2>
            <br><p>Bravo, vous avez fini le jeu !</p><br>
            <p class = "fin" id = "Fin1">Vos choix vous on rapproché des versions des frères Grimm et de Disney du conte de la Belle au bois dormant. Vous pouvez retrouver la bande d'annonce de l'animation de Walt Disney sur <a href="https://www.youtube.com/watch?v=gV-8k4b2eTY" target="_blank">ce lien</a> et la version intégrale du conte de Jacob et Wilhelm Grimm <a href="http://onl.inrp.fr/ONL/travauxthematiques/livresdejeunesse/ouvrages/ouvrages_proposes/grand-sommeil/belle-bois-dormant-grim/final_document_view" target="_blank">ici</a>.</p>
            <p class = "fin" id = "Fin2">Malheuresement, vous n'avez pas réussi à sauver la Belle au bois dormant, mais n'abandonnez pas, vous pouvez encore tenter d'autres choix !</p>
            <p class = "fin" id = "Fin3">Vos choix vous on rapproché de la version de Giambattista Basile, auteur italien du XVIème siècle, de la Belle au bois dormant. Nous vous invitons à découvrir la version intégrale du conte à <a href="http://touslescontes.com/biblio/conte.php?iDconte=595" target="_blank">cette adresse</a>.</p>
            <p class = "fin" id = "Fin4">Vos choix vous on rapproché de la version de Giambattista Basile, auteur italien du XVIème siècle, de la Belle au bois dormant. Nous vous invitons à découvrir la version intégrale du conte à <a href="http://touslescontes.com/biblio/conte.php?iDconte=595" target="_blank">cette adresse</a>. Malheuresement, vous n'avez pas réussi à sauver la Belle au bois dormant, mais n'abandonnez pas, vous pouvez encore revenir sur vos choix !</p>
            <p class = "fin" id = "Fin5">Vos choix vous on rapproché de la version de Charles Perrault de la Belle au bois dormant. Nous vous invitons à découvrir la version intégrale du conte à <a href="http://onl.inrp.fr/ONL/travauxthematiques/livresdejeunesse/ouvrages/ouvrages_proposes/john-chatterton/belle-bois-dormant-perrault" target="_blank">cette adresse</a>.</p>
            <p class = "fin" id = "Fin6">Vos choix vous on rapproché de la version de Charles Perrault de la Belle au bois dormant. Nous vous invitons à découvrir la version intégrale du conte à <a href="http://onl.inrp.fr/ONL/travauxthematiques/livresdejeunesse/ouvrages/ouvrages_proposes/john-chatterton/belle-bois-dormant-perrault" target="_blank">cette adresse</a>.</p>
            <p class = "fin" id = "Fin7">Vos choix vous on rapproché de la version de Charles Perrault de la Belle au bois dormant. Nous vous invitons à découvrir la version intégrale du conte à <a href="http://onl.inrp.fr/ONL/travauxthematiques/livresdejeunesse/ouvrages/ouvrages_proposes/john-chatterton/belle-bois-dormant-perrault" target="_blank">cette adresse</a>. Malheuresement, vous n'avez pas réussi à sauver la Belle au bois dormant, mais n'abandonnez pas, vous pouvez encore revenir sur vos choix !</p>
            <br><p>Maintenant que vous avez terminé le jeu, deux nouvelles rubriques sont disponibles dans le menu. Dans "Vos Choix", vous pourrez découvrir le pourcentage de joueurs ayant fait les mêmes choix que vous. Cette rubrique vous permettra également de revenir sur vos pas pour explorer les autres versions du conte. Dans la "Galerie d'image", vous pourrez en savoir plus sur nos illustrations.</p>
        </div>
    </div>

<script>
    document.getElementById("texteAffiche").style.display = "block";
    document.getElementById("<?php echo $idFin; ?>").style.display = "block";
</script>

</body>

</html>

