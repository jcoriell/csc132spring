

class Conditionals{

    public static void main(String[] args){
        double score = 85.0;
        char letterGrade;

        letterGrade = calcScore(score);
        System.out.println(letterGrade);
    }

    public static char calcScore(double value){
        if (value >= 89.5){
            return 'A';
        }
        else if (value >= 79.5){
            return 'B';
        }
        else if (value >= 69.5){
            return 'C';
        }
        else if (value >= 59.5){
            return 'D';
        }
        else{
            return 'F';
        }

    }

}

class SwitchExample{
    public static void main(String[] args){
        char letterGrade = 'A';
        String feedback;
        String generalizedFeedback;

        feedback = determineFeedback(letterGrade);  
        System.out.println(feedback);  

        generalizedFeedback = lessSpecificFeedback(letterGrade);
        System.out.println(generalizedFeedback)
    }

    // without fallthrough
    public static String determineFeedback(char grade){
        // switch conditions are restricted to certain datatypes 
        // (char, int, string, a few others)
        switch (grade){
            case 'A': 
                String name = "Everybody";
                return "Excellent Job, " + name;
            case 'B': return "Great Job";
            case 'C': return "Good Job";
            case 'D': return "Poor Job";
            case 'F': return "Maybe next time";
            default: return "Not a valid grade"; // catch all case
        }
    }

    // with fallthrough
    public static String lessSpecificFeedback(char grade){
        switch (grade){
            case 'A':
            case 'B': return "Great Job";
            case 'C': return "Good Job";
            case 'D': 
            case 'F': return "Maybe next time";
            default : return "Not a valid grade"; 
        }
    }

}