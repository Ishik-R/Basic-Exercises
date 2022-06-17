package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;

public class Controller {
    @FXML
    public Label lblMessage;

    public void pressButton(ActionEvent event){
        System.out.println("The button was clicked");
        lblMessage.setText("Hello world!");
    }
}
