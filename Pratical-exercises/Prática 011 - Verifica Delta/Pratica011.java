import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Pratica011 extends JFrame {
    private JPanel mainPanel;
    private JButton btnCalcular;
    private JSpinner spinnerA;
    private JSpinner spinnerB;
    private JSpinner spinnerC;
    private JLabel lblDelta1;
    private JLabel lblB;
    private JLabel lblA;
    private JLabel lblC;
    private JLabel lblDeltaID;
    private JLabel lblTipoResp;
    private JLabel lblValorDelta;
    private JLabel lblDeltaExp2;
    private JLabel lblDeltaExp1;
    private JLabel lblTipoID;

    public Pratica011(String title){
        super(title);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(mainPanel);
        this.pack();

        lblDelta1.setText("\u0394 = ");
        lblDeltaID.setText("\u0394 = ");
        lblDeltaExp1.setText(" - 4 * ");
        lblDeltaExp2.setText(" * ");
        btnCalcular.setText("Calcular!");
        btnCalcular.setSize(100,50);

        //ChangeListener que promove a mudança do valor de A toda vez que o spinnerA tiver seu valor alterado
        spinnerA.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblA.setText(spinnerA.getValue().toString());
            }
        });

        //ChangeListener que promove a mudança do valor de B toda vez que o spinnerB tiver seu valor alterado
        spinnerB.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblB.setText(spinnerB.getValue().toString());
            }
        });

        //ChangeListener que promove a mudança do valor de C toda vez que o spinnerC tiver seu valor alterado
        spinnerC.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblC.setText(spinnerC.getValue().toString());
            }
        });

        //ActionListener que promove a funcionalidade do botão de calcular para que ele exiba os resultados de Delta
        btnCalcular.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                //Exiba os valores de A, B e C mesmo que o usuário não tenha mexido nos spinners.
                lblA.setText(spinnerA.getValue().toString());
                lblB.setText(spinnerB.getValue().toString());
                lblC.setText(spinnerC.getValue().toString());

                int a = Integer.parseInt(spinnerA.getValue().toString());
                int b = Integer.parseInt(spinnerB.getValue().toString());
                int c = Integer.parseInt(spinnerC.getValue().toString());
                int delta = (b * b) - (4 * a * c);
                lblValorDelta.setText(String.valueOf(delta));

                if(delta > 0)
                    lblTipoResp.setText("Possui raízes reais.");
                else if(delta == 0)
                    lblTipoResp.setText("Possui raízes reais de mesmo valor.");
                else
                    lblTipoResp.setText("Não possui raízes reais.");
            }
        });
    }

    public static void main(String[] args){
        JFrame p011frame = new Pratica011("Prática 011 - Verifica Delta");
        p011frame.setSize(420,230);
        p011frame.setResizable(false);
        p011frame.setVisible(true);
    }

}
