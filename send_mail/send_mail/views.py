from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from send_mail.serializer import ViewSerializer
from django.core.mail import EmailMessage



class SendMailViews(GenericAPIView):
    serializer_class = ViewSerializer
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        email = []
        email.append(str(serializer.data.get('recipient_email', None)).strip())
        subject_message = serializer.data.get('subject', None)
        message = serializer.data.get('message', None)

        email = EmailMessage(subject=subject_message, body=message, to=email)
        email.send()

        return Response(data={'Email send success'}, status=status.HTTP_201_CREATED)
