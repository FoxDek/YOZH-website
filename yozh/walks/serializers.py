import os

from rest_framework import serializers
from .models import Walk, WalkImage

class WalkImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalkImage
        fields = ['image']

    def to_representation(self, instance):
        return instance.image.name

class WalkSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Walk
        fields = '__all__'

    def get_images(self, obj):
        return [os.path.basename(image.image.name) for image in obj.images.all()]

class WalkCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True
    )

    class Meta:
        model = Walk
        fields = ['title', 'description', 'places', 'hours_duration', 'images']

    def create(self, validated_data):
        images = validated_data.pop('images')
        walk = Walk.objects.create(**validated_data)
        for image in images:
            WalkImage.objects.create(walk=walk, image=image)
        return walk
