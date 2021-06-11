from rest_framework import serializers


class ViewSerializer(serializers.Serializer):
    recipient_email = serializers.CharField()
    subject = serializers.CharField(allow_blank=True, allow_null=True)
    message = serializers.CharField(allow_blank=True, allow_null=True)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if not ret.get('subject', None):
            ret.update({'subject': 'This email is reply automatic'})
        if not ret.get('message', None):
            ret.update({'message': 'This email is reply automatic For tell you \'Accept me and Contact me now\''})
        return ret
