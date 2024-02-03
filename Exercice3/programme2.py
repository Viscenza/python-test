import sqlite3

def find_missing_number(tab):
    x = min(tab)
    y = max(tab)
    
    expected_sum = (x + y) * (y - x + 1) // 2
    real_sum = sum(tab)
    
    missing_number = expected_sum - real_sum
    
    # Stocker le nombre manquant dans une table SQLite
    connection = sqlite3.connect('database2.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS missing_number (nombre INTEGER)")
    cursor.execute("INSERT INTO missing_number VALUES (?)", (missing_number,))
    connection.commit()
    connection.close()
    
    return missing_number

# Exemple d'utilisation
exemple = [1, 2, 3, 5, 6, 7, 8]
resultat = find_missing_number(exemple)
print(f"Le nombre manquant est : {resultat}")
