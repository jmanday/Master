package com.jesusgarciamanday.playquestion;

/**
 * Created by jesusgarciamanday on 16/5/17.
 */

import javax.activation.DataHandler;
import javax.activation.DataSource;
import javax.activation.FileDataSource;
import javax.mail.BodyPart;
import javax.mail.Message;
import javax.mail.Multipart;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;

import java.io.File;
import java.util.Map;
import java.util.Properties;
import java.util.TreeMap;

public class Mail extends javax.mail.Authenticator{

    private final String fromEmail = "jmandaytest@gmail.com";
    private final String password = "07j10g83M";
    private String toEmail = "";
    private Properties props = null;
    private Session session = null;

    public enum ServerMail {
        GMAIL;

        public void setParams(Properties props){
            switch (this){
                case GMAIL:
                    props.setProperty("mail.transport.protocol", "smtp");
                    props.setProperty("mail.host", "smtp.gmail.com");
                    props.put("mail.smtp.auth", "true");
                    props.put("mail.smtp.port", "465");
                    props.put("mail.smtp.socketFactory.port", "465");
                    props.put("mail.smtp.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
                    props.put("mail.smtp.socketFactory.fallback", "false");
                    props.setProperty("mail.smtp.quitwait", "false");
                    break;
                default:
                    break;
            }
        }
    }

    public Mail(String toEmail, ServerMail serverMail){
        this.toEmail = toEmail;
        props = new Properties();
        serverMail.setParams(props);
        session = Session.getDefaultInstance(props, this);
    }


    protected PasswordAuthentication getPasswordAuthentication() {
        return new PasswordAuthentication(fromEmail, password);
    }


    public void send(TreeMap<String, byte[]> picturesTaken){
        try {

            // multipart to attach the image
            Multipart multipart = new MimeMultipart("SMS");
            for(Map.Entry<String,byte[]> entry : picturesTaken.entrySet()){
                BodyPart imagePart = new MimeBodyPart();
                String attachFile = entry.getKey();
                DataSource source = new FileDataSource(attachFile);
                imagePart.setDataHandler(new DataHandler(source));
                imagePart.setFileName(new File(attachFile).getName());
                multipart.addBodyPart(imagePart);
            }
            //picturesTaken.clear();

            // message to send via email
            final MimeMessage msg = new MimeMessage(Session.getDefaultInstance(props, Mail.this));
            msg.setFrom(new InternetAddress(fromEmail));
            msg.setRecipient(Message.RecipientType.TO,new InternetAddress(toEmail));
            msg.setSubject("Picture");
            msg.setContent(multipart);
            Transport.send(msg);

            for(Map.Entry<String,byte[]> entry : picturesTaken.entrySet()){
                File file = new File(entry.getKey());
                file.delete();
            }

            System.out.println("message sent successfully");

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

}
