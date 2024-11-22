import java.net.URI;
import java.net.http.*;
import java.io.*;

public class RestApi {
    public static void main(String[] args) throws IOException, InterruptedException {

        HttpRequest request = HttpRequest.newBuilder()
                .uri(new URI.create("https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={API_KEY}"))
                .header("Authorization", "Bearer {API_KEY}")
                .GET()
                .build();
    }
}