# Client

# Import socket module for network communication
# Import tkinter module for creating a graphical user interface
import socket
import tkinter as tk

# Function to send a request to the server
def send_request():
    inp = input_field.get()
    if inp.lower() == "over":
        client.send(inp.encode())
        client.close()
        root.quit()
    else:
        client.send(inp.encode())
        answer = client.recv(1024)
        answer_label.config(text="Answer is " + answer.decode())

# Function to clear the input field
def clear_input():
    input_field.delete(0, tk.END)

# Create the main tkinter window
root = tk.Tk()
root.title("Simple Calculator")

# Set the background color of the main window to black
root.configure(bg='black')

# Create a label for user instructions, set the background to black, and text color to light blue
input_label = tk.Label(root, text="Enter the operation (operand operator operand)", bg='black', fg='light blue')
input_label.pack()

# Create an input field for user input, set the background to black, and text color to light blue
input_field = tk.Entry(root, bg='black', fg='light blue')
input_field.pack()

# Create a "Submit" button, set the background to black, and text color to light blue
submit_button = tk.Button(root, text="Submit", command=send_request, bg='black', fg='light blue')
submit_button.pack()

# Create a "Clear" button, set the background to black, and text color to light blue
clear_button = tk.Button(root, text="Clear", command=clear_input, bg='black', fg='light blue')
clear_button.pack()

# Create a label to display the answer, set the background to black, and text color to light blue
answer_label = tk.Label(root, text="", bg='black', fg='light blue')
answer_label.pack()

# Define the server's address and port
SERVER = "127.0.0.1"
PORT = 8080

# Create a socket and connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

# Start the tkinter main event loop
root.mainloop()
