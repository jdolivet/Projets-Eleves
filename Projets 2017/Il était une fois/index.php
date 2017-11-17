<?php include 'head-header-menu.php';?>

    <div id = "main" onclick = "FermeMenu()">

        <div id = "loader"></div>
        <img id = "imagefleurs" onload="LoadOK()" src = "">
        <div class = "index" id = "titreindex">La Belle<br>au bois dormant</div>
        <a href = "jeu.php" class = "bouton index" id = "jouerindex"> Jouer </a>
        <a href = "presentation.php" class = "bouton index" id = "presentationindex">Présentation</a>

    </div>

<script>

    function LoadOK() {
        document.getElementById('loader').style.display = 'none';
        document.getElementById('imagefleurs').style.display = 'block';
        document.getElementById('titreindex').style.display = 'table';
        document.getElementById('presentationindex').style.display = 'table';
        document.getElementById('jouerindex').style.display = 'table';
    }

    nbAleatoire = Math.random();

    if (nbAleatoire <= 0.33) {
        document.getElementById("imagefleurs").src = "images/fleurs1.jpg";
    } else if (nbAleatoire >= 0.66) {
        document.getElementById("imagefleurs").src = "images/fleurs2.jpg";
    } else {
        document.getElementById("imagefleurs").src = "images/fleurs3.jpg";
    }

</script>

</body>

</html>
