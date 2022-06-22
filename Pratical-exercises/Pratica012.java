import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Pratica012 extends JFrame{

    private JPanel mainPanel;
    private JSlider sliA;
    private JSlider sliB;
    private JSlider sliC;
    private JButton btnVer;
    private JLabel lblForm;
    private JLabel lblType;
    private JLabel lblA;
    private JLabel lblB;
    private JLabel lblC;
    private JPanel panAnwser;
    private JLabel lblTypeId;

    public Pratica012(String title){
        super(title);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(mainPanel);
        this.pack();

        panAnwser.setVisible(false);

        btnVer.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                panAnwser.setVisible(true);
                int a = sliA.getValue();
                int b = sliB.getValue();
                int c = sliC.getValue();

                if(a<b+c && b<a+c && c<a+b){
                    lblForm.setText("Yes, it's a valid triangle.");
                    lblTypeId.setText("Type of the triangle:");
                    if(a==b && b==c)
                        lblType.setText(" equilateral triangle.");
                    else if(a==b || b==c || c==a)
                        lblType.setText(" isoceles triangle.");
                    else
                        lblType.setText(" scalene triangle.");
                } else{
                    lblForm.setText("No, it isn't a valid triangle.");
                    lblTypeId.setText("---");
                    lblType.setText("");
                }

            }
        });

        sliA.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblA.setText(String.valueOf(sliA.getValue()));
            }
        });

        sliB.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblB.setText(String.valueOf(sliB.getValue()));
            }
        });

        sliC.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblC.setText(String.valueOf(sliC.getValue()));
            }
        });
    }

    public static void main(String[] args) {
        JFrame p012Frame = new Pratica012("Prática 012 - Triangles!");
        p012Frame.setSize(400,250);
        p012Frame.setResizable(false);
        p012Frame.setVisible(true);
    }

}
