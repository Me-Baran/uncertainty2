from model import model

# Calculate predictions
predictions = model.predict_proba({
    "train": "delayed",
    "rain": "heavy"
})

# Print predictions for each node
for node, prediction in zip(model.states, predictions):
    print(f"\nNode: {node.name}")
    
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        if hasattr(prediction, "parameters"):
            for param in prediction.parameters[0]:
                print(f"{param}: {prediction.parameters[0][param]: 0.4f}")