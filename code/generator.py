from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class Generator:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "google/flan-t5-base",
            use_fast=False
        )
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            "google/flan-t5-base"
        )
        self.model.eval()

    def generate(self, context, question):
        if not context.strip():
            return "संदर्भः न लभ्यते। कृपया अन्यं प्रश्नं पृच्छतु।"

        prompt = (
            "You are a Sanskrit scholar.\n"
            "Answer the question strictly using the context.\n\n"
            f"Context:\n{context}\n\n"
            f"Question:\n{question}\n\n"
            "Answer in clear Sanskrit sentences:"
        )

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        with torch.no_grad():
            output_ids = self.model.generate(
                **inputs,
                max_new_tokens=120,
                num_beams=4,
                do_sample=False
            )

        answer = self.tokenizer.decode(
            output_ids[0],
            skip_special_tokens=True
        )

        return answer.strip()
