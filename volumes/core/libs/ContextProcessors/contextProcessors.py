# from B_Setting.models import Settings, Social
#
#
# def setting_context(request):
#     setting: Settings = Settings.objects.first()
#     return {
#         'setting': setting
#     }
#
#
# def social_context(request):
#     socials: Social = Social.objects.select_related('base_social').all()
#     return {
#         'socials': socials
#     }
