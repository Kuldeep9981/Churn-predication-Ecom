import joblib

print("Loading model...")

# Load your existing model
model = joblib.load("random_forest_model.joblib")

print("Compressing model...")

# Save compressed version
joblib.dump(model, "model_compressed.pkl", compress=3)

print("✅ Compressed model saved as model_compressed.pkl")


