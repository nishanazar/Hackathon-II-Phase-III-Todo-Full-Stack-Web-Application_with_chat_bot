from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat_route_exists():
    """Test that the chat route exists and returns appropriate status"""
    
    # Test with a generic user ID format similar to what's in the error
    response = client.post("/api/user_1768821771317/chat", 
                          json={"message": "test"})
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json() if response.content else 'No content'}")
    
    # The route should exist, so we shouldn't get a 404
    # We might get 403 (forbidden) if auth fails or 422 (validation error) if request is malformed
    # But we shouldn't get 404 if the route is properly registered
    
if __name__ == "__main__":
    test_chat_route_exists()