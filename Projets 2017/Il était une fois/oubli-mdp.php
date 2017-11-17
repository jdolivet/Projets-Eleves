<?php 
		
	//S'il y a une session ouverte, on la ferme.
	if (isset($_SESSION)) {
		session_unset(); 
		session_destroy(); 
	}
		
	include 'head-header-menu.php';

	//On transforme le csv des comptes en array d'arrays pour le lire plus tard
	$csv = array_map("str_getcsv", file("comptes.csv"));
	
?>
	
	<script>
		
		jQuery.validator.addMethod( //on ajoute une méthode pour vérifier le pseudonyme
			"pseudoNonExistant", //nom de la méthode
			function(pseu) { //fonction qui vérifie l'existance du pseudo
				//on transmet le array de arrays de PHP à JS
				//la fonction json_encode() permet de traduire le array de arrays en langage PHP à un langage JSon
				var JScsv = <?php echo json_encode($csv) ?>; 
				var n = 0;
				for (var i = 1; i < JScsv.length; i++) { //si n==0, alors le pseudo n'existe pas
					if (JScsv[i][0]  == pseu) {
						n += 1;
					}
				}
				pseudonyme = pseu;
				if (n==0) {
					return false;
				} else {
					return true;
				}
			},
			"Ce pseudonyme n'existe pas" //message à afficher en cas d'erreur
		),
		
		$().ready(function() {
    		$("#VerPseudo").validate({ //on vérifie les conditions pour envoyer le formulaire
				rules: {
					pseudo: {
							required: true, //la variable doit être remplie
							pseudoNonExistant: true, //me´thode créée pour vérifier l'existance du pseudo
						},
				},
				messages: {
					pseudo: {
						required: "Veuillez entrer votre pseudonyme",
					},
				}
			});
		});

	</script>

	<div id = "main" onclick = "FermeMenu()">

		<h2 style="margin-top:10px ; margin-bottom:10px">Réinitialisation du mot de passe</h2>
		<!-- après vérification, les données vont être envoyées à nouveau-mdp.php grâce à la méthode post-->
		<form accept-charset="UTF-8" class="cmxform" id="VerPseudo" method="post" action="nouveau-mdp.php">
			<div class="container">
				<p style = "text-indent: 10px; text-align: left;">
					<label for="pseudo"><b>Pseudonyme</b></label>
					<input id="pseudo" name="pseudo" type="text" placeholder="Entrez votre pseudonyme">
				</p>
				<p style = "text-indent: 10px; text-align: left;">
					<input class="boutoninscr" id="boutonConf1" type="submit" value="Confirmer">
				</p>
			</div>
		<form>

	</div>

</body>
</html>