

class Repetition {
    
    public static void main(String[] args){

        // While loops ~~~~~~~~~~

        // while loop
        int i = 0;
        while (i < 10){
            i++;
        }
        System.out.println("After the while loop, i = " + i);

        // do while: executes at least 1, then checks the condition
        i = 0;
        do {
            i--;
        }while(i>0);
        System.out.println("After the do while loop, i = " + i);

        // For loops ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        // general structure: for (initialization; condition ; change)
        for (int j = 0; j < 10; j++){
            System.out.print(j + " ");
        }
        System.out.println();

        // counting by not 1. (two in this case)
        for (int j = 0; j < 10; j+=2){
            System.out.print(j + " ");
        }
        System.out.println();

        // more than one condition
        for (int j = 0, k = 0; j < 10 && k < 10; j++, k+=2){
            System.out.print("(" + j + "," + k + ")");
        }
        System.out.println();

        // for each item in an array - loop
        // creating an array
        double[] mathConstants = new double[5];

        mathConstants[0] = 3.1415; // pi
        mathConstants[1] = 2.72; // e, euler's number
        mathConstants[2] = 1.73; // sqrt(2)
        mathConstants[3] = 1.62; // phi - golden ratio

        System.out.print("My Math Constants: ");
        // for each loop
        for (double d : mathConstants){
            System.out.print(d + " ");
        }
        System.out.println();
    }
}


