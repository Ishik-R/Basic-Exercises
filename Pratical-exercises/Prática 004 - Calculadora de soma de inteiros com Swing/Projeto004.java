import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Projeto004 extends JFrame{
    private JPanel mainPanel;
    private JTextField textField1;
    private JTextField textField2;
    private JButton btnEqual;
    private JLabel labelResult;

    public Projeto004(String title){
        super(title);

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(mainPanel);
        this.pack();
        btnEqual.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int n1 = Integer.parseInt(textField1.getText());
                int n2 = Integer.parseInt(textField2.getText());
                labelResult.setText(Integer.toString(n1+n2));
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new Projeto004("Pratica 004");
        frame.setVisible(true);
    }
}
