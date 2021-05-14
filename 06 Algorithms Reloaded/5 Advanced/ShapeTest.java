public class ShapeTest {
    public static void main(String[] args){
        Rectangle myRectangle = new Rectangle(4, 3);
        myRectangle.draw();

        Square mySquare = new Square(4);
        mySquare.draw();

        Triangle myTriangle = new Triangle(3);
        myTriangle.draw();
    }
}

// abstract means we cannot instantiate a Shape object
abstract class Shape{

    // available for this class and subclasses
    protected int length;
    protected int width;

    // constructor
    public Shape(int l, int w){
        length = l;
        width = w;
    }

    public void draw(){
        for (int i = 0; i < width; i++){
            for (int j = 0; j < length; j++){
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println();
    }
}

// inheritance is done with the keyword extends
class Rectangle extends Shape{
    public Rectangle(int l, int w){
        super(l, w);
    }
}

class Square extends Shape{
    public Square(int s){
        super(s, s);
    }
}

class Triangle extends Shape{
    public Triangle(int s){
        super(s, s);
    }

    public void draw(){
        for (int i = 0; i < width; i++){
            for(int j=0; j < width - i; j++){
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
