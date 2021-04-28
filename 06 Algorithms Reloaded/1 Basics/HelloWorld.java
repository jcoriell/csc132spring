/* The public class name has to match the file name
   Only one public class per file */
// public makes the class available outside of the 'package'
public class HelloWorld{

    // public before a method means the method is accessible outside the class
    // (private means its only accessible within the class)
    /* static enforces the idea that there is only 1 'main' function for ...
       objects from that class */
    // void means the method/function doesn't return anything
    // String[] means 'args' is an array of strings
    public static void main(String[] args){
        // Sytem is a class and out is an object (for output) in that class
        System.out.println("Hello World"); // statements must end with semicolons
        // Scope: c doesn't exist here: System.out.println(c);
    }
}


// Data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class VariablesAndConstants{

    public static void main(String[] args){

        // variables are created with their types
        int a = 5;
        int b = 3;

        // 5 + 3 = 8 
        System.out.println(a + "+" + b + "=" + (a + b));
        System.out.println(a);

        // formatting like in python. use %s for a string, %d is for decimal integer. 
        // These are called format specifier
        System.out.println(String.format("a = %s" , a));
        System.out.println(String.format("a = %d, b = %s", a, b));

        final int THIS_IS_A_CONSTANT = 5;
        // Can't do this: THIS_IS_A_CONSTANT = 8;
        System.out.println(THIS_IS_A_CONSTANT);
        
        //
        int c;
        c = 7;
        System.out.println(c);

    }
}

class DataTypeExamples{

    public static void main(String[] args){
        int a;
        float numberPointZero; // 32 bit numbers
        double bigNumberPointZero; // 64 bit number
        String textTextText;
        char aSingleCharacter;
        boolean trueFalse;

        a = 1;
        System.out.println(a);

        // double data type (note that the stuff on the right of = is a double (literally))
        bigNumberPointZero = 37487348.474;
        // data type must match. this doesn't: bigNumberPointZero = "hello";
        System.out.println(bigNumberPointZero);

        // casting the double literal value to a float
        numberPointZero = (float) 1.7; // (float) casts 1.7 to a float
        numberPointZero = 1.8f; //the little f specifies 1.8 is a float
        System.out.println(numberPointZero);

        // string uses double quote
        textTextText = "this is a string";
        System.out.println(textTextText);

        // booleans
        trueFalse = true;
        trueFalse = false;
        System.out.println(trueFalse);

        // char uses single quotes
        aSingleCharacter = 'h';
        // There are numbers associated with characters: aSingleCharacter = 8;
        aSingleCharacter = 63; // a questionmark (see: ascii)
        System.out.println(aSingleCharacter);
        
    }
}


// fixed in size, uniform pieces of data
class ArrayExamples{

    public static void main (String[] args){
        // initilize
        int x; // not an array
        int[] y; // is an array of integers

        // creating an array of a specific size
        double[] nums = new double[10];
        System.out.println(nums);
        System.out.println(nums.length);    // getting it's length
        System.out.println(nums[0]); // accessing the 0th element

        nums[0] = 8;    // changing the 0th element
        System.out.println(nums[0]);

        int[] grades = {80, 70, 90, 100};
        String[] names = {"not josh", "philip", "colin", "87roiwru - elon's child"};

    }
}


// Operators ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ArithmeticOperators {
    public static void main(String[] args){
        System.out.println(1 + 2); //addition
        System.out.println(1 - 2); //subtraction
        System.out.println(1 * 2); //multiplication
        
        System.out.println(1 / 2); // integer division, result is 0
        System.out.println(1f / 2); // float division, results 
        System.out.println((float) 1 / 2); // float division
        
        System.out.println((double) 1 / 2); // double division
        System.out.println(5 % 2); //mod
        System.out.println(Math.pow(2,3)); // 2 to the power of 3

    }
}
