from django.shortcuts import render
from rest_framework import generics, mixins

from .models import Academic
from .serializer import AcademicSerializer

# Create your views here.
"""                title: "A Variant Model of TGAN for Music Generation",
                abstract: "In the past five years, we have seen an increase in generative adversarial networks (GANs) and their applications for image generation. Due to the randomness and unpredictability of the structure of music, music generation is well suited to the use of GANs. Numerous studies have been published on music generation by using temporal GANs. However, few studies have focused on the relationships between melodies and chords, and the effects of latent space on time sequence. We also propose a new method to implement latent structure on GANs for music generation.The main innovation of the proposed model is the use of new discriminator to recognize the time sequence of music and use of a pretrained beat generator to improve the quality of patterned melodies and chords.Results indicated that the pretrained model improved the quality of generated music.",
                url: "https://dl.acm.org/doi/abs/10.1145/3399871.3399888",
                github: null,
                authors: "Cheng, P. S., Lai, C. Y., Chang, C. C., Chiou, S. F., & Yang, Y. C.",
                publisher: "In Proceedings of the 2020 Asia Service Sciences and Software Engineering Conference (2020, May)",
                gallary: [],
                """


class AcademicMixinApiView(
        generics.GenericAPIView,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin):

    serializer_class = AcademicSerializer
    queryset = Academic.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)
