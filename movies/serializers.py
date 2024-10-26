from rest_framework import serializers
from movies.models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Movies` instance, given the validated data.
        """
        return Movies.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Movies` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.year = validated_data.get('year', instance.year)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.director = validated_data.get('director', instance.director)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance