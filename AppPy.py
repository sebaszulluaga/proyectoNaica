import tkinter as tk
from tkinter import messagebox
import gspread
from datetime import datetime

# Google Sheets Authentication
gc = gspread.service_account(filename='C:\\Users\\jenni\\OneDrive\\Desktop\\Proyecto Naica\\driven-bison-437904-r7-dacf9bdd3b83.json')
spreadsheet_id = '1GeLCj1xG2gHbmfGl2VWsRbvD92NUxQpygDI-liTT6To'
db_sheet = gc.open_by_key(spreadsheet_id).get_worksheet(0)  # Sheet 1 (Database)
log_sheet = gc.open_by_key(spreadsheet_id).get_worksheet(1)  # Sheet 2 (Entry/Exit Logs)
laundry_sheet = gc.open_by_key(spreadsheet_id).get_worksheet(2)  # Sheet 3 (Laundry)

# Function to register entry or exit
def register_entry():
    cid = cid_entry.get()  # Get the text from the CID entry widget
    action = action_var.get()  # Get the selected radio button value

    if cid in db_sheet.col_values(1):  # Check if the CID exists
        row_index = db_sheet.col_values(1).index(cid) + 1
        name = db_sheet.cell(row_index, 2).value  # Name in column 2
        room = db_sheet.cell(row_index, 3).value  # Room in column 3

        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%Y-%m-%d")
        current_time = current_datetime.strftime("%H:%M:%S")

        log_sheet.append_row([cid, name, room, action, current_date, current_time])
        messagebox.showinfo("Success", "Record saved successfully.")
        cid_entry.delete(0, tk.END)  # Clear the CID entry field
    else:
        messagebox.showwarning("Invalid ID", "The entered CID is not found in the database.")

# Function to register laundry actions (pickup/drop-off)
def register_laundry():
    cid = cid_entry_laundry.get()
    action = laundry_var.get()  # Get the selected laundry action

    if cid in db_sheet.col_values(1):  # Check if the CID exists
        row_index = db_sheet.col_values(1).index(cid) + 1
        name = db_sheet.cell(row_index, 2).value  # Name in column 2
        room = db_sheet.cell(row_index, 3).value  # Room in column 3

        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%Y-%m-%d")
        current_time = current_datetime.strftime("%H:%M:%S")

        laundry_sheet.append_row([cid, name, room, action, current_date, current_time])
        messagebox.showinfo("Success", "Laundry action registered successfully.")
        cid_entry_laundry.delete(0, tk.END)  # Clear the CID entry field
    else:
        messagebox.showwarning("Invalid ID", "The entered CID is not found in the database.")

# Create the main window
root = tk.Tk()
root.title("Resident Entry and Laundry Registration")
root.geometry("410x600")

# --- Section 1: Entry/Exit Registration ---

# Label for Entry/Exit section
entry_section_label = tk.Label(root, text="Entry/Exit Registration", font=("Arial", 16, "bold"))
entry_section_label.pack(pady=10)

# Widgets for entering CID (Entry/Exit)
cid_label = tk.Label(root, text="Enter CID (Entry/Exit):", font=("Arial", 14))
cid_label.pack(pady=5)

cid_entry = tk.Entry(root, font=("Arial", 14))
cid_entry.pack(pady=5)

# Radio buttons for entry and exit actions
action_var = tk.StringVar(value="Entered")
entry_radio = tk.Radiobutton(root, text="Entered", variable=action_var, value="Entered", font=("Arial", 12))
entry_radio.pack(pady=5)
exit_radio = tk.Radiobutton(root, text="Exited", variable=action_var, value="Exited", font=("Arial", 12))
exit_radio.pack(pady=5)

# Button to trigger entry/exit registration
entry_button = tk.Button(root, text="Register Entry/Exit", font=("Arial", 14), command=register_entry)
entry_button.pack(pady=10)

# --- Section 2: Laundry Registration ---

# Label for Laundry section
laundry_section_label = tk.Label(root, text="Laundry Registration", font=("Arial", 16, "bold"))
laundry_section_label.pack(pady=20)

# Widgets for entering CID (Laundry)
cid_label_laundry = tk.Label(root, text="Enter CID (Laundry):", font=("Arial", 14))
cid_label_laundry.pack(pady=5)

cid_entry_laundry = tk.Entry(root, font=("Arial", 14))
cid_entry_laundry.pack(pady=5)

# Radio buttons for laundry actions
laundry_var = tk.StringVar(value="Pickup")
pickup_radio = tk.Radiobutton(root, text="Pickup Laundry", variable=laundry_var, value="Pickup", font=("Arial", 12))
pickup_radio.pack(pady=5)
dropoff_radio = tk.Radiobutton(root, text="Drop-off Laundry", variable=laundry_var, value="Dropoff", font=("Arial", 12))
dropoff_radio.pack(pady=5)

# Button to trigger laundry registration
laundry_button = tk.Button(root, text="Register Laundry", font=("Arial", 14), command=register_laundry)
laundry_button.pack(pady=10)

# Run the application
root.mainloop()
