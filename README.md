
<h1 align="center">🛒 FreshMart Inventory Management System</h1>

<p align="center">
  <b>A simple yet powerful desktop inventory manager built with Python, Tkinter, and JSON storage.</b><br>
  <i>Helps small grocery stores like FreshMart easily track, update, and manage stock levels.</i>
</p>

<hr>

📦 Overview
<br>
FreshMart Inventory Management System is a lightweight desktop application designed to manage stock items in small retail or grocery shops.
<br><br>
✅ Features include
- Add new inventory items with expiry date.<br>
- View all items in a user-friendly table.<br>
- Update stock quantity easily.<br>
- Delete outdated or unwanted items.<br>
- Alerts for low stock items (quantity below 10).<br>

<hr>

🚀 How to Run

<ol>
  <li>Make sure you have <code>Python 3</code> installed on your system.</li>
  <li>Install required libraries:
    <pre>pip install tkcalendar</pre>
  </li>
  <li>Clone this repository or download the code files.</li>
  <li>Run the script:
    <pre>python inventory_app.py</pre>
  </li>
</ol>

✨ That's it! The application window should now appear.

<hr>

🛠️ Key Components & How It Works

<ul>
  <li><b>GUI:</b> Built with <code>Tkinter</code> and <code>ttk</code> widgets for modern look.</li>
  <li><b>Data Storage:</b> Uses a local JSON file (<code>inventory.json</code>) to store inventory data persistently.</li>
  <li><b>Date Picker:</b> Integrates <code>tkcalendar.DateEntry</code> for selecting expiry dates easily.</li>
  <li><b>Low Stock Alerts:</b> Automatically notifies user about items running low on stock when the app starts.</li>
</ul>

<hr>

🧩 File Structure
<br>
inventory_app.py     # Main Python script containing the entire application
<br>
inventory.json       # JSON file to store inventory data (created after first run)
<br>
README.md            # Project documentation (this file)

<hr>
✏️ How to Contribute
If you'd like to improve this project or add new features:

Fork the repository.

Make your changes.

Submit a pull request!

<hr>
🧡 Author
Developed by Sweta Kumari
If you find this helpful, leave a ⭐ or share it with others!
