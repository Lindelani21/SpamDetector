import tkinter as tk
from tkinter import scrolledtext
import re

INITIAL_SPAM_KEYWORDS = {
    "free": 2,
    "win": 2,
    "prize": 2,
    "click here": 3,
    "limited time": 3,
    "congratulations": 2,
    "refinance": 1,
    "password": 1,
    "urgent": 2,
    "act now": 2,
    "exclusive offer": 3,
    "cash bonus": 2,
    "risk-free": 2,
    "guaranteed": 2,
    "call now": 2,
    "earn money": 2,
    "extra income": 2,
    "no fees": 1,
    "no credit check": 1,
    "money back": 1,
    "save big": 1,
    "lowest price": 1,
    "discount": 1,
    "credit card": 1,
    "insurance": 1,
    "investment": 1,
    "opportunity": 1,
    "get rich quick": 3,
    "lose weight": 2,
    "cash": 1,
    "check or money order": 1,
    "call": 1,
    "click": 4,
    "instant": 1,
    "quick": 1,
    "fast": 1,
}

INITIAL_NON_KEYWORDS = {
    "thank you": 2,
    "meeting": 2,
    "attachment": 2,
    "draft": 2,
    "review": 2,
    "hi": 1,
    "team": 5,
    "discuss": 1,
    "proposal": 1,
    "tomorrow": 1,
    "deadline": 1,
    "presentation": 1,
    "feedback": 1,
    "questions": 1,
    "update": 1,
    "schedule": 1,
    "report": 1,
    "invoice": 1,
    "lunch": 1,
    "coffee": 1,
    "kind regards": 5,
    "best regards": 5,
    "sincerely": 5,
    "cheers": 5,
    "good day": 5,
    "kindly": 2,
    "workshop": 1,
    "conference": 1,
    "seminar": 1,
    "webinar": 1,
    "would like to": 1,
    "please let me know": 3,
    "attached file": 3,
    "looking forward": 3,
    "follow up": 3,
    "reminder": 3,
    "agenda": 3,
    "minutes": 3,
    "action items": 3,
}


SPAM_SYMBOLS = [
    (r'!{2,}', 1),  # Multiple exclamation marks
    (r'\?{2,}', 1),  # Multiple question marks
    (r'\$\d+', 1),  # Dollar amounts
    (r'\d{3}-\d{3}-\d{4}', 1),  # Phone numbers
    (r'\d+%', 1),  # Percentages
    (r'http[s]?://\S+', 2),  # URLs
    (r'www\.\S+', 2),  # URLs
    (r'[A-Z]{5,}', 1),  # All caps words
    (r'\b[A-Z]{2,}\b', 1),  # All caps words
    (r'\b[A-Z]\b', 1),  # Single all caps letters
    (r'!', 1),  # Exclamation marks
    (r'\?', 1),  # Question marks
    (r'http[s]?://\S+', 3),  # URLs
    (r'bit\.ly|tinyurl\.com', 3),  # Shortened URLs
    (r'[A-Z]{3,}', 2),  # Excessive uppercase letters
]

def classify_email(email_content):
    
    email_content = email_content.lower()

    # Initialize scores
    spam_score = 0
    ham_score = 0

    # Calculate spam score
    for keyword, weight in INITIAL_SPAM_KEYWORDS.items():
        if keyword in email_content:
            spam_score += weight

    # Calculate none score
    for keyword, weight in INITIAL_NON_KEYWORDS.items():
        if keyword in email_content:
            ham_score += weight

    # Check for spam symbols using regex
    for pattern, weight in SPAM_SYMBOLS:
        if re.search(pattern, email_content):
            spam_score += weight

    # Classify based on the higher score
    if spam_score + 0.5 > ham_score:
        return "spam"
    else:
        return "notspam"

# GUI Application
class SpamDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spam Email Detector")
        self.root.geometry("1000x5500")

        # Title Label
        self.title_label = tk.Label(root, text="Spam Email Detector", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Text Area for Email Input
        self.email_input = scrolledtext.ScrolledText(root, width=100, height=40, wrap=tk.WORD)
        self.email_input.pack(padx=10, pady=10)

        # Classify Button
        self.classify_button = tk.Button(root, text="Classify Email", command=self.classify_and_display, font=("Arial", 12))
        self.classify_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="Classification: ", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def classify_and_display(self):
        email_content = self.email_input.get("1.0", tk.END).strip()
        if email_content:
            classification = classify_email(email_content)
            self.result_label.config(text=f"Classification: {classification}")
        else:
            self.result_label.config(text="Please enter some email content.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpamDetectorApp(root)
    root.mainloop()
