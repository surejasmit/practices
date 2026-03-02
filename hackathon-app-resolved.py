# Hackathon Project - Main Application
# ✅ RESOLVED: Both Person1 and Person2 features combined

def calculate_score(points):
    """Calculate user score"""
    return points * 10

def login(username, password):
    """PERSON1: Login feature"""
    print("\n🔐 LOGIN FEATURE (by Person1)")
    print(f"Username: {username}")
    print(f"Password: {'*' * len(password)}")
    print("✅ Login successful!")
    return True

def logout(username):
    """PERSON2: Logout feature"""
    print("\n🚪 LOGOUT FEATURE (by Person2)")
    print(f"User: {username}")
    print("✅ Logged out successfully!")
    print("Session ended.")
    return True

def display_menu():
    """Display main menu"""
    print("="*40)
    print("   HACKATHON PROJECT MENU")
    print("="*40)
    print("1. Start Challenge")
    print("2. View Leaderboard")
    print("3. Exit")
    print("="*40)

def main():
    print("Welcome to Hackathon Project!")
    print("Version: 2.0 - CONFLICT RESOLVED")
    print("Features: Login (Person1) + Logout (Person2)")
    print("Status: Both features working together!")
    print()
    
    # BOTH features working together
    login("testuser", "pass123")  # Person1's feature
    
    display_menu()
    score = calculate_score(5)
    print(f"\nSample Score: {score} points")
    
    logout("testuser")  # Person2's feature

if __name__ == "__main__":
    main()
