import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Pratica007 extends JFrame{
    private JSpinner spinnerNumber;
    private JButton calcularButton;
    private JPanel mainPanel;
    private JLabel lblValorAbsoluto;
    private JLabel lblCubicRoot;
    private JLabel lblSquareRoot;
    private JLabel lblRest;
    private JPanel panelResults;
    private JLabel lblCalculatorImage;

    public Pratica007(String title){
        super(title);

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(mainPanel);
        this.pack();

        panelResults.setVisible(false);

        calcularButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int number = Integer.parseInt(spinnerNumber.getValue().toString());
                panelResults.setVisible(true);

                //Resto da divisão por 2:
                lblRest.setText(Integer.toString(number%2));

                //Raiz quadrada:
                //Também seria possível exibir o resultado sem o String.format: lblSquareRoot.setText(Double.toString(Math.sqrt(number)));
                double sqroot = Math.sqrt(number);
                lblSquareRoot.setText(String.format("%.2f",sqroot));    //Arredondamento para duas casas decimais

                //Raiz cúbica:
                //Também será possível exibir o resultado sem o String.format: lblCubicRoot.setText(Double.toString(Math.cbrt(number)));
                double cbroot = Math.cbrt(number);
                lblCubicRoot.setText(String.format("%.2f", cbroot));    //Arredondamento para duas casas decimais

                //Valor absoluto:
                lblValorAbsoluto.setText(Integer.toString(Math.abs(number)));
            }
        });
    }

    public static void main(String[] args) {
        JFrame p007Frame = new Pratica007("Pratica 007 - Funções Math");
        p007Frame.setVisible(true);
    }

}
