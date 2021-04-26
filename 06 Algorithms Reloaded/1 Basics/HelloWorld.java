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
    }
}