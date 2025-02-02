from django.contrib import admin
from .models import FAQ

# Check if FAQ has already been registered
if not admin.site.is_registered(FAQ):
    @admin.register(FAQ)
    class FAQAdmin(admin.ModelAdmin):
        list_display = (
            'question', 'answer',
            'get_hindi_faq', 'get_bengali_faq', 'get_telugu_faq',
            'get_tamil_faq', 'get_malayalam_faq', 'get_kannada_faq',
            'created_at', 'updated_at'
        )

        search_fields = (
            'question', 'question_hi', 'question_bn', 'question_te', 'question_ta', 'question_ml', 'question_kn',
            'answer', 'answer_hi', 'answer_bn', 'answer_te', 'answer_ta', 'answer_ml', 'answer_kn'
        )

        fieldsets = (
            ('Default (English)', {
                'fields': ('question', 'answer'),
            }),
            ('Hindi', {
                'fields': ('question_hi', 'answer_hi'),
            }),
            ('Bengali', {
                'fields': ('question_bn', 'answer_bn'),
            }),
            ('Telugu', {
                'fields': ('question_te', 'answer_te'),
            }),
            ('Tamil', {
                'fields': ('question_ta', 'answer_ta'),
            }),
            ('Malayalam', {
                'fields': ('question_ml', 'answer_ml'),
            }),
            ('Kannada', {
                'fields': ('question_kn', 'answer_kn'),
            }),
            ('Metadata', {
                'fields': ('updated_at',),  # Only include editable fields
            }),
        )

        readonly_fields = ('created_at', 'updated_at')  # Mark these fields as readonly

        def get_hindi_faq(self, obj):
            return f"Q: {obj.question_hi} | A: {obj.answer_hi}"
        get_hindi_faq.short_description = 'Hindi FAQ'

        def get_bengali_faq(self, obj):
            return f"Q: {obj.question_bn} | A: {obj.answer_bn}"
        get_bengali_faq.short_description = 'Bengali FAQ'

        def get_telugu_faq(self, obj):
            return f"Q: {obj.question_te} | A: {obj.answer_te}"
        get_telugu_faq.short_description = 'Telugu FAQ'

        def get_tamil_faq(self, obj):
            return f"Q: {obj.question_ta} | A: {obj.answer_ta}"
        get_tamil_faq.short_description = 'Tamil FAQ'

        def get_malayalam_faq(self, obj):
            return f"Q: {obj.question_ml} | A: {obj.answer_ml}"
        get_malayalam_faq.short_description = 'Malayalam FAQ'

        def get_kannada_faq(self, obj):
            return f"Q: {obj.question_kn} | A: {obj.answer_kn}"
        get_kannada_faq.short_description = 'Kannada FAQ'