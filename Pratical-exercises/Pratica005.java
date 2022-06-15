package classes;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Pratica005 extends JFrame{
    private JSpinner spinnerBoltCasts;
    private JButton buttonBolt;
    private JLabel labelShowDamage;
    private JLabel labelBoltImage;
    private JPanel mainPanel;

    public Pratica005(String title){
        super(title);

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(mainPanel);
        this.pack();

        buttonBolt.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int damage = Integer.parseInt(spinnerBoltCasts.getValue().toString()) * 3;

                if(damage >= 0)
                    labelShowDamage.setText(Integer.toString(damage));
                else
                    labelShowDamage.setText("??");
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new Pratica005("Pratica 005 - Lightning Bolting!");
        frame.setVisible(true);
    }
}
