import ktrain

predictor = ktrain.load_predictor('./trained_models/topics_predictor_v3.2')


#['geodesy', 'geology', 'math', 'neftegas_texts']
def predict_text_class(text, return_probabilities=False):
    return predictor.predict(text, return_probabilities)
