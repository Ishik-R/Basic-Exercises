import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Pratica017 extends JFrame {
    private JPanel mainFrame;
    private JSlider sliStart;
    private JSlider sliFinish;
    private JSlider sliStep;
    private JButton btnExecute;
    private JList listNumbers;
    private JLabel lblStart;
    private JLabel lblFinish;
    private JLabel lblStep;

    public Pratica017(String title){
        super(title);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(mainFrame);
        this.pack();

        sliStart.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblStart.setText(String.valueOf(sliStart.getValue()));
            }
        });

        sliFinish.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblFinish.setText(String.valueOf(sliFinish.getValue()));
            }
        });

        sliStep.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblStep.setText(Integer.toString(sliStep.getValue()));  //Mudei o método de conversão somente para dar uma variada
            }
        });

        btnExecute.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int start = sliStart.getValue();
                int finish = sliFinish.getValue();
                int step = sliStep.getValue();

                DefaultListModel lista = new DefaultListModel();
                for(int c=start; c<=finish; c+=step){
                    lista.addElement(c);
                }

                listNumbers.setModel(lista);
            }
        });

    }

    public static void main(String[] args) {
        JFrame p017frame = new Pratica017("Prática 017 - Incrementador");
        p017frame.setSize(500, 550);
        p017frame.setLocationRelativeTo(null);
        p017frame.setVisible(true);
    }

}
