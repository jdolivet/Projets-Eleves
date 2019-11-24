// flake class: flake est dans le tableau snow (snow contient plusieurs flakes)
class flake {
  constructor() {
    this.x = random(width);
    this.y = random(height);
    this.diameter = 7;
    this.speedx = vx_flake; //on associe la vitesse this.speedx à la valeur dans sketch de vx_flake
    this.speedy = vy_flake; //on associe la vitesse this.speedy à la valeur dans sketch de vy_flake
  }
  update(){
    this.speedx=vx_flake;
    this.speedy=vy_flake;
  }

  move() {
    this.x += this.speedx;//pour actualiser la position je prends x2 et j'associe x1+vitesse
    this.y += this.speedy;
  }

  display() { //on vérifie si le flake est dans la canvas
    if (this.x >width||this.y>height){
      this.x = random(width);
      this.y = random(height);
    }else{
      fill(255,250,250); // couleur
      ellipse(this.x, this.y, this.diameter, this.diameter);
    }
  }
}

