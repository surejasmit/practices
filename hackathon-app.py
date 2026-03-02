# Hackathon Project - Main Application
# GDG Sprintathon Demo

def calculate_score(points):
    """Calculate user score"""
    return points * 10

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
    print("Version: 1.0")
    print("Status: Ready for modifications")
    print()
    display_menu()
    
    # Test score calculation
    score = calculate_score(5)
    print(f"\nSample Score: {score} points")

if __name__ == "__main__":
    main()
