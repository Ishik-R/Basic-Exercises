import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Date;

public class TelaRelogio extends JFrame{
    private JLabel lblCalendario;
    private JButton cliqueAquiButton;
    private JLabel lblHora;
    private JLabel btnHora;
    private JPanel mainPanel;
    private JLabel lblTitulo;

    public TelaRelogio() {
        cliqueAquiButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Date relogio = new Date();
                lblHora.setText(relogio.toString());
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame01 = new JFrame("Prática 003: Relógio em Swing");
        frame01.setContentPane(new TelaRelogio().mainPanel);
        frame01.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame01.pack();
        frame01.setVisible(true);
    }

}
