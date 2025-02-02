from django.db import models
from ckeditor.fields import RichTextField
from translate import Translator  # Import translate package
from django.utils.html import strip_tags

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Translation fields for different languages
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    question_te = models.TextField(blank=True, null=True)
    question_ta = models.TextField(blank=True, null=True)
    question_ml = models.TextField(blank=True, null=True)
    question_kn = models.TextField(blank=True, null=True)
    
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)
    answer_te = RichTextField(blank=True, null=True)
    answer_ta = RichTextField(blank=True, null=True)
    answer_ml = RichTextField(blank=True, null=True)
    answer_kn = RichTextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update when modified

    def get_translation(self, lang):
        """
        Returns the translated question and answer, or falls back to English if not available.
        """
        # Dynamically check for the translated field or default to English (question/answer)
        question_field = f'question_{lang}' if hasattr(self, f'question_{lang}') else 'question'
        answer_field = f'answer_{lang}' if hasattr(self, f'answer_{lang}') else 'answer'
        
        return {
            "question": getattr(self, question_field, self.question),
            "answer": getattr(self, answer_field, self.answer),
        }

    def save(self, *args, **kwargs):
        """
        Translate question and answer to other languages when saving.
        Uses the offline translate package for translation.
        """
        # Define translators for each language
        translators = {
            'hi': Translator(to_lang="hi"),
            'bn': Translator(to_lang="bn"),
            'te': Translator(to_lang="te"),
            'ta': Translator(to_lang="ta"),
            'ml': Translator(to_lang="ml"),
            'kn': Translator(to_lang="kn"),
        }
        
        try:
            # Translate the question and answer for each language if fields are not filled
            for lang, translator in translators.items():
                # Translate only if the translation field is empty
                if not getattr(self, f'question_{lang}'):
                    setattr(self, f'question_{lang}', translator.translate(self.question))
                if not getattr(self, f'answer_{lang}'):
                    setattr(self, f'answer_{lang}', translator.translate(self.answer))

            # Strip HTML tags after translation to keep content clean
            self.question = strip_tags(self.question)
            self.answer = strip_tags(self.answer)
            for lang in translators.keys():
                setattr(self, f'question_{lang}', strip_tags(getattr(self, f'question_{lang}')))
                setattr(self, f'answer_{lang}', strip_tags(getattr(self, f'answer_{lang}')))
            
        except Exception as e:
            # Log the error or raise a validation error depending on your preference
            print(f"Translation error: {e}")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question