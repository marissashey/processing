/**
 * Words. 
 * 
 * The text() function is used for writing words to the screen.
 * The letters can be aligned left, center, or right with the 
 * textAlign() function. 
 */
  
PFont f;
  
void setup() {
  size(640, 360);
  
  // Create the font
  printArray(PFont.list());
  f = createFont("Times-Italic", 120);
  textFont(f);
}

void draw() {
  background(0);
  textAlign(LEFT);
  
  drawType(width * 0.05);
 
}

void drawType(float x) {
  line(x, 176,196,222, x, 65);
  line(x, 176,196,222, x, height);
  fill(255);
  text("an hour’s train ride whisks us from city grays", x, 80);
  text("to bay purples, blues, oranges, and greens.", x, 100);

  text("the subway entrance at qianhai bay is the only modern,",x,120);
  text("machine-made construction for miles.", x, 140);

  text("its straight and sharp-edged glass and metal", x, 160);
  text("jut out from the ground, offbeat.", x, 180);
 
  text("it is an abrupt departure from its feral surroundings,", x, 200); 
  text("where warm-colored wildflowers and dirt paths grow", x, 220);
  
  text ("where they want to.", x, 240);
  text("even more so compared to where we came from,", x, 260);
  
  text("the bay is untamed.", x, 280);
  
}
