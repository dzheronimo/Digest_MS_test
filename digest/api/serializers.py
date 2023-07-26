from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='post_id')
    title = serializers.CharField()
    post = serializers.CharField()
    rating = serializers.IntegerField()


class DigestSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=512)
    digest_list = PostSerializer(read_only=True, many=True)
