class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        String operator = ineq+eq;
        boolean result=false;
        
        switch(operator){
            case ">=":
                result=(n>=m);
                break;
            case "<=":
                result=(n<=m);
                break;
            case ">!":
                result=(n>m);
                break;
            case "<!":
                result=(n<m);
                break;
                    
        }
        return result ?1:0;
    }
}