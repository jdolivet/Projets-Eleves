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

	<h2 style="margin: 60px auto">Galerie d'images</h2>

    <div id = "texteAffiche" style = "display: block;">
        <p>Toutes nos images sont sous license <i>Creative Commons - Attribution - Pas d’Utilisation Commerciale 4.0 International</i>. Vous pouvez donc les partager, adapter, remixer, en faire tout ce que vous voulez tant que vous ne les vendez pas !</p>
        <br>
    </div>
	
    <div class="galerie">
	
	    <div class="dessin">
            <a class="Image" target="_blank" href="images/image0.jpg">
                <img src="images/image0.jpg" alt="image 0">
            </a>
            <div class="descr">Château pendant le printemps</div>
        </div>
		
		<div class="dessin">
            <a class="Image" target="_blank" href="images/image5.jpg">
                <img src="images/image5.jpg" alt="image 5">
            </a>
            <div class="descr">Château pendant l'hiver</div>
        </div>
		
		<div class="dessin">
            <a class="Image" target="_blank" href="images/imageA.jpg">
                <img src="images/imageA.jpg" alt="image A">
            </a>
            <div class="descr">Château avec les ronces</div>
        </div>
		
        <div class="dessin">
            <a class="Image" target="_blank" href="images/image2.jpg">
                <img src="images/image2.jpg" alt="image 2">
            </a>
            <div class="descr">Préparation du baptême </div>
        </div>

        <div class="dessin">
            <a class="Image" target="_blank" href="images/image3.jpg">
                <img src="images/image3.jpg" alt="image 3">
            </a>
            <div class="descr">Malédiction pendant le baptême</div>
        </div>

        <div class="dessin">
            <a class="Image" target="_blank" href="images/image4.jpg">
                <img src="images/image4.jpg" alt="image 4">
            </a>
            <div class="descr">Voeu de la Fée des Lilas</div>
        </div>

        <div class="dessin">
            <a class="Image" target="_blank" href="images/image1.jpg">
                <img src="images/image1.jpg" alt="image 1">
            </a>
            <div class="descr">Rencontre avec la Grenouille</div>
        </div>
		
        <div class="dessin">
            <a class="Image" target="_blank" href="images/image6.jpg">
                <img src="images/image6.jpg" alt="image 6">
            </a>
            <div class="descr">Bûcher des fuseaux</div>
        </div>

        <div class="dessin">
            <a class="Image" target="_blank" href="images/image7.jpg">
                <img src="images/image7.jpg" alt="image 7">
            </a>
            <div class="descr">Cabane dans la forêt</div>
        </div>

        <div class="dessin">
            <a class="Image" target="_blank" href="images/image8.jpg">
                <img src="images/image8.jpg" alt="image 8">
            </a>
            <div class="descr">Escaliers du château</div>
        </div>
		
        <div class="dessin">
            <a class="Image" target="_blank" href="images/imageC.jpg">
                <img src="images/imageC.jpg" alt="image C">
            </a>
            <div class="descr">Le château s'endort</div>
        </div>

        <div class="dessin">
            <a class="Image" target="_blank" href="images/image9.jpg">
                <img src="images/image9.jpg" alt="image 9">
            </a>
            <div class="descr">Sommeil de la princesse</div>
        </div>
	
        <div class="dessin">
            <a class="Image" target="_blank" href="images/imageE.jpg">
                <img src="images/imageE.jpg" alt="image E">
            </a>
            <div class="descr">Rencontre avec le Roi Fortuné</div>
        </div>
		
        <div class="dessin">
            <a class="Image" target="_blank" href="images/imageF.jpg">
                <img src="images/imageF.jpg" alt="image F">
            </a>
            <div class="descr">Fée des Lilas avec les enfants</div>
        </div>
		
        <div class="dessin">
            <a class="Image" target="_blank" href="images/imageG.jpg">
                <img src="images/imageG.jpg" alt="image G">
            </a>
            <div class="descr">Famille avec le Roi Fortuné</div>
        </div>
		
		<div class="dessin">
            <a class="Image" target="_blank" href="images/imageN.jpg">
                <img src="images/imageN.jpg" alt="image N">
            </a>
            <div class="descr">Sacre dans le royaume de la princesse</div>
        </div>		
		
        <div class="dessin">
            <a class="Image" target="_blank" href="images/imageO.jpg">
                <img src="images/imageO.jpg" alt="image O">
            </a>
            <div class="descr">Sacre dans le royaume du Prince Chéri</div>
        </div>
	
        <div class="dessin">
            <a class="Image" target="_blank" href="images/imageH.jpg">
                <img src="images/imageH.jpg" alt="image H">
            </a>
            <div class="descr">Reine dans salon du Roi Fortuné</div>
        </div>
		
        <div class="dessin">
            <a class="Image" target="_blank" href="images/imageI.jpg">
                <img src="images/imageI.jpg" alt="image I">
            </a>
            <div class="descr">Repas dans salon du Roi Fortuné</div>
        </div>		
		
        <div class="dessin">
            <a class="Image" target="_blank" href="images/imageP.jpg">
                <img src="images/imageP.jpg" alt="image P">
            </a>
            <div class="descr">Ogresse dans salon du Prince Chéri</div>
        </div>
		
        <div class="dessin">
            <a class="Image" target="_blank" href="images/imageQ.jpg">
                <img src="images/imageQ.jpg" alt="image Q">
            </a>
            <div class="descr">Repas dans salon du Prince Chéri</div>
        </div>		
		
        <div class="dessin">
            <a class="Image" target="_blank" href="images/imageB.jpg">
                <img src="images/imageB.jpg" alt="image B">
            </a>
            <div class="descr">Mariage avec le Prince Charmant</div>
        </div>
		
        <div class="dessin">
            <a class="Image" target="_blank" href="images/imageK.jpg">
                <img src="images/imageK.jpg" alt="image K">
            </a>
            <div class="descr">Mariage avec le Roi Fortuné</div>
        </div>

        <div class="dessin">
            <a class="Image" target="_blank" href="images/imageM.jpg">
                <img src="images/imageM.jpg" alt="image M">
            </a>
            <div class="descr">Mariage avec le Prince Chéri</div>
        </div>
		
	    <div class="dessin">
            <a class="Image" target="_blank" href="images/imageJ.jpg">
                <img src="images/imageJ.jpg" alt="image J">
            </a>
            <div class="descr">Bûcher</div>
        </div>
		
		<div class="dessin">
            <a class="Image" target="_blank" href="images/imageR.jpg">
                <img src="images/imageR.jpg" alt="image R">
            </a>
            <div class="descr">Chaudron avec serpents</div>
        </div>
		
    </div>

</div>

<a rel="license" id="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Licença Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a>

</body>