import java.io.*;
import java.net.*;
public class server3and5
{
public static int cameraBaseDegree = 150;
  public static void main(String[] args) throws Exception
  {
      
	Socket sock = new Socket ("192.168.86.30", 3000);
Runtime.getRuntime().exec("sudo python /home/pi/halt2.py");
Runtime.getRuntime().exec("sudo service motion start");
      //Socket sock = sersock.accept( );                          
                              // reading from keyboard (keyRead object)
      BufferedReader keyRead = new BufferedReader(new InputStreamReader(System.in));
	                      // sending to client (pwrite object)
      OutputStream ostream = sock.getOutputStream(); 
      PrintWriter pwrite = new PrintWriter(ostream, true);
 
                              // receiving from server ( receiveRead  object)
      InputStream istream = sock.getInputStream();
      BufferedReader receiveRead = new BufferedReader(new InputStreamReader(istream));
 
      String receiveMessage, sendMessage,  receiveMessage2;      
         receiveMessage2 = " ";
      while(true)
      {
        if ((receiveMessage = receiveRead.readLine()) != null)  
        {
       if(receiveMessage.equalsIgnoreCase(receiveMessage2)&& (!((receiveMessage.indexOf("voice") >=0 || receiveMessage.indexOf("small") >= 0)))){
}    
else {

Runtime.getRuntime().exec(receiveMessage);
receiveMessage2 = receiveMessage; receiveMessage = " ";}


 

        }         
    
        pwrite.println("A");             
        pwrite.flush();
      }               
    }                    
}       