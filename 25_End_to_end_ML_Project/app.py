from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


# Create the Flask application
application = Flask(__name__)

# Create app alias
app = application


# Home page route
@app.route("/")
def index():
    return render_template("home.html")


# Prediction page route
@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():

    # Display the prediction form
    if request.method == "GET":
        return render_template("index.html")

    # Get user input from the form
    data = CustomData(
        gender=request.form.get("gender"),
        race_ethnicity=request.form.get("ethnicity"),
        parental_level_of_education=request.form.get(
            "parental_level_of_education"
        ),
        lunch=request.form.get("lunch"),
        test_preparation_course=request.form.get(
            "test_preparation_course"
        ),
        reading_score=float(
            request.form.get("reading_score")
        ),
        writing_score=float(
            request.form.get("writing_score")
        )
    )

    # Convert the input data into a DataFrame
    pred_df = data.get_data_as_data_frame()

    print("Prediction Input:")
    print(pred_df)

    # Create the prediction pipeline
    predict_pipeline = PredictPipeline()

    # Predict the student's math score
    results = predict_pipeline.predict(pred_df)

    # Display the prediction result on the same form page
    return render_template(
        "index.html",
        results=round(float(results[0]), 2)
    )


# Run the Flask application
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )