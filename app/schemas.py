from supabase import create_client, Client

def create_tables(supabase: Client):
    # Users table
    supabase.table("users").create(
        {
            "email": "text unique",
            "password": "text",
            "full_name": "text",
            "phone": "text",
            "created_at": "timestamp default now()"
        }
    ).execute()

    # Rides table
    supabase.table("rides").create(
        {
            "user_id": "text",
            "driver_id": "text",
            "pickup_lat": "float8",
            "pickup_lng": "float8",
            "destination_lat": "float8",
            "destination_lng": "float8",
            "status": "text",  # requested, accepted, completed, cancelled
            "created_at": "timestamp default now()"
        }
    ).execute()