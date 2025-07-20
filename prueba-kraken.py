import json # Used for pretty-printing the JSON response
import kraken

# Example 3: Creating a client with all parameters
print("\n--- Example 3: Creating client with all parameters ---")
response3 = kraken.crear_cliente_stripe(
    email="test_user_003@example.com",
    firebase_user="firebase_id_xyz",
    site="myawesomeapp.com"
)
print("\nAPI Response 3:")
print(json.dumps(response3, indent=2))