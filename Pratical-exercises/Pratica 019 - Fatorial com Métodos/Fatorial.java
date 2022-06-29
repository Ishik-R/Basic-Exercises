package classes;

public class Fatorial {
    
    private int num = 0;
    private int fat = 1;
    private String exp = "0";
    
    public void setValor(int n){
        exp = "";
        num = n;
        int f = 1;
        String s = "";
        for(int c = n; c > 1; c--){
            f *= c;
            s += c + " x ";
        }
        s += "1";
        exp = s;
        fat = f;
    }
    
    public int getFatorial(){
        return fat;
    }
    
    public String getExpressao(){
        return exp;
    }
    
}
