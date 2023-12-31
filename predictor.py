from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from model import AnswerPredictor


MODEL_PATH = "./trained_models"
model = AutoModelForQuestionAnswering.from_pretrained(MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

predictor = AnswerPredictor(model, tokenizer, device='cpu', n_best=10, no_answer=True)
