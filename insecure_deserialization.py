# insecure_deserialization.py

import pickle

def deserialize_user_data(serialized_data):
    # Insecure deserialization
    user_data = pickle.loads(serialized_data)
    return user_data

if __name__ == "__main__":
    serialized_data = input("Enter serialized user data: ")
    user_data = deserialize_user_data(serialized_data)
    print(f"Deserialized user data: {user_data}")
