import javax.swing.*;
//import javax.swing.border.Border;     //utilizado somente para criar bordas nos elementos. Não utilizado na versão final
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import java.awt.*;

public class Pratica012{

    public static void main(String[] args) {
        JFrame mainFrame = new JFrame();
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mainFrame.setTitle("Prática 012 - Verificador de triângulos");
        mainFrame.setSize(590, 400);
        mainFrame.setResizable(false);
        mainFrame.setLayout(null);

        /*
        Para facilitar a construção e o posicionamento dos elementos, durante a criação de cada um dos elementos deste
        programa eu deixei marcada a opção de bordas. Deste modo era muito mais simples visualizar os limites de cada um
        dos elementos, evitando sobreposições e melhorando a apresentação visual.

        Assim que todos os elementos foram devidamente posicionados eu removi as bordas de tudo. Porém, caso seja
        necessário ou do desejo de alguém colocar tais bordas, segue abaixo um exemplo de como colocar ela ao redor do
        JLabel "lblTitulo".

        Border border = BorderFactory.createLineBorder(Color.BLUE, 2);  //Determinando cor e espessura da borda
        lblTitulo.setBorder(border);
        */

        //Texto de boas vindas (JLabel)
        JLabel lblTitulo = new JLabel("Crie seu próprio triângulo e veja se ele é válido!");
        lblTitulo.setBounds(20,15,500,40);
        lblTitulo.setFont(new Font("SansSerif", Font.BOLD, 16));
        mainFrame.add(lblTitulo);

        //Identificador do Slider A
        JLabel lbl001 = new JLabel("Segmento A: ");
        lbl001.setBounds(20,55,160,40);
        lbl001.setFont(new Font("SansSerif", Font.PLAIN, 24));
        mainFrame.add(lbl001);

        //Identificador do Slider B
        JLabel lbl002 = new JLabel("Segmento B: ");
        lbl002.setBounds(20, 105, 160, 40);
        lbl002.setFont(new Font("SansSerif", Font.PLAIN, 24));
        mainFrame.add(lbl002);

        //Identificador do Slider C
        JLabel lbl003 = new JLabel("Segmento C: ");
        lbl003.setBounds(20,155, 160, 40);
        lbl003.setFont(new Font("SansSerif", Font.PLAIN, 24));
        mainFrame.add(lbl003);

        //Mostrador do valor do Slider A
        JLabel lblSegA = new JLabel();
        lblSegA.setBounds(520, 55, 40, 40);
        lblSegA.setFont(new Font("SansSerif", Font.PLAIN, 24));
        mainFrame.add(lblSegA);

        //Mostrador do valor do Slider B
        JLabel lblSegB = new JLabel();
        lblSegB.setBounds(520, 105, 40, 40);
        lblSegB.setFont(new Font("SansSerif", Font.PLAIN, 24));
        mainFrame.add(lblSegB);

        //Mostrador do valor do Slider C
        JLabel lblSegC = new JLabel();
        lblSegC.setBounds(520, 155, 40, 40);
        lblSegC.setFont(new Font("SansSerif", Font.PLAIN, 24));
        mainFrame.add(lblSegC);

        //Slider A
        JSlider sliA = new JSlider(0, 30, 0);
        sliA.setBounds(180, 65, 300, 40);
        sliA.setPaintTrack(true);
        sliA.setMajorTickSpacing(5);
        sliA.setPaintLabels(true);
        sliA.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblSegA.setText(String.valueOf(sliA.getValue()));
            }
        });
        mainFrame.add(sliA);

        //Slider B
        JSlider sliB = new JSlider(0, 30, 0);
        sliB.setBounds(180, 115, 300, 40);
        sliB.setPaintTrack(true);
        sliB.setMajorTickSpacing(5);
        sliB.setPaintLabels(true);
        sliB.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblSegB.setText(String.valueOf(sliB.getValue()));
            }
        });
        mainFrame.add(sliB);

        //Slider C
        JSlider sliC = new JSlider(0, 30, 0);
        sliC.setBounds(180, 165, 300, 40);
        sliC.setPaintTrack(true);
        sliC.setMajorTickSpacing(5);
        sliC.setPaintLabels(true);
        sliC.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                lblSegC.setText(String.valueOf(sliC.getValue()));
            }
        });
        mainFrame.add(sliC);

        //Legenda da formação do triângulo (JLabel)
        JLabel lblForm = new JLabel("Triângulo válido?");
        lblForm.setBounds(20, 255, 160, 40);
        lblForm.setFont(new Font("SansSerif", Font.PLAIN, 20));
        mainFrame.add(lblForm);

        //Legenda do tipo do triângulo (JLabel)
        JLabel lblType = new JLabel("Tipo de triângulo:");
        lblType.setBounds(20, 305, 160,40);
        lblType.setFont(new Font("SansSerif", Font.PLAIN, 20));
        mainFrame.add(lblType);

        //Resposta da formação do triângulo (JLabel)
        JLabel lblAnwserForm = new JLabel();
        lblAnwserForm.setBounds(200, 255, 380, 40);
        lblAnwserForm.setFont(new Font("SansSerif", Font.PLAIN, 20));
        mainFrame.add(lblAnwserForm);

        //Resposta do tipo do triângulo (JLabel)
        JLabel lblAnwserType = new JLabel();
        lblAnwserType.setBounds(200, 305, 380, 40);
        lblAnwserType.setFont(new Font("SansSerif", Font.PLAIN, 20));
        mainFrame.add(lblAnwserType);

        //Botão do programa
        JButton btnVerify = new JButton("Verificar");
        btnVerify.setBounds(200, 215, 200, 30);
        btnVerify.addActionListener(e -> btnPress(lblAnwserForm, lblAnwserType, sliA.getValue(), sliB.getValue(), sliC.getValue()));
        mainFrame.add(btnVerify);

        mainFrame.setVisible(true);     //Após todos os elementos serem adicionados ao mainFrame, o programa deixa-o visível
    }

    //Método para definir as ações que o botão deve executar quando apertado (que é essencialmente realizar os cálculos)
    public static void btnPress(JLabel lbl1, JLabel lbl2, int a, int b, int c){
        if(a<b+c && b<a+c && c<a+b){
            lbl1.setText("Triângulo válido!");
            if(a==b && b==c)
                lbl2.setText("triângulo equilátero.");
            else if(a==b || b==c || a==c)
                lbl2.setText("triângulo isóceles.");
            else
                lbl2.setText("triângulo escaleno.");
        } else{
            lbl1.setText("Não forma um triângulo!");
            lbl2.setText("NaN");
        }
    }
}