  
  float p2x = 100;
  float p2y = 400;
  float p3x = 700;
  float p3y = 400;
  
void setup()
{
  size(800,600);
}

void draw()
{
  background(128);
  float p1x = 100;
  float p1y = 100;
  float p4x = 700;
  float p4y = 100;

  if(mousePressed == true)
  {
    p2x = mouseX;
    p2y = mouseY;
    
  }else
  {
    p3x = mouseX;
    p3y = mouseY;
  }
  
  beginShape();
  vertex(p1x, p1y);
  for(float t = 0; t <= 1; t += 0.01)
  {
    float ax = p1x + t*(p2x-p1x);
    float bx = p2x + t*(p3x-p2x);
    float cx = p3x + t*(p4x-p3x);
    float rx = ax + t*(bx-ax);
    float sx = bx + t*(cx-bx);
    float fx = rx + t*(sx-rx);
    
    float ay = p1y + t*(p2y-p1y);
    float by = p2y + t*(p3y-p2y);
    float cy = p3y + t*(p4y-p3y);
    float ry = ay + t*(by-ay);
    float sy = by + t*(cy-by);
    float fy = ry + t*(sy-ry);
    
    vertex(fx,fy);  
  }
  vertex(p4x, p4y);
  endShape(CLOSE);
}
