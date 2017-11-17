<?php

// C veut dire choix et O veut dire option (C1O1 = Choix 1, Option 1).
$choix = $_GET['choix'];
$pseudo = $_GET['pseudo'];

// La fonction file transforme chaque ligne d'un fichier en élément d'un array.
// La fonction array_map exécute la fonction str_csv sur chacun des élément de l'array créé grâce à file.
// La fonction str_getcsv sépare les éléments de chaque ligne en éléments d'un array.
$csv = array_map("str_getcsv", file("comptes.csv"));

// On cherche à quel index de l'array corresopond le choix fait par l'utilisateur et augmente de 1 la case correspondante.
$idCompte = 0;
foreach ($csv as $ligne) {
    if ($ligne[0] == $pseudo){
        if (substr($choix, 0, 3) == "Fin"){
            $csv[$idCompte][6] = $choix;
        } else {
            $csv[$idCompte][5] .= $choix;
        }
        break;
    }
    ++$idCompte;
}

// On transforme l'array en chaîne de caractères en format csv.
$nouveauxContenu = "";
foreach ($csv as $ligne) {
    $nouveauxContenu .= implode(",", $ligne)."\r\n";
}

// On remplace le contenu du fichier statistiques par le contenu modifié.
$fichier = fopen("comptes.csv", "w");
fputs($fichier, $nouveauxContenu);
fclose($fichier);

?>