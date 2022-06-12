from . import parser, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICE = (("Dorama", "Dorama"), ("Vapes", "Vapes"), ("Movies", "Movies"))
    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            "media_type",
        ]

    def parse_data(self):
        if self.data["media_type"] == "Dorama":
            dorama_parser = parser.parser_func_dorama()
            for data in dorama_parser:
                models.Dorama.objects.create(**data)
        elif self.data["media_type"] == "Vapes":
            vapes_parser = parser.parser_func_vapes()
            for data in vapes_parser:
                models.Vapes.objects.create(**data)
        elif self.data["media_type"] == "Movies":
            movies_parser = parser.parser_func_movies()
            for data in movies_parser:
                models.Movies.objects.create(**data)
