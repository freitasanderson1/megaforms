from django.contrib import admin

from django.contrib.admin import ModelAdmin

from django.utils.crypto import get_random_string

from django.contrib.admin.options import TabularInline, StackedInline
from django.template.loader import get_template
from django.utils.functional import cached_property


##############
from questionario.models import TipoQuestionario, ItemQuestionario, OpcoesItemQuestionario
from questionario.forms import ItemQuestionarioAdminForm
from questionario.admin import ItemQuestionarioAdmin
class OpcoesItemQuestionarioInline(StackedInline):
    model = OpcoesItemQuestionario
    extra = 1

class MyForm(StackedInline.form):

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.instance.form = self

    def is_valid(self):
        return super().is_valid() and self.nested.formset.is_valid()

    @cached_property
    def nested(self):
        modeladmin = ItemQuestionarioAdmin(self._meta.model, self.modeladmin.admin_site)

        # get formsets and instances for change/add view depending on the request
        formsets, instances = modeladmin._create_formsets(self.modeladmin.request, self.instance, change=self.instance.pk)

        # gets the inline from inline_formsets
        inline = modeladmin.get_inline_formsets(self.modeladmin.request, formsets[:1], instances[:1], self.instance)[0]

        # handles prefix
        inline.formset.prefix = f'{self.prefix}_{formsets[0].prefix}'.replace('-', '_')
        return inline

    def is_multipart(self, *args, **kwargs):
        return super().is_multipart() or self.nested.formset.form().is_multipart()

    @cached_property
    def changed_data(self):
        changed_inline_fields = []
        for form in self.nested.formset:
            for name, bf in form._bound_items():
                if bf._has_changed():
                    changed_inline_fields.append(name)
        return super().changed_data + changed_inline_fields

    def save(self, *args, **kwargs):
        response = super().save(*args, **kwargs)
        self.nested.formset.save(*args, **kwargs)
        return response

class ItemQuestionarioInline(admin.TabularInline):
    model = ItemQuestionario
    # template = "admin/questionario/itemquestionario_inline.html"
    extra = 1


    fieldsets = (
        (None, {
            "fields": (
                ['descricao', 'tipo']
            ),
        }),
        ('Opções', {
            "fields": (
                ['opcoes_inline',]
            ),
        }),

    )
    
    readonly_fields = ('opcoes_inline',)
    form = MyForm

    def opcoes_inline(self, obj=None, *args, **kwargs):
        context = getattr(self.modeladmin.response, 'context_data', None) or {}
        # insert nested inline from form
        return get_template(obj.form.nested.opts.template).render(context | {'inline_admin_formset': obj.form.nested}, self.modeladmin.request)

    def get_formset(self, *args, **kwargs):
        formset = super().get_formset(*args, **kwargs)
        # from.modeladmin is needed in property form.nested
        # for nested inline
        formset.form.modeladmin = self.modeladmin
        return formset


@admin.register(TipoQuestionario)
class TipoQuestionarioAdmin(ModelAdmin):
    list_display = ('id','nome','tipoDoQuestionario','slug','ativo')
    inlines = [
        ItemQuestionarioInline,
    ]
    # autocomplete_fields = ['quemCadastrou',]
    readonly_fields = ['quemCadastrou','slug',]
    icon_name = 'content_paste'
    
    def changeform_view(self, request, *args, **kwargs):
        self.request = request
        return super().changeform_view(request, *args, **kwargs)

    def render_change_form(self, request, *args, **kwargs):
        self.response = super().render_change_form(request, *args, **kwargs)
        return self.response

    def get_inline_instances(self, *args, **kwargs):
        yield from ((inline, vars(inline).update(modeladmin=self))[0] for inline in super().get_inline_instances(*args, **kwargs))

    def save_model(self, request, obj, form, change):

        if not obj.quemCadastrou:
            obj.quemCadastrou = request.user

        super(TipoQuestionarioAdmin, self).save_model(request, obj, form, change)
    class Media:
        js = ('assets/JS/admin/ScriptQuestionarioAdmin.js',)    
        css = {
             'all': ('assets/CSS/admin/QuestionarioAdmin.css',)
        }