import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MainFrame extends JFrame{
    private JLabel lb1;
    private JButton okButton;
    private JPanel mainPanel;

    public MainFrame(){
        setContentPane(mainPanel);
        setTitle("Bem-vindo!");
        setSize(500, 300);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setVisible(true);

        okButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                lb1.setText("Olá mundo!");
            }
        });
    }

    public static void main(String[] args) {
        MainFrame meuFrame = new MainFrame();
    }

}
