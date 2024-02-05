# TELEGRAM BOT FOR INCOME AND EXPENSE TRACKING

This Telegram bot helps users manage their finances efficiently. It includes the following features:

- Add expenses with category specifications.
- Predefined expense categories are hardcoded.
- View available expense categories.
- Add income with income category specification.
- View all expenses, monthly expenses, and weekly expenses.
- Delete expenses or income entries.
- Display income and expense statistics by category for the day, month, week, and year.

## Installation and Setup


1. **Clone the repository:**
    ```bash
    git clone [repository URL]
    cd Telegram_bot
    ```

2. **Create a .env file in the same directory as your script and add your Telegram bot token:**
    ```TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN```

3. **Set up a Virtual Environment:**
    - Before installing the project dependencies, it's recommended to create a virtual environment:
      ```bash
      python -m venv myenv
      source myenv/bin/activate  # On Windows, use: myenv\Scripts\activate
      ```

4. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run your script:**
   ```python your_script_name.py```
