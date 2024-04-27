from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.getcwd(), ".env"), override=True, verbose=True) 


from chat import app

if __name__ == "__main__":
    app.run()