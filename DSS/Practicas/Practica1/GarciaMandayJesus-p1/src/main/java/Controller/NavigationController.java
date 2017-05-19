package Controller;

import javax.faces.event.ActionEvent;
import java.io.Serializable;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.RequestScoped;
import javax.faces.bean.SessionScoped;

@ManagedBean(name = "navigationController", eager = true)
@SessionScoped
public class NavigationController implements Serializable{

	private static final long serialVersionUID = 1L;
	private static final boolean OFF = false;
	private static final boolean ON = true;
	private static final String BNT_TXT_ON = "Encender";
	private static final String BNT_TXT_ACELERAR = "Acelerar";
	private static final String BNT_TXT_OFF = "Apagar";
	private static final String TXT_TITLE_ON = "ENCENDIDO";
	private static final String TXT_TITLE_OFF = "APAGADO";
	private static final String TXT_TITLE_ACELERANDO = "ACELERANDO";
	private final String COLOR_RED = "red";
	private final String COLOR_GREEN = "green";
	private final String COLOR_BLUE = "blue";
	private final String ID_BTN_ONOFF = "btnOnOff";
	private final String ID_BTN_ACELERAR = "btnAcelerar";
	
	private boolean state = OFF;
	private String buttonID;
	private String textTitle = TXT_TITLE_OFF;
	private String colorTitle = COLOR_RED;
	private String textBtnOnOff = BNT_TXT_ON;
	private String colorBtnOnOff = COLOR_GREEN;
	private String textBtnAcelerar = BNT_TXT_ACELERAR;
	private String colorBtnAcelerar = COLOR_RED;
	
	
	public void changeStateButtonOnOff(){
		state = !state;
		
		if(state){
			textTitle = TXT_TITLE_ON;
			colorTitle = COLOR_GREEN;
			textBtnOnOff = BNT_TXT_OFF;
			colorBtnOnOff = COLOR_GREEN;
			colorBtnAcelerar = COLOR_GREEN;
		}
		else{
			textTitle = TXT_TITLE_OFF;
			colorTitle = COLOR_RED;
			textBtnOnOff = BNT_TXT_ON;
			colorBtnOnOff = COLOR_GREEN;
			colorBtnAcelerar = COLOR_RED;
		}
	}
	
	public void changeStateButtonAcelerar(){
		
		if (state) {
			textTitle = TXT_TITLE_ACELERANDO;
			colorTitle = COLOR_BLUE;
			textBtnOnOff = BNT_TXT_OFF;
			colorBtnOnOff = COLOR_GREEN;
			colorBtnAcelerar = COLOR_GREEN;
		}
	}
	
	public void listenerClicked(ActionEvent event){
		
		buttonID = event.getComponent().getId();
		
		if (buttonID != null){
			if (buttonID.equals(ID_BTN_ONOFF))
				changeStateButtonOnOff();
			else{
				if (buttonID.equals(ID_BTN_ACELERAR))
					changeStateButtonAcelerar();
			}
		}
			
	}
	
	public void setTextTitle(String textTitle){
		this.textTitle = textTitle;
	}
	
	public String getTextTitle(){
		return this.textTitle;
	}
	
	public void setColorTitle(String colorTitle){
		this.colorTitle = colorTitle;
	}
	
	public String getColorTitle(){
		return this.colorTitle;
	}
	
	public void setTextBtnOfOff(String textBtnOnOff){
		this.textBtnOnOff = textBtnOnOff;
	}
	
	public String getTextBtnOnOff(){
		return this.textBtnOnOff;
	}
	
	public void setColorBtnOnOff(String colorBtnOnOff){
		this.colorBtnOnOff = colorBtnOnOff;
	}
	
	public String getColorBtnOnOff(){
		return this.colorBtnOnOff;
	}
	
	public void setTextBtnAcelerar(String textBtnAcelerar){
		this.textBtnAcelerar = textBtnAcelerar;
	}
	
	public String getTextBtnAcelerar(){
		return this.textBtnAcelerar;
	}
	
	public void setColorBtnAcelerar(String colorBtnAcelerar){
		this.colorBtnAcelerar = colorBtnAcelerar;
	}
	
	public String getColorBtnAcelerar(){
		return this.colorBtnAcelerar;
	}

}
