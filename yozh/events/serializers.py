import os

from rest_framework import serializers
from .models import Event, EventImage

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['image']

    def to_representation(self, instance):
        return instance.image.name

class EventSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_images(self, obj):
        return [os.path.basename(image.image.name) for image in obj.images.all()]

class EventCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True
    )

    class Meta:
        model = Event
        fields = ['title', 'description', 'coordinates_x', 'coordinates_y', 'is_partner_event', 'images']

    def create(self, validated_data):
        images = validated_data.pop('images')
        event = Event.objects.create(**validated_data)
        for image in images:
            EventImage.objects.create(event=event, image=image)
        return event
