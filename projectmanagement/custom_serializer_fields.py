from rest_framework import serializers


class BasicIdAndTitleField(serializers.RelatedField):
    def to_representation(self, value):
        return {"id": value.id, "title": value.title}


class CommentField(serializers.RelatedField):
    def to_representation(self, value):
        return {"user": value.user.id, "id": value.id, "title": value.title, "text": value.text}
