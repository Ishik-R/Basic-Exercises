import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Pratica010 extends JFrame{

    private JPanel MainPanel;
    private JButton btnVerify;
    private JTextField txtValor;
    private JLabel lblResult;

    public Pratica010 (String title){
        //Elementos gerais da criação do Swing.
        super(title);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(MainPanel);
        this.pack();

        //Listener da ação do botão btnVerify
        btnVerify.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int num = Integer.parseInt(txtValor.getText().toString());
                if (num % 2 == 0)
                    lblResult.setText(num + " é par!");
                else
                    lblResult.setText(num + " é ímpar!");
            }
        });
    }

    public static void main(String[] args) {
        JFrame p010Frame = new Pratica010("Prática 010 - Par ou ímpar?");
        p010Frame.setSize(340,140);
        p010Frame.setResizable(false);
        p010Frame.setVisible(true);
    }

}
