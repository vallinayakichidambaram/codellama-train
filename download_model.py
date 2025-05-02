from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
login(token="my-token")
model_name = "codellama/CodeLlama-7b-Instruct-hf"
cache_dir = "./models"

tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir)