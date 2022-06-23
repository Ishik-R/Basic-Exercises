import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

public class Pratica015 extends JFrame{
    private JPanel mainPanel;
    private JSpinner spiNum;
    private JLabel lblResult;

    public Pratica015(String title){
        super(title);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(mainPanel);
        this.pack();

        spiNum.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                if(spiNum.getValue().hashCode() >= 0 && spiNum.getValue().hashCode() < 13){
                    int result = 1;
                    for(int i = 1; i <= spiNum.getValue().hashCode(); i++)
                        result = result * i;
                    lblResult.setText(String.valueOf(result));
                } else if(spiNum.getValue().hashCode() > 12){
                    lblResult.setText("grande demais!");
                } else{
                    lblResult.setText("valor inválido!");
                }
            }
        });
    }

    public static void main(String[] args) {
        JFrame p015frame = new Pratica015("Prática 015 - Fatorial");
        p015frame.setSize(440,100);
        p015frame.setLocationRelativeTo(null);
        p015frame.setVisible(true);
    }
}
