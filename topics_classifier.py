import ktrain

predictor = ktrain.load_predictor('./trained_models/topics_predictor_v3.2')

predictable_topics = ['Computer Science' , 'Physics', 'Mathematics', 'Statistics', 'Quantitative Biology', 'Quantitative Finance', 'Geodesy', 'Geology', 'Neftegas']


#['Computer Science' , 'Physics', 'Mathematics', 'Statistics', 'Quantitative Biology', 'Quantitative Finance', 'Geodesy', 'Geology', 'Neftegas']
def predict_text_class(text, return_probabilities=False):
    return predictor.predict(text, return_probabilities)

def prepare_prediction_response(text):
    '''возвращает dict с угаданной темой и её шансом'''

    predictions = predict_text_class(text, return_probabilities=True)
    topic = predictable_topics[predictions.argmax()]
    return {'predicted_topic': topic, 'value': predictions[predictions.argmax()].item()}
