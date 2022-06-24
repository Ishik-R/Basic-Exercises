import javax.swing.JOptionPane;
import java.text.DecimalFormat;

public class Pratica016 {

    public static void main(String[] args) {
        int n;
        int sum = 0;
        int evenN = 0;
        int oddN = 0;
        int over100 = 0;
        int inputs = 0;

        do{
            n = Integer.parseInt(JOptionPane.showInputDialog(null, "<html>Prática 016 - Introdução ao JOptionPane <br>Insira um número <em>(zero interromperá a execução)</em></html>"));
            if(n==0)
                break;
            sum += n;
            inputs++;
            if(n > 100)
                over100++;
            if(n % 2 == 0)
                evenN++;
            else
                oddN++;
        } while(n != 0);

        float average = (float) sum / inputs;
        DecimalFormat df = new DecimalFormat("#.##");

        JOptionPane.showMessageDialog(null,
                "<html>Resultado final:<hr><br> " +
                        "Números entrados: " + inputs + "<br>" +
                        "Soma dos números: " + sum + "<br>" +
                        "Total de pares: " + evenN + "<br>" +
                        "Total de ímpares: " + oddN + "<br>" +
                        "Acima de 100: " + over100 + "<br>" +
                        "Média: " + df.format(average) + "</html>");

    }

}
