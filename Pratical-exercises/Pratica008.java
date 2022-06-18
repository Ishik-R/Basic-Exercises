import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.time.LocalDate;

public class Pratica008 extends JFrame{
    private JPanel mainPanel;
    private JSpinner spinnerAge;
    private JButton btnCalc;
    private JLabel lblShowAge;
    private JLabel lblShowVote;

    public Pratica008(String title){
        super(title);

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(mainPanel);
        this.pack();

        btnCalc.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                //Verificar o ano em que estamos pelo LocalDate.now().getYear()
                int currentYear = LocalDate.now().getYear();

                //Carregar a entrada do Jspinner (uma String) para um valor int
                int birthYear = Integer.parseInt(spinnerAge.getValue().toString());

                //Calcular a idade da pessoa
                int age = currentYear - birthYear;

                //Verificar a obrigatoriedade do voto (de acordo com a idade) e realizar a saída nos devidos Labels.
                lblShowAge.setText(Integer.toString(age));
                if(age < 0)
                    lblShowVote.setText("Você não nasceu ainda! o.o");
                else if(((age < 18) && (age > 16)) || (age > 70))
                    lblShowVote.setText("Voto facultativo.");
                else if(age > 18 && age < 70)
                    lblShowVote.setText("Voto obrigatório.");
                else
                    lblShowVote.setText("Você é novo demais para votar.");
            }
        });
    }

    public static void main(String[] args) {
        JFrame p008Frame = new Pratica008("Pratica 008 - Verificador de idade");
        p008Frame.setResizable(false);
        p008Frame.setVisible(true);
    }

}
