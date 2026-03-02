# Hackathon Project - Main Application
# Modified by PERSON2 - Added Logout Feature

def calculate_score(points):
    """Calculate user score"""
    return points * 10

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
    print("Version: 1.0 + Person2 Logout")
    print("Status: Ready for modifications")
    print()
    
    # PERSON2's addition - Logout feature
    logout("person2")
    
    display_menu()
    score = calculate_score(5)
    print(f"\nSample Score: {score} points")

if __name__ == "__main__":
    main()
