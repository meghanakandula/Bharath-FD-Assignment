from rest_framework import generics
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get(self, request, *args, **kwargs):
        lang = request.GET.get('lang', 'en')  # Default to 'en' if no language is specified
        faqs = self.get_queryset()

        # Fetch translated content for each FAQ
        translated_faqs = []
        for faq in faqs:
            translation = faq.get_translation(lang)
            translated_faqs.append({
                'question': translation['question'],
                'answer': translation['answer'],
                'question_hi': faq.question_hi,
                'question_bn': faq.question_bn,
                'question_te': faq.question_te,
                'question_ta': faq.question_ta,
                'question_ml': faq.question_ml,
                'question_kn': faq.question_kn,
                'answer_hi': faq.answer_hi,
                'answer_bn': faq.answer_bn,
                'answer_te': faq.answer_te,
                'answer_ta': faq.answer_ta,
                'answer_ml': faq.answer_ml,
                'answer_kn': faq.answer_kn,
            })

        # Return the translated FAQs as a response
        return Response(translated_faqs)