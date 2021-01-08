class FormValidMixin():
    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.athor = self.request.user
        return super().form_valid(form)