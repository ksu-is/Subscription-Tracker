import datetime

class SubscriptionTracker:
    def __init__(self):
        self.subscriptions = {}

    def display_subscriptions(self):
        if not self.subscriptions:
            print("No subscriptions found.")
        else:
            print("Your Subscriptions:")
            for subscription, details in self.subscriptions.items():
                due_date, amount_due = details
                print(f"{subscription} - Due Date: {due_date}, Amount Due: ${amount_due:.2f}")

    def add_subscription(self, subscription, due_date, amount_due):
        self.subscriptions[subscription] = (due_date, amount_due)
        print(f"Subscription '{subscription}' added.")

    def edit_subscription(self, subscription, due_date, amount_due):
        if subscription in self.subscriptions:
            self.subscriptions[subscription] = (due_date, amount_due)
            print(f"Subscription '{subscription}' updated.")
        else:
            print("Subscription not found.")

def main():
    tracker = SubscriptionTracker()

    while True:
        print("\nSubscription Tracker Menu:")
        print("1. Display Subscriptions")
        print("2. Add Subscription")
        print("3. Edit Subscription")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            tracker.display_subscriptions()
        elif choice == "2":
            subscription = input("Enter the new subscription name: ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            amount_due = float(input("Enter the amount due: $"))
            tracker.add_subscription(subscription, due_date, amount_due)
        elif choice == "3":
            subscription = input("Enter the subscription name to edit: ")
            due_date = input("Enter the new due date (YYYY-MM-DD): ")
            amount_due = float(input("Enter the new amount due: $"))
            tracker.edit_subscription(subscription, due_date, amount_due)
        elif choice == "4":
            print("Exiting the Subscription Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
