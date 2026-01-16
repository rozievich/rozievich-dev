from django.contrib import admin
from django.utils.html import format_html
from dateutil.relativedelta import relativedelta

from .models import Skill, Experience, Portfolio, Message

# Skill Admin
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience_count', 'portfolio_count')
    list_display_links = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

    def experience_count(self, obj):
        return obj.experiences.count()
    experience_count.short_description = "Tajribalarda ishlatilgan"

    def portfolio_count(self, obj):
        return obj.portfolio_items.count()
    portfolio_count.short_description = "Portfolio loyihalarida ishlatilgan"

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Statistika (o‘qish uchun)', {
            'classes': ('collapse',),
            'fields': ()
        }),
    )


# Experience Admin
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'position',
        'start_date',
        'end_date',
        'duration',
        'skills_list',
        'company_link'
    )
    list_display_links = ('company_name', 'position')
    list_filter = ('start_date', 'end_date')
    search_fields = ('company_name', 'position', 'description')
    ordering = ('-start_date',)
    filter_horizontal = ('skills',)

    def skills_list(self, obj):
        """Skill'larni chiroyli ko'rsatish"""
        if obj.skills.exists():
            return ", ".join([skill.name for skill in obj.skills.all()[:5]])
        return "—"
    skills_list.short_description = "Asosiy ko‘nikmalar"

    def company_link(self, obj):
        """Company URL bor bo'lsa link chiqarish"""
        if obj.company_url:
            return format_html(
                '<a href="{}" target="_blank" rel="noopener">🔗</a>',
                obj.company_url
            )
        return "—"
    company_link.short_description = "Sayt"

    def duration(self, obj):
        """Ish davomiyligini chiroyli ko'rsatish"""
        if not obj.end_date:
            return "Hozirda"
        delta = relativedelta(obj.end_date, obj.start_date)
        parts = []
        if delta.years:
            parts.append(f"{delta.years} yil")
        if delta.months:
            parts.append(f"{delta.months} oy")
        return " ".join(parts) or "1 oy"
    duration.short_description = "Davomiylik"

    # Fieldsetlar — tartib va guruhlash
    fieldsets = (
        ('Asosiy ma’lumotlar', {
            'fields': (
                ('company_name', 'company_url'),
                ('position',),
                ('start_date', 'end_date'),
            )
        }),
        ('Tavsif va ko‘nikmalar', {
            'fields': ('description', 'skills'),
        }),
    )

    # Qo'shimcha optimallashtirish
    readonly_fields = ('duration',)  # faqat ko'rish uchun (admin o'zgartira olmaydi)


# ======================
# Portfolio Admin
# ======================
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'thumbnail',
        'tech_skills_list',
        'is_future',
        'project_link',
        'github_link',
        'created_at'
    )
    list_display_links = ('title',)
    list_filter = ('is_future', 'tech_skills')
    search_fields = ('title', 'description')
    ordering = ('-is_future', 'title')
    filter_horizontal = ('tech_skills',)
    date_hierarchy = 'created_at'  # sana bo'yicha navigatsiya

    # Rasmni kichik ko'rinishda chiqarish
    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 60px; border-radius: 4px;" />',
                obj.image.url
            )
        return "—"
    thumbnail.short_description = "Rasm"

    def tech_skills_list(self, obj):
        skills = obj.tech_skills.all()[:6]
        if skills:
            return ", ".join([s.name for s in skills]) + ("..." if obj.tech_skills.count() > 6 else "")
        return "—"
    tech_skills_list.short_description = "Texnologiyalar"

    def project_link(self, obj):
        if obj.project_url:
            return format_html(
                '<a href="{}" target="_blank">🌐</a>',
                obj.project_url
            )
        return "—"
    project_link.short_description = "Loyiha"

    def github_link(self, obj):
        if obj.github_url:
            return format_html(
                '<a href="{}" target="_blank">🐙</a>',
                obj.github_url
            )
        return "—"
    github_link.short_description = "GitHub"

    # Qo'shimcha maydonlar
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 400px; border: 1px solid #ddd; border-radius: 8px;" />',
                obj.image.url
            )
        return "Rasm yuklanmagan"
    thumbnail_preview.short_description = "Rasm (katta ko'rinish)"

    fieldsets = (
        ('Asosiy ma’lumotlar', {
            'fields': (
                ('title', 'is_future'),
                ('image', 'thumbnail_preview'),
                ('project_url', 'github_url'),
            )
        }),
        ('Tavsif va texnologiyalar', {
            'fields': ('description', 'tech_skills'),
        }),
    )


# ======================
# Message Admin
# ======================
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email_link',
        'subject',
        'is_read_badge',
        'sent_at',
    )
    list_display_links = ('subject',)
    list_filter = ('is_read', 'sent_at')
    search_fields = ('name', 'email', 'subject', 'body')
    date_hierarchy = 'sent_at'
    ordering = ('-sent_at',)

    # Qo'shimcha chiroyli maydonlar
    def email_link(self, obj):
        return format_html(
            '<a href="mailto:{}">{}</a>',
            obj.email, obj.email
        )
    email_link.short_description = "Email"

    def is_read_badge(self, obj):
        if obj.is_read:
            return format_html(
                '<span style="background:#28a745;color:white;padding:4px 8px;border-radius:12px;">O‘qilgan</span>'
            )
        return format_html(
            '<span style="background:#dc3545;color:white;padding:4px 8px;border-radius:12px;font-weight:bold;">Yangi</span>'
        )
    is_read_badge.short_description = "Holati"
    is_read_badge.allow_tags = True

    # O'qilmagan xabarlarni avtomatik belgilash
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f"{updated} ta xabar o‘qilgan deb belgilandi.")
    mark_as_read.short_description = "Tanlanganlarni o‘qilgan deb belgilash"

    actions = ['mark_as_read']

    fieldsets = (
        ('Yuboruvchi', {
            'fields': (('name', 'email'), 'subject')
        }),
        ('Xabar', {
            'fields': ('body', 'is_read', 'sent_at'),
        }),
    )

    readonly_fields = ('name', 'email', 'subject', 'body', 'sent_at')

    # Xabarni ochganda avtomatik o'qilgan deb belgilash
    def change_view(self, request, object_id, form_url='', extra_context=None):
        response = super().change_view(request, object_id, form_url, extra_context)
        if object_id:
            Message.objects.filter(id=object_id, is_read=False).update(is_read=True)
        return response
