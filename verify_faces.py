from deepface import DeepFace
import os

def verify_faces(profile_path, gov_id_path):
    """
    Verifies if the face in the profile picture matches the one in the government ID.
    """
    try:
        result = DeepFace.verify(img1_path=profile_path, img2_path=gov_id_path)
        return result['verified'], result['distance']
    except Exception as e:
        print(f"Error during verification: {e}")
        return False, None

if __name__ == "__main__":
    # Example usage
    profile_img = "./static/uploads/profile_picture.jpg"
    gov_id_img = "./static/uploads/gov_id.jpg"

    is_verified, distance = verify_faces(profile_img, gov_id_img)
    print(f"Verified: {is_verified}, Distance: {distance}")
