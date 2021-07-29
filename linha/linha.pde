
void setup()
{
  size(800,600);
}

void draw()
{
  background(155);
  float px = width/2;
  float py = height/2;
  float p2x = mouseX;
  float p2y = mouseY;
  
  beginShape();
  vertex(px,py);
  vertex(p2x,p2y);
  endShape(CLOSE);
  
}
