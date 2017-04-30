import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
/**
 * @author Arpit Mandliya
 */
public class HttpURLConnectionExample {
 
 private final String USER_AGENT = "Mozilla/5.0";
 
 public static void main(String[] args) throws Exception {
 
  HttpURLConnectionExample http = new HttpURLConnectionExample();
 
     // Sending get request
  http.sendingGetRequest();
  
    // Sending post request
  http.sendingPostRequest();
 
 }
 
 // HTTP GET request
 private void sendingGetRequest() throws Exception {
 
  String urlString = "http://52.49.91.111:8443/";
  
  URL url = new URL(urlString);
  HttpURLConnection con = (HttpURLConnection) url.openConnection();
 
  // By default it is GET request
  con.setRequestMethod("GET");
 
  //add request header
  con.setRequestProperty("User-Agent", USER_AGENT);
  int responseCode = 0;
  try{
      responseCode = con.getResponseCode();
    }catch(Exception e){}
  System.out.println("Sending get request : "+ url);
  System.out.println("Response code : "+ responseCode);
 
  // Reading response from input Stream
  BufferedReader in = new BufferedReader(
          new InputStreamReader(con.getInputStream()));
  String output;
  StringBuffer response = new StringBuffer();
 
  while ((output = in.readLine()) != null) {
   response.append(output);
  }
  in.close();
 
  //printing result from response
  System.out.println(response.toString());
 
 }
 
 // HTTP Post request
 private void sendingPostRequest() throws Exception {
 
  String url = "http://localhost:8080/JAXRSJsonCRUDExample/rest/countries";
  URL obj = new URL(url);
  HttpURLConnection con = (HttpURLConnection) obj.openConnection();
 
        // Setting basic post request
  con.setRequestMethod("POST");
  con.setRequestProperty("User-Agent", USER_AGENT);
  con.setRequestProperty("Accept-Language", "en-US,en;q=0.5");
  con.setRequestProperty("Content-Type","application/json");
 
  String postJsonData = "";
  
  // Send post request
  con.setDoOutput(true);
  DataOutputStream wr = new DataOutputStream(con.getOutputStream());
  wr.writeBytes(postJsonData);
  wr.flush();
  wr.close();
 
  int responseCode = con.getResponseCode();
  System.out.println("nSending 'POST' request to URL : " + url);
  System.out.println("Post Data : " + postJsonData);
  System.out.println("Response Code : " + responseCode);
 
  BufferedReader in = new BufferedReader(
          new InputStreamReader(con.getInputStream()));
  String output;
  StringBuffer response = new StringBuffer();
 
  while ((output = in.readLine()) != null) {
   response.append(output);
  }
  in.close();
  
  //printing result from response
  System.out.println(response.toString());
 }
}