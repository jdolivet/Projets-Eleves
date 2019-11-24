//global variable
points=0;//score du début
life=3;//nombre de vies
let snow = []; // array of Jitter objects
friction=0.001;//coefficient de frottement

function setup(){//création des elements: cible, balle, snow, canvas
  g = random(30, 320); // intervalle ds lequel est compris g (y) du target
  j = random(20,(width/2)+60);
  w = random(10, 50);
  h = random(10, 50);
  cnv = createCanvas(350, 450);
  ball = new ball;
  target = new target;
  
  // snow array
  vx_flake=random(5);//vitesse des flocons
  vy_flake=random(5);
  for (let i = 0; i < 30; i++) { //tableau de flocons – quand un flocon sort du canvas un autre entre de l’autre côté ( nb de flocons est constant)

    snow.push(new flake());
  }
}

function draw(){//dessiner les elements
  //nettoyer background
    background(220);
  
  if (life>0){//si vies sup à 0
    //actualise snow
    for (let i = 0; i < snow.length; i++) {
      snow[i].move();
      snow[i].display();
    }
    //actualise cible
      ball.update();
      ball.show();

      target.show();
      DrawForce();//droite de l'intensité de la force
      score();   //montrer score
      life_print();   //montrer nb de vies
  }else{ //fin du jeu
      //montrer message
      fill(0);
      textSize(50);
      scoretext = text('You Loose', width/2-120, height/2-100, 400, 400);
  }
} 

class target{
  update(){
    g = random(30, 320);//nb aleat entre 30 et 320
    j = random(20,(width/2)+60);//je garantis que la cible est dans une partie supérieure, pour qu'il soit au dessus de la balle 
    w = random(10, 50);
    h = random(10, 50);
  }
  show(){
    fill(0);//couleur
    rect(g, j, w, h);
  }
}

function DrawForce(){
  stroke(0);
    x = width/2;//position balle
    y = 9*height/10;
    cx = x - mouseX;//position du mouse
    cy = y - mouseY;
    //a = x + mouseX;
    //b = y + mouseY;
    line(x, y, x+cx, y+cy);
    stroke(220);
  print ('on')
}


function mousePressed(){
    x = width/2;
    y = 9*height/10;
    cx = x - mouseX;
    cy = y - mouseY;
    ball.throw=1;
    if(ball.Vx==0 && ball.Vy==0){ //solution du pb du double click: la fonction mouse pressed ne fonctionne que si la balle est immobile
      ball.Vx= cx/2+vx_flake;
      ball.Vy= cy/2+vy_flake;
    }

}
function score(){ //affichage du score
  fill(0);
  scoretext = text('SCORE:' + points , width/2, 30, 25, 25);
}

function life_print(){ //affichage des vies
  fill(0);
  scoretext = text('Lifes:' + life , width/2, 10, 25, 25);
}



