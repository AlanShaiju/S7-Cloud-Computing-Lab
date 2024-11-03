import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        String serverAddress = "localhost"; // Use "localhost" if running on the same machine
        int port = 1234;

        try (Socket socket = new Socket(serverAddress, port)) {
            System.out.println("Connected to the server.");

            BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
            Scanner scanner = new Scanner(System.in);

            String message;
            while (true) {
                System.out.print("Enter message (type 'exit' to disconnect): ");
                message = scanner.nextLine();
                
                // Send message to the server
                output.println(message);
                
                // Exit if user types "exit"
                if (message.equalsIgnoreCase("exit")) {
                    System.out.println("Disconnected from the server.");
                    break;
                }

                // Read response from the server
                String response = input.readLine();
                System.out.println(response);
            }

            scanner.close();
        } catch (IOException e) {
            System.err.println("Client Error: " + e.getMessage());
        }
    }
}
