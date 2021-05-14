
class FractionAction{

    public static void main(String[] args){
        // instantiate a fraction
        Fraction f = new Fraction(); 
        System.out.println(f);

        // testing getters and setters
        System.out.println(f.getNumerator());
        System.out.println(f.getDenominator());
        System.out.println(f);
        f.setNumerator(4);
        f.setDenominator(0);
        System.out.println(f);

        // testing our second constructor
        Fraction f2 = new Fraction(1,2);
        System.out.println(f2);

        // testing reduce
        Fraction f3 = new Fraction(10, 20);
        System.out.println(f3);
    }

}


class Fraction {
    // instance variables
    private int numerator;  //private means we can only modify this inside the class
    private int denominator;

    // constructor; public so we can instantiate instances; name matches the class
    public Fraction(){
        numerator = 0;
        denominator = 1;
    }

    // second constructor with parameters
    public Fraction(int num, int den){
        numerator = num;
        if (den != 0){
            denominator = den;
        }
        else{
            denominator = 1;
        }
        reduce();
    }

    // accessors/mutators - getters/setters
    public int getNumerator(){
        return numerator;
    }

    public void setNumerator(int val){
        numerator = val;
        reduce();
    }

    public int getDenominator(){
        return denominator;
    }

    public void setDenominator(int val){
        if (val != 0){
            denominator = val;
            reduce();
        }
    }

    public void reduce(){
        int gcd = 1;
        int min = Math.min(Math.abs(numerator), Math.abs(denominator));

        // checking for divisibility
        for (int i = 2; i <= min; i++){
            if (numerator % i == 0 && denominator % i == 0){
                gcd = i;
            }
        }

        numerator /= gcd;
        denominator /= gcd;

        if (numerator == 0){
            denominator = 1;
        }
    }

    public Fraction add(Fraction f){
        // try creating this
    }

    // a method like __str__
    public String toString(){
        return numerator + "/" + denominator;
    }
}


