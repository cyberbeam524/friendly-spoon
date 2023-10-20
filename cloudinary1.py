# https://cloudinary.com/documentation/python_quickstart
# Set your Cloudinary credentials
# ==============================
# from dotenv import load_dotenv
# load_dotenv()

# Import the Cloudinary libraries
# ==============================
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Import to format the JSON responses
# ==============================
import json

# Set configuration parameter: return "https" URLs by setting secure=True  
# ==============================
config = cloudinary.config(secure=True)

import cloudinary
          
cloudinary.config( 
  cloud_name = "dfniun5i8", 
  api_key = "331112935958192", 
  api_secret = "LnSW0oFBM-VbBL-LKVIjbg6vUCM" 
)

# Log the configuration
# ==============================
print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")


def getAssetInfo(image_id):

  # Get and use details of the image
  # ==============================

  # Get image details and save it in the variable 'image_info'.
  image_info=cloudinary.api.resource(image_id)
  print("****3. Get and use details of the image****\nUpload response:\n", json.dumps(image_info,indent=2), "\n")

  # Assign tags to the uploaded image based on its width. Save the response to the update in the variable 'update_resp'.
  if image_info["width"]>900:
    update_resp=cloudinary.api.update("olympic_flag2", tags = "large")
  elif image_info["width"]>500:
    update_resp=cloudinary.api.update("olympic_flag2", tags = "medium")
  else:
    update_resp=cloudinary.api.update("olympic_flag2", tags = "small")

  # Log the new tag to the console.
  print("New tag: ", update_resp["tags"], "\n")
  return image_info




cloudinary.uploader.upload("https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg", 
  public_id = "olympic_flag2")

getAssetInfo("olympic_flag2")