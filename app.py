# import necessary libraries
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect
import missiontomars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

db = mongo.db.mars_db
collection = db.mars_db
collection_image = db.mars_db
collection_weather = db.mars_db
collection_hemisphere = db.mars_db




# create route that renders index.html template
@app.route("/")
def home():
   

    News_dict= db.collection.find()

    featured_Image_dict = db.collection_image.find()

    mars_weather_dict = db.collection_weather.find()

    full_hemisphere_dict = db.collection_hemisphere.find()


    
    
    

    

    return render_template("index.html", News_dict = News_dict, 
                                        featured_Image_dict = featured_Image_dict,
                                        mars_weather_dict = mars_weather_dict,
                                        full_hemisphere_dict = full_hemisphere_dict)


@app.route("/scrape")
def scrape():
    

    db.collection.remove()
    News_dict = missiontomars.mars_news()
    db.collection.insert_one(News_dict)

    db.collection_image.remove()
    featured_Image_dict = missiontomars.featured_image()
    db.collection_image.insert_one(featured_Image_dict)

    db.collection_weather.remove()
    mars_weather_dict = missiontomars.Weather_tweet()
    db.collection_weather.insert_one(mars_weather_dict)


    db.collection_hemisphere.remove()
    full_hemisphere_dict = missiontomars.hemisphere_images()
    db.collection_hemisphere.insert_one(full_hemisphere_dict)

    



    print('----------------------------------------------------')
    print('----------------------------------------------------')
    print(News_dict)
    print('-----------------------------------------------------')
    print('-----------------------------------------------------')
    print(featured_Image_dict)
    print('-----------------------------------------------------')
    print('-----------------------------------------------------')
    print(mars_weather_dict)
    print('-----------------------------------------------------')
    print('-----------------------------------------------------')
    print(full_hemisphere_dict)
    
    return redirect("/", code=302)




if __name__ == "__main__":
    app.run(debug=True)