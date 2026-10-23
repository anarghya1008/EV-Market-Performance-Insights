
import os
from flask import Flask, render_template

app = Flask(__name__)

TABLEAU_URL = os.environ.get(
    "TABLEAU_URL",
    "https://public.tableau.com/views/Project1_17926889567930/Dashboard2"
)

TABLEAU_PROFILE_URL = "https://public.tableau.com/app/profile/anarghya.jain4219"

PROJECT = {
    "title": "Electric Vehicle Market Performance & Insights",
    "author": "Anarghya Jain"
}

KPIS = [
    {"label": "EV models in dataset", "value": "199,999", "unit": ""},
    {"label": "Manufacturers in dataset", "value": "200", "unit": ""},
    {"label": "Average driving range", "value": "324.5", "unit": "km"},
    {"label": "Average customer rating", "value": "4.089", "unit": "/ 5"},
    {"label": "Average battery capacity", "value": "78.24", "unit": "kWh"},
]

OBJECTIVES = [
    "Understand EV categories, manufacturers and battery types.",
    "Explore customer ratings and annual sales.",
    "Compare price, battery capacity and driving range.",
    "Compare efficiency across EV categories.",
]

QUESTIONS = [
    "Which EV categories and manufacturers have the most models?",
    "How do customer ratings differ?",
    "How do annual sales change by model year?",
    "Does a higher price relate to a longer driving range?",
    "Does battery capacity relate to driving range?",
    "Which categories are the most efficient?",
]

GUIDE = [
    ("EV category distribution", "Distribution of models across categories."),
    ("Manufacturer model counts", "Models listed for each manufacturer."),
    ("Customer ratings", "Ratings across models and manufacturers."),
    ("Annual sales", "Sales grouped by model year."),
    ("Battery types", "Distribution of battery types."),
    ("Manufacturing countries", "Countries represented in the dataset."),
    ("Price vs. range", "Price compared with driving range."),
    ("Battery vs. range", "Battery capacity compared with driving range."),
    ("Efficiency", "Efficiency comparison by category."),
]

TECH_STACK = [
    ("Tableau Public", "Interactive dashboard"),
    ("Tableau Embedding API v3", "Dashboard embedding"),
    ("Python and Flask", "Web server"),
    ("HTML, CSS, JavaScript", "Website design and interactions"),
]

LIMITATIONS = [
    "Dataset counts are not verified real-world market totals.",
    "Correlation does not prove causation.",
    "Averages may hide differences between categories.",
    "Summary values should be verified against the source dataset.",
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        project=PROJECT,
        kpis=KPIS,
        objectives=OBJECTIVES,
        questions=QUESTIONS,
        guide=GUIDE,
        tech_stack=TECH_STACK,
        limitations=LIMITATIONS,
        tableau_url=TABLEAU_URL,
        profile_url=TABLEAU_PROFILE_URL,
    )


@app.errorhandler(404)
def not_found(error):
    return "<h1>Page not found</h1><a href='/'>Back home</a>", 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)