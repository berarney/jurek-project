def individual_serial(edu) -> dict:
    return{
        "full_name": str(edu["full_name"]),
        "email": edu["email"],
        "password": str(edu["password"])
    }

def list_serial(edus) -> list:
    return [individual_serial(edu) for edu in edus]