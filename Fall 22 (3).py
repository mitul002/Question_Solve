num_users = int(input("Enter the number of users: "))
users_dict = {}
for i in range(1, num_users + 1):  # Adjust the range to include the last user
    name = input(f"Enter name for user {i}: ")
    plan = input(f"Enter plan for user {i} (Basic/Standard/Premium): ")
    users_dict[i] = {"name": name, "plan": plan}

# Calculate payment amounts directly without using a separate function
for user_id, user_info in users_dict.items():

    if user_info["plan"] == "Basic":
        payment_amount = 9.99
    elif user_info["plan"] == "Standard":
        payment_amount = 15.99
    elif user_info["plan"] == "Premium":
        payment_amount = 19.99

    print(f"User {user_info['name']} with plan {plan} has to pay ${payment_amount:.2f}.")
