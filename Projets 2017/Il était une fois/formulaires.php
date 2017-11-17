<?php 
		
		session_start();
		//S'il y a une session ouverte, on la ferme.
		if (isset($_SESSION)) {
			$_SESSION['statutlogin'] = "NON";
		}

		include 'head-header-menu.php';

		//On transforme le csv des comptes en array d'arrays pour le lire plus tard
		$csv = array_map("str_getcsv", file("comptes.csv"));
	?>
	<script>
	
		//on ajoute une méthode pour vérifier si le pseudonyme est déjà utilisé pour l'inscription
		//on utilise la fonction du jQuery validation plugin addMethod(nom de la méthode, fonction, message à afficher)
		jQuery.validator.addMethod(
			"pseudoExistant", //nom de la méthode
			function(pseu) { //vérifie si le pseudonyme est déjà existant dans le csv des comptes
				//on transmet la variable de PHP à JS
				//la fonction json_encode permet de trasformer l'array en langage php en un array en json
				var JScsv = <?php echo json_encode($csv) ?>;
				// on parcourt le csv en cherchant un pseudonyme identique
				var n = 0;
				for (var i = 1; i < JScsv.length; i++) {
					if (JScsv[i][0]  == pseu) {
						n += 1;
					}
				}
				if (n==0) {
					return true;
				}
				else {return false;}
			},
			"Ce pseudonyme existe déjà"//message à afficher en cas d'erreur
		),
		
		//on utilise la même fonction en inversant true et false (le pseudo doit être existant pour la connection)
		jQuery.validator.addMethod(
			"pseudoNonExistant",
			function(pseu) {
				var JScsv = <?php echo json_encode($csv) ?>;
				var n = 0;
				for (var i = 1; i < JScsv.length; i++) {
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
			"Ce pseudonyme n'existe pas"
		),
		
		//on ajoute alors une méthode pour vérifier si le mot de passe correspond à celui du compte pour la connection
		jQuery.validator.addMethod(
			"mdpInc",
			function(mdp) {
				var JScsv = <?php echo json_encode($csv) ?>;
				var idCompte = 1;
				while ((JScsv[idCompte][0] != pseudonyme)&&(idCompte<JScsv.length)) {
					idCompte += 1;
				}
				if (JScsv[idCompte][1] == mdp) {
					return true;
				} else { 
					return false;
				}
			},
			"Mot de passe incorrect"
		),
		
		//on utilise le jquery validation plugin pour vérifier les conditions de l'inscription côté client	
		$().ready(function() {
			$("#pageInscr").validate({ //vérifie les conditions pour l'inscription
				rules: { //on énonce les conditions
					pseudo: {
						required: true,
						pseudoExistant : true, //on utilise la méthode créée
						minlength: 5,
					},
					mdp: {
						required: true,
						minlength: 5,
					},
					mdp_conf: {
						required: true,
						equalTo: "#mdp",
					},
					reponse: "required",
				},
				messages: { //on définit les messages à afficher pour chaque erreur
					pseudo: {
						required: "Veuillez entrer votre pseudonyme",
						minlength: "Le pseudonyme doit avoir au moins 5 charactères",
					},
					mdp: {
						required: "Veuillez entrer votre mot de passe",
						minlength: "Le mot de passe doit avoir au moins 5 charactères",
					},
					mdp_conf: {
						required: "Veuillez confirmer votre mot de passe",
						equalTo: "Les mots de passe doivent être identiques",
					},
					reponse: "Veuillez entrer une réponse",
				}
			});
		
			$("#pageConn").validate({ //vérifie les conditions pour la connection
				rules: {
					pseudo: {
						required: true,
						pseudoNonExistant: true, //on utilise la méthode créée
					},
					mdp: {
						required: true,
						mdpInc: true, //on utilise la méthode créée
					},
				},
				messages: {
					pseudo: {
						required: "Veuillez entrer votre pseudonyme",
					},
					mdp: {
						required: "Veuillez entrer votre mot de passe",
					},
				}
			});
		});

	</script>
	


<div id="main" onclick = "FermeMenu()">

	<h2 style="margin-top:10px ; margin-bottom:10px">S'inscrire</h2>
	<!-- après vérification, les données vont être envoyées à jeu.php grâce à la méthode post-->
	<form accept-charset="UTF-8" class="cmxform" id="pageInscr" method="post" action="jeu.php">
		<div class="container">
			<p style = "text-indent: 10px; text-align: left;">
				<label for="pseudo"><b>Pseudonyme</b></label>
				<input name="pseudo" type="text" placeholder="Entrez votre pseudonyme">
			</p>
			<p style = "text-indent: 10px; text-align: left;">
				<label for="mdp"><b>Mot de passe</b></label>
				<input id="mdp" name="mdp" type="password" placeholder="Créez un mot de passe">
				<label for="mdp_conf"></label>
				<input name="mdp_conf" type="password" placeholder="Confirmez votre mot de passe">
			</p>
			<p style = "text-indent: 10px; text-align: left;">
				<label for="qSecurite"><b>Question de sécurité : </b></label>
				<select name="question" required> <!-- permet de choisir sa question de securite -->
					<!-- la première option a une valeur vide donc l'attribut required de la question va obliger à choisir une autre option -->
					<option value="">Choisissez votre question</option>
					<option value="0">Comment s'appelait votre premier animal de compagnie?</option>
					<option value="1">Quel était votre surnom quand vous étiez petit?</option>
					<option value="2">Quelle est votre équipe de sport préférée?</option>
					<option value="3">Quelle est votre couleur préférée?</option>
					<option value="4">Quel est votre animal préféré?</option>
					<option value="5">Quel est votre plat préféré?</option>
				</select>
				<input name="reponse" type="text" placeholder="Réponse">
			</p>
			<p style = "text-indent: 10px; text-align: left;">
				<input class="boutoninscr" id="boutoninscr" type="submit" value="Confirmer">
			</p>
		</div>
	</form>

	<br>
	<br>

	<h2 style="margin:10px 50px;">Se connecter</h2>
	<!-- après vérification, les données vont être envoyées à jeu.php grâce à la méthode post-->
	<form accept-charset="UTF-8" class="cmxform" id="pageConn" method="post" action="jeu.php">
		<div class="container">
			<p style = "text-indent: 10px; text-align: left;">
				<label for="pseudo"><b>Pseudonyme</b></label>
				<input name="pseudo" type="text" placeholder="Entrez votre pseudonyme">
			</p>
			<p style = "text-indent: 10px; text-align: left;">
				<label><b>Mot de passe</b></label>
				<input name="mdp" type="password" placeholder="Entrez votre mot de passe">
			</p>
			<p style = "text-indent: 10px; text-align: left;">
				<input type ="button" class="bouton_oubli" value="Mot de passe oublié?" onClick="window.location.href = 'oubli-mdp.php'">
			</p>
			<p style = "text-indent: 10px; text-align: left;">
				<input class="boutonlogin" id="boutonlogin" type="submit" value="Confirmer">
			</p>
				
			
		</div>
	</form>
	
</div>

</body>

</html>
