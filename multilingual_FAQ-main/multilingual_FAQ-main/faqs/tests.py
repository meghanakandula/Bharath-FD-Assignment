import pytest
from .models import FAQ

@pytest.mark.django_db
def test_faq_translation():
    # Create a FAQ with English question and answer
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
    )
    
    # Save to trigger translation
    faq.save()

    # Assert that translation fields are populated
    assert faq.question_hi is not None
    assert faq.question_bn is not None
    assert faq.question_te is not None
    assert faq.question_ta is not None
    assert faq.question_ml is not None
    assert faq.question_kn is not None

    assert faq.answer_hi is not None
    assert faq.answer_bn is not None
    assert faq.answer_te is not None
    assert faq.answer_ta is not None
    assert faq.answer_ml is not None
    assert faq.answer_kn is not None
    
    # Optionally, assert that translations are different from the original question/answer
    assert faq.question_hi != faq.question
    assert faq.answer_hi != faq.answer
    assert faq.question_bn != faq.question
    assert faq.answer_bn != faq.answer
    # Repeat for other languages