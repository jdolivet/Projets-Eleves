class ball{
  constructor(){
    this.throwed=0;
    this.x=width/2; //coordonnées position initiale
    this.y=9*height/10;
    this.Vx=0;
    this.Vy=0; 
    this.size=10;//taille en pixels
  }
  update(){//vérifier position de la balle et actualiser

    if(this.Vx!=0 && this.Vy!=0){ //quand vitesse différente de 0 (!)

      // x=x0+v*t+a/2*t*t

     //équation du mouv. uniformément varié

      // correspond à  x=x0+ v*t*constant + constant*t*t //cette équation change la vitesse et donc la position de la balle (obs: 0.02 cst de la vitesse)
      this.x=this.x+this.Vx*deltaTime*0.02+friction*deltaTime*deltaTime;//deltatime=t
      this.y=this.y+this.Vy*deltaTime*0.02+friction*deltaTime*deltaTime;
    }
    if(this.x>width || this.x<0){ // balle est en dehors du canvas
      this.x=width/2;
      this.y=9*height/10;
      this.Vx=0;
      this.Vy=0;
      life=life-1; 
    }
    if(this.y>height || this.y<0){ // balle est en dehors du canvas
      this.x=width/2;
      this.y=9*height/10;
      this.Vx=0;
      this.Vy=0;      
      life=life-1;
    }
    
   // on vérifie si la balle atteint la cible
    //cela permet de limiter les bornes de la cible rect. : limite supérieure gauche; limite inférieure gauche; limite supérieure droite; limite inférieure droite
    if(this.y<=j+h+this.size/2 && this.y>=j-this.size/2 && this.x<=g+w+this.size/2 && this.x>=g-this.size/2){
      this.x=width/2;
      this.y=9*height/10;
      this.Vx=0;
      this.Vy=0;
      points+=1;  //on rajoute 1 point
      target.update(); //on remet une nouvelle cible aleat

      vx_flake=random(5); // on actualise la vitesse des flocons
      vy_flake=random(5);
      //on actualise la snow (=tempête) avec plusieurs flocons
      for (let i = 0; i < snow.length; i++) {
        snow[i].update();//actualise vitesse
        snow[i].move();//actualise position
        snow[i].display();//redessine flake
      }      
    }
  }
  show(){
    fill(200, 35, 90);
    stroke(0);
    ellipse(this.x,this.y,this.size,this.size);
  }
}