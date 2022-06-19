import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Pratica009 extends JFrame{
    private JPanel mainPanel;
    private JButton btnPalpite;
    private JLabel lblBaloon;
    private JLabel lblAnswer;
    private JSpinner spinner1;
    private JLabel lblGenie;

    public Pratica009 (String title){
        super(title);

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(mainPanel);
        this.pack();

        lblBaloon.setText("Tente adivinhar o número que eu estou pensando entre 1 e 5!");
        lblBaloon.setHorizontalTextPosition(JLabel.CENTER);

        btnPalpite.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                int genieN = (int) (1 + Math.random() * (6 - 1));
                int yourN = Integer.parseInt(spinner1.getValue().toString());
                if (genieN == yourN){
                    lblBaloon.setText("Boa! Tente adivinhar o número que eu estou pensando entre 1 e 5!");
                    lblAnswer.setText("Você acertou!");
                }
                else if (yourN < 1 || yourN > 5){
                    lblBaloon.setText("O número deve estar entre 1 e 5!");
                    lblAnswer.setText("");
                } else{
                    lblBaloon.setText("Quase! Tente adivinhar o número que eu estou pensando entre 1 e 5!");
                    lblAnswer.setText("Você errou! O número era " + genieN);
                }
            }
        });
    }

    public static void main(String[] args) {
        JFrame p009Frame = new Pratica009("Prática 009 - adivinhador");
        p009Frame.setVisible(true);
        p009Frame.setResizable(false);
    }

}
