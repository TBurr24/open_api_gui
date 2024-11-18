import os
from tkinter import Tk, Label, Entry, Text, Button, END
from dotenv import load_dotenv
import openai

# Load API key from .env file
load_dotenv()
api_key = os.getenv('OPEN_API_KEY')
if not api_key:
    raise ValueError("Please add your OpenAI API key to the .env file.")

# Initialize OpenAI API
openai.api_key = api_key

# Function to handle submission and fetch completion
def get_completion():
    prompt = input_box.get("1.0", END).strip()
    if not prompt:
        output_box.delete("1.0", END)
        output_box.insert(END, "Please enter a prompt.")
        return
    
    try:
        # Call OpenAI API for completion
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        completion = response.choices[0].text.strip()
    except Exception as e:
        completion = f"Error: {e}"

    # Display the completion in the output box
    output_box.delete("1.0", END)
    output_box.insert(END, completion)

# Create the GUI
root = Tk()
root.title("OpenAI Prompt Completer")

# Input Label and Text Box
Label(root, text="Enter your prompt:").pack(pady=5)
input_box = Text(root, height=10, width=50)
input_box.pack(pady=5)

# Submit Button
submit_button = Button(root, text="Submit", command=get_completion)
submit_button.pack(pady=5)

# Output Label and Text Box
Label(root, text="Output:").pack(pady=5)
output_box = Text(root, height=10, width=50)
output_box.pack(pady=5)

# Run the application
root.mainloop()
