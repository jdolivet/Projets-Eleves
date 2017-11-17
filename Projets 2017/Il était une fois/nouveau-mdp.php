<?php 
		
	//S'il y a une session ouverte, on la ferme.
	if (isset($_SESSION)) {
		session_unset(); 
		session_destroy(); 
	}
		
	include 'head-header-menu.php';

	//on reçoit la variable postée par la vérification du pseudonyme
	//la fonction htmlspecialchars() remplace les caractères spéciaux pour empêcher des utilisateurs d'insérer du code
	$pseudo = htmlspecialchars($_POST["pseudo"]); 

	//On transforme le csv des comptes en array d'arrays pour le lire plus tard
	$csv = array_map("str_getcsv", file("comptes.csv"));
	
?>

	<script>
	
		pseudonyme = "<?php echo $pseudo?>"; //on transmet la variable PHP à JS
		jQuery.validator.addMethod( //on ajoute alors une méthode pour vérifier la réponse
			"repInc", //nom de méthode
			function(rep) { //vérifie si la réponse correspond à celui du compte
				var JScsv = <?php echo json_encode($csv) ?>; //on traduit le array de arrays PHP à JSon
				//on cherche le idCompte: numéro de la ligne du compte dans le csv
				var idCompte = 1;
				while ((JScsv[idCompte][0] != pseudonyme)&&(idCompte<JScsv.length)) {
					idCompte += 1;
				}
				if (JScsv[idCompte][3] == rep) { //on vérifie alors la réponse
					return true;
				} else { 
					return false;
				}
			},
			"Réponse incorrecte" //message à afficher en cas d'erreur
		),
	
		
		$().ready(function() {
			$("#ReiniMdp").validate({ //on vérifie les conditions pour cahnger le mot de passe
				rules: {
					reponse: {
						required: true,
						repInc: true, //on utilise la méthode créée pour vérifier la réponse
					},
					nouv_mdp: {
						required: true,
						minlength: 5,
					},
					mdp_conf: {
						required: true,
						equalTo: "#nouv_mdp",
					},
				},
				messages: {
					reponse: {
						required: "Veuillez entrer une réponse",
					},
					nouv_mdp: {
						required: "Veuillez entrer votre mot de passe",
						minlength: "Le mot de passe doit avoir au moins 5 charactères",
					},
					mdp_conf: {
						required: "Veuillez confirmer votre mot de passe",
						equalTo: "Les mots de passe doivent être identiques",
					},
				}
			});
		});


	</script>

	<div id = "main" onclick = "FermeMenu()">

		<h2 style="margin-top:10px ; margin-bottom:10px">Réinitialisation du mot de passe</h2>

		<!-- après vérification, les données vont être envoyées à jeu.php grâce à la méthode post-->
		<form accept-charset="UTF-8" class="cmxform" id="ReiniMdp" method="post" action="jeu.php"> 
		<div class="container">
			<p style = "text-indent: 10px; text-align: left;">
				<label for="pseudo"><b>Pseudonyme : <?php echo $pseudo ?></b></label>
				<!-- on rajoute un input avec le pseudonyme pour le poster à la prochaine page -->
				<input name="pseudo" type="text" value="<?php echo $pseudo ?>" style="display:none">
			</p>
			<p style = "text-indent: 10px; text-align: left; ">
				<label for="qSecurite"><b>Question de sécurité : 
					<?php
						// on cherche idCompte: le numéro de la ligne correspondant au pseudonyme
						$idCompte = 0;
						foreach ($csv as $ligne) {
							if ($ligne[0] == $pseudo){break;}
							++$idCompte;
						}
						$questions = array("0"=>"Comment s'appelait votre premier animal de compagnie?",
						"1"=>"Quel était votre surnom quand vous étiez petit?",
						"2"=>"Quelle est votre équipe de sport préférée?",
						"3"=>"Quelle est votre couleur préférée?",
						"4"=>"Quel est votre animal préféré?",
						"5"=>"Quel est votre plat préféré?");
						//on cherche dans le csv des comptes l'identifiant de la question pour ce compte
						echo $questions[$csv[$idCompte][2]];
					?>
				</b></label>

				<input name="reponse" type="text" placeholder="Réponse">
			</p>
			<p style = "text-indent: 10px; text-align: left;">
				<label for="nouv_mdp"><b>Nouveau mot de passe</b></label>
				<input id="nouv_mdp" name="nouv_mdp" type="password" placeholder="Entrez un nouveau mot de passe">
				<input name="mdp_conf" type="password" placeholder="Confirmez votre mot de passe"> 
			</p>
			
			<p style = "text-indent: 10px; text-align: left;">
				<input class="boutoninscr" id="boutoninscr" type="submit" value="Confirmer">
			</p>
		</div>
		</form>
	</div>

</body>
</html>