import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Pratica014 extends JFrame{
    private JPanel mainPanel;
    private JButton btnContar;
    private JLabel lblCount;
    private JSpinner spiNum;

    public Pratica014(String title){
        super(title);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(mainPanel);
        this.pack();

        btnContar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(spiNum.getValue().hashCode()<=0) {
                    lblCount.setText("Insira um número natural não nulo para a contagem.");
                } else if(spiNum.getValue().hashCode()>26){
                    lblCount.setText("Valor grande demais para a tela, desculpe!");
                } else{
                    String text = "";
                    for(int i=1; i<=spiNum.getValue().hashCode(); i++){
                        text += i + " ";
                    }
                    lblCount.setText(text);
                }
            }
        });
    }

    public static void main(String[] args) {
        JFrame p014frame = new Pratica014("Prática 014 - Contador");
        p014frame.setLocationRelativeTo(null);
        p014frame.setSize(500, 150);
        p014frame.setResizable(false);
        p014frame.setVisible(true);
    }

}
